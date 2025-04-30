# AI Website Generator Using CodeLlama

## Project Summary
This AI-powered prototype generates basic multi-page website templates using OpenAI’s CodeLlama model via Ollama. It supports different business types and produces zipped HTML/CSS templates with navigation, which can be further edited and customized by developers.

## Features
- Generates website templates for various business types
- Creates multiple HTML pages with navigation
- Includes a shared `styles.css` for consistent styling
- User input handled via a Flask web interface
- ZIP download of generated site structure

## Tech Stack
- Python 3
- Flask
- Ollama (CodeLlama model)

## File Structure
```
.
├── app.py
├── templates/
│   └── index.html
├── generated_sites/
├── requirements.txt
├── README.md
└── debug_output.txt
```

## Installation
### Requirements
- Python 3.9+
- [Ollama](https://ollama.com) with CodeLlama installed

### Setup
```bash
git clone https://github.com/yourusername/ai-website-generator.git
cd ai-website-generator
pip install -r requirements.txt
```

### Run
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

## requirements.txt
```
Flask==2.3.3
```

## License
MIT License
