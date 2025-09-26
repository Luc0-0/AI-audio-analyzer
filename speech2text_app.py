# speech2text_app.py

from transformers import pipeline

def transcribe(audio_file: str, model: str = "openai/whisper-small.en") -> str:
    """
    Transcribe audio into text using HuggingFace Whisper ASR.
    
    Args:
        audio_file (str): Path to audio file
        model (str): Whisper model (tiny, base, small, medium, large)
        
    Returns:
        str: Transcript text
    """
    # Load model only once (cache)
    global asr_pipe
    if "asr_pipe" not in globals():
        asr_pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            chunk_length_s=30
        )
    result = asr_pipe(audio_file)
    return result["text"]
