from flask import Flask, request, render_template, send_file
import subprocess
import os
import zipfile
from datetime import datetime

app = Flask(__name__)
OUTPUT_DIR = "generated_sites"

def get_website_structure(business_type: str):
    mapping = {
        "portfolio": {
            "pages": ["index", "about", "projects", "contact"],
            "style": "modern",
            "theme": "dark"
        },
        "restaurant": {
            "pages": ["index", "menu", "gallery", "contact"],
            "style": "elegant",
            "theme": "warm"
        },
        "ecommerce": {
            "pages": ["index", "products", "cart", "contact"],
            "style": "clean",
            "theme": "light"
        },
        "agency": {
            "pages": ["index", "services", "portfolio", "team", "contact"],
            "style": "corporate",
            "theme": "professional"
        }
    }
    return mapping.get(business_type.lower(), mapping["portfolio"])

def generate_prompt(business_type: str):
    structure = get_website_structure(business_type)
    pages = structure["pages"]
    nav_links = "".join([f'<a href="{p}.html">{p.capitalize()}</a> ' for p in pages])
    pages_list = ', '.join(pages)

    return f"""
Generate a multi-page responsive website using HTML and CSS.

Business type: {business_type}
Pages to include: {pages_list}
Theme: {structure['theme']}
Style: {structure['style']}

Instructions:
- Create separate HTML files named: {pages_list.replace(', ', '.html, ')}.html
- Before each file, write: FILE: filename.html (e.g., FILE: index.html)
- Include this navigation bar in **every** page at the top:
  <nav>{nav_links}</nav>
- Each page must link to all others.
- Link CSS in every page with: <link rel="stylesheet" href="styles.css">
- Place all CSS styles in one file named FILE: styles.css
- Only output code, no explanations.
"""

def run_codellama(prompt: str) -> str:
    try:
        process = subprocess.Popen(
            ['ollama', 'run', 'codellama'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        output, _ = process.communicate(input=prompt)

        # Log the full model output
        with open("debug_output.txt", "w", encoding="utf-8") as f:
            f.write(output)

        return output
    except Exception as e:
        return f"Error: {str(e)}"

def save_files_from_output(output: str, output_folder: str):
    os.makedirs(output_folder, exist_ok=True)
    current_file = None
    buffer = []

    for line in output.splitlines():
        if line.strip().startswith("FILE:"):
            if current_file and buffer:
                with open(os.path.join(output_folder, current_file), "w", encoding="utf-8") as f:
                    f.write('\n'.join(buffer))
            current_file = line.strip().replace("FILE:", "").strip()
            buffer = []
        else:
            buffer.append(line)

    # Save the last file
    if current_file and buffer:
        with open(os.path.join(output_folder, current_file), "w", encoding="utf-8") as f:
            f.write('\n'.join(buffer))

def zip_output_folder(folder_path: str, zip_name: str):
    zip_path = zip_name + ".zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)
    return zip_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        business_type = request.form["business_type"]
        prompt = generate_prompt(business_type)
        ai_output = run_codellama(prompt)

        # Create unique session folder
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_folder = os.path.join(OUTPUT_DIR, f"{business_type}_{timestamp}")
        save_files_from_output(ai_output, session_folder)

        zip_file = zip_output_folder(session_folder, session_folder)
        return send_file(zip_file, as_attachment=True)

    return render_template("index.html", error=None)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    app.run(debug=True)
