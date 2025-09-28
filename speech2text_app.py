# speech2text_app.py

import logging
from faster_whisper import WhisperModel
from config import config

# Cache model globally (not thread-safe, but simple for this app)
_model_cache = {}

def transcribe(audio_file: str, model: str = config.WHISPER_MODEL) -> str:
    """
    Transcribe audio into text using Faster Whisper ASR.

    Args:
        audio_file (str): Path to audio file
        model (str): Whisper model size (tiny, base, small, medium, large)

    Returns:
        str: Transcript text
    """
    try:
        if model not in _model_cache:
            logging.info(f"Loading Whisper model: {model}")
            _model_cache[model] = WhisperModel(model, device="auto", compute_type="float16")

        whisper_model = _model_cache[model]
        segments, info = whisper_model.transcribe(audio_file, beam_size=5)

        transcript = " ".join([segment.text for segment in segments])
        logging.info(f"Transcription completed. Language: {info.language} (probability: {info.language_probability:.2f})")
        return transcript.strip()
    except Exception as e:
        logging.error(f"Error during transcription: {e}")
        raise
