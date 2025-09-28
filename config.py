import os

# Configuration for models and settings
class Config:
    # Whisper model for transcription (faster-whisper model size)
    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "small")

    # Summarization model
    SUMMARIZER_MODEL = os.getenv("SUMMARIZER_MODEL", "facebook/bart-large-cnn")

    # Summary parameters
    SUMMARY_MAX_LENGTH = int(os.getenv("SUMMARY_MAX_LENGTH", "100"))
    SUMMARY_MIN_LENGTH = int(os.getenv("SUMMARY_MIN_LENGTH", "30"))

    # Logging level
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Server settings
    SERVER_NAME = os.getenv("SERVER_NAME", "0.0.0.0")
    SERVER_PORT = int(os.getenv("SERVER_PORT", "7861"))

config = Config()