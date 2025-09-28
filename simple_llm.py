# simple_llm.py

import logging
from transformers import pipeline
from config import config

# Cache summarizer models
_summarizer_cache = {}

def summarize_text(text: str, model: str = config.SUMMARIZER_MODEL) -> str:
    """
    Summarize transcript into shorter text.

    Args:
        text (str): Transcript text
        model (str): Summarization model

    Returns:
        str: Summary
    """
    try:
        if model not in _summarizer_cache:
            logging.info(f"Loading summarization model: {model}")
            _summarizer_cache[model] = pipeline("summarization", model=model)

        summarizer = _summarizer_cache[model]

        # Approximate token limit (BART models ~1024 tokens)
        words = text.split()
        if len(words) > 500:  # Conservative word limit
            # Chunk by words, approximately 400 words per chunk
            chunk_size = 400
            chunks = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
            summaries = []
            for chunk in chunks:
                summary = summarizer(chunk, max_length=config.SUMMARY_MAX_LENGTH, min_length=config.SUMMARY_MIN_LENGTH, do_sample=False)[0]["summary_text"]
                summaries.append(summary)
            return " ".join(summaries)
        else:
            return summarizer(text, max_length=config.SUMMARY_MAX_LENGTH, min_length=config.SUMMARY_MIN_LENGTH, do_sample=False)[0]["summary_text"]
    except Exception as e:
        logging.error(f"Error during summarization: {e}")
        raise
