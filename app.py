import gradio as gr
from speech2text_app import transcribe
from simple_llm import summarize_text

import os
import logging
from config import config

# Premium CSS
custom_css = """
body {
    background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
    font-family: 'Poppins', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #1f2937;
    margin: 0;
    padding: 0;
}

.gradio-container {
    max-width: 1100px;
    margin: 40px auto;
    padding: 30px;
    background: white;
    border-radius: 24px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}

h1 {
    color: #111827;
    text-align: center;
    font-weight: 800;
    font-size: 2.7em;
    margin-bottom: 10px;
}

.subheading {
    text-align: center;
    font-size: 1.15em;
    color: #4b5563;
    margin-bottom: 35px;
}

.features {
    display: flex;
    justify-content: space-between;
    margin-bottom: 40px;
    color: #FDEB9E;
}

.feature-card {
    flex: 1;
    margin: 0 10px;
    background: #f9fafb;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: transform 0.2s;
}

.feature-card:hover {
    transform: translateY(-4px);
}

.feature-card h3 {
    margin-bottom: 10px;
    font-size: 1.2em;
    color: #2563eb;
}

.feature-card p {
    color: #1f2937;
    font-size: 0.95em;
}

.gr-button {
    background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
    border: none;
    border-radius: 14px !important;
    color: white !important;
    font-weight: 600;
    font-size: 1.05em;
    padding: 12px 20px;
    transition: all 0.3s ease;
}

.gr-button:hover {
    transform: scale(1.04);
    box-shadow: 0 6px 18px rgba(79, 70, 229, 0.4);
}

.gr-tab {
    border-radius: 14px !important;
    padding: 12px;
    font-weight: 600;
    background: #f3f4f6;
}

.gr-textbox {
    border-radius: 14px !important;
    border: 1px solid #e5e7eb !important;
    background: #fafafa !important;
    font-size: 0.95em !important;
    line-height: 1.5;
}
"""

def analyze(audio_file: str) -> tuple[str, str]:
    """Transcribe + summarize audio"""
    try:
        if not os.path.isfile(audio_file):
            raise ValueError("Invalid audio file path.")

        logging.info("Transcription started...")
        transcript = transcribe(audio_file)

        if not transcript.strip():
            return "No transcript generated.", "No summary available."

        logging.info("Summarization started...")
        summary = summarize_text(transcript)

        return transcript, summary
    except Exception as e:
        logging.error(f"Error: {e}")
        return f"⚠️ Error: {str(e)}", "Summary unavailable."

with gr.Blocks(css=custom_css) as demo:
    # Hero section
    gr.Markdown("<h1>🎧 Audio AI Analyzer</h1>")
    gr.Markdown("<p class='subheading'>Turn conversations into clarity with AI-powered transcription & summarization.</p>")

    # Feature highlights
    gr.HTML(
        """
        <div class="features">
            <div class="feature-card">
                <h3>📝 Full Transcript</h3>
                <p>Complete text conversion of your audio for easy reading & review.</p>
            </div>
            <div class="feature-card">
                <h3>✨ Concise Summary</h3>
                <p>Key points and highlights automatically extracted from long speech.</p>
            </div>
            <div class="feature-card">
                <h3>⚡ Powered by AI</h3>
                <p>Advanced Whisper + HuggingFace models working behind the scenes.</p>
            </div>
        </div>
        """
    )

    # Analyzer section
    with gr.Row():
        with gr.Column(scale=1):
            audio = gr.Audio(
                type="filepath",
                sources=["microphone", "upload"],
                label="🎤 Upload or Record Audio"
            )
            run_btn = gr.Button("🚀 Analyze Audio")

        with gr.Column(scale=2):
            with gr.Tab("📜 Transcript"):
                transcript_box = gr.Textbox(
                    label="Transcript",
                    lines=14,
                    interactive=False,
                    placeholder="Your transcript will appear here..."
                )
            with gr.Tab("✨ Summary"):
                summary_box = gr.Textbox(
                    label="Summary",
                    lines=14,
                    interactive=False,
                    placeholder="Concise summary will appear here..."
                )

    run_btn.click(
        analyze,
        inputs=audio,
        outputs=[transcript_box, summary_box]
    )

if __name__ == "__main__":
    logging.basicConfig(level=getattr(logging, config.LOG_LEVEL.upper(), logging.INFO))
    demo.launch(server_name=config.SERVER_NAME, server_port=config.SERVER_PORT)
