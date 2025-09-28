# 🎧 Audio AI Analyzer

An open-source AI web app to **transcribe audio** and **generate summaries with key points**.  
Built with [Whisper](https://huggingface.co/openai/whisper-small.en) for transcription + [HuggingFace Summarizers](https://huggingface.co/models?pipeline_tag=summarization) for summarization.  
UI powered by [Gradio](https://gradio.app/).

---

## ✨ Features

- 🎤 Upload or record audio (mic & file upload support)
- 📜 Automatic **speech-to-text transcription**
- ✨ Concise **summarization of long text**
- ⚡ Runs fully on **open-source models** (Whisper + BART/T5)
- 🌐 Simple **web interface** (Gradio)
- 🐳 Easy to containerize with **Docker**

---

## 📂 Project Structure

audio-ai-analyzer/
├── app.py # Main entrypoint (Gradio UI)
├── speech2text_app.py # Transcription module (Whisper)
├── simple_llm.py # Summarizer module (BART/T5)
├── requirements.txt # Python dependencies
├── Dockerfile # Container setup
├── .gitignore # Ignore venv/cache/junk files
└── README.md # Project documentation

---

## ⚙️ Installation (Local Development)

1. Clone the repo:

   ```bash
   git clone https://github.com/Luc0-0/AI-audio-analyzer.git
   cd AI-audio-analyzer

   ```

2. Create virtual env & install dependencies:

python -m venv venv
source venv/bin/activate # (Linux/Mac)
venv\Scripts\activate # (Windows)

pip install -r requirements.txt

3. Run the App

   python app.py

🐳 Run with Docker

Build the image:

docker build -t audio-ai-app .

Run the container:

docker run -p 7860:7860 audio-ai-app

Open http://localhost:7860

⚡ Pro Tip: Mount HuggingFace cache to avoid re-downloading models:

docker run -p 7860:7860 -v ~/.cache/huggingface:/root/.cache/huggingface audio-ai-app

🛠️ Requirements

Python 3.9+

Docker (optional, for containerization)

Internet (first run downloads HuggingFace models)

🔮 Roadmap

Add speaker diarization (who said what)

Export summaries to PDF/Notion/Markdown

Multiple summarization styles (meeting, lecture, sales)

Deploy on cloud (Render, HuggingFace Spaces, AWS, etc.)

UI refinements: JSON output, download button, styled layout

🧩 Tech Stack

Transformers
(Whisper, BART/T5)

Gradio
(UI)

Docker
(containerization)

Python 3.10

📜 License

MIT License © 2025
Open-source, free to use & extend.

👨‍💻 Author

Built by Luc (@Luc0-0)
