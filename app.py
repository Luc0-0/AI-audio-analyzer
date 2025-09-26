import gradio as gr
from speech2text_app import transcribe
from simple_llm import summarize_text

def analyze(audio_file):
    transcript = transcribe(audio_file)
    summary = summarize_text(transcript)
    return transcript, summary

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🎧 Audio AI Analyzer
        Upload or record audio and get:
        - Full **Transcript**
        - Concise **Summary**

        ⚡ Powered by Whisper + HuggingFace Summarizer
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            audio = gr.Audio(
                type="filepath",
                sources=["microphone", "upload"],
                label="🎤 Input Audio"
            )
            run_btn = gr.Button("🚀 Analyze", variant="primary")

        with gr.Column(scale=2):
            with gr.Tab("📜 Transcript"):
                transcript_box = gr.Textbox(
                    label="Transcript",
                    lines=12,
                    interactive=False
                )
            with gr.Tab("✨ Summary"):
                summary_box = gr.Textbox(
                    label="Summary",
                    lines=12,
                    interactive=False
                )

    run_btn.click(
        analyze,
        inputs=audio,
        outputs=[transcript_box, summary_box]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
