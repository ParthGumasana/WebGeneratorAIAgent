AI Website Generator Using CodeLlama

🧠 Project Summary

This AI-powered web app generates multi-page, responsive websites based on user input. It uses OpenAI’s CodeLlama model (run via Ollama) to create HTML and CSS files with full navigation support. Users can select a business type and receive a downloadable .zip containing the entire website.

⚠️ Note: This is a prototype and does not produce fully functional, production-ready websites. It creates basic HTML/CSS templates which can be further customized and edited by developers.

🚀 Features

Generate websites for multiple business types

Multi-page HTML generation

Shared styles.css for design consistency

Dynamic navigation bars across all pages

Flask-based web interface for interaction

One-click ZIP download of generated sites

🏗️ Tech Stack

Python

Flask

Ollama (with CodeLlama model)

📁 File Structure

.
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # HTML form for user input
├── generated_sites/      # Auto-generated folders and zipped websites
├── requirements.txt
├── README.md             # This file
└── debug_output.txt      # Captures model output for debugging

🧾 requirements.txt

Flask==2.3.3

⚠️ Make sure Ollama is installed separately on your machine.

Install Python dependencies:

pip install -r requirements.txt

Install and run Ollama:

# Download and install Ollama from https://ollama.com
ollama run codellama

🔧 How to Run

git clone https://github.com/yourusername/ai-website-generator.git
cd ai-website-generator
pip install -r requirements.txt
python app.py

Visit: http://localhost:5000 in your browser.

🧪 How It Works

User selects a business type from the form

Flask generates a custom prompt and sends it to CodeLlama via ollama run

Model output is parsed into multiple HTML files and one styles.css

Files are zipped and returned for download

📸 Screenshots (Optional)

Include screenshots of your form UI and generated site structure.

👨‍💼 For HR/Presentation

“I developed an AI-powered agent using CodeLlama to generate complete, styled websites based on business categories. It dynamically creates multiple pages with internal navigation and supports instant download, all through a lightweight Flask web app.”

📜 License

MIT License

