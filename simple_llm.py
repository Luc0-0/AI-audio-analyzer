# simple_llm.py

from transformers import pipeline

def summarize_text(text: str, model: str = "facebook/bart-large-cnn") -> str:
    """
    Summarize transcript into shorter text.

    Args:
        text (str): Transcript text
        model (str): Summarization model

    Returns:
        str: Summary
    """
    # Load model only once
    global summarizer
    if "summarizer" not in globals():
        summarizer = pipeline("summarization", model=model)

    # HuggingFace models have max token limits → chunk if too long
    if len(text.split()) > 700:  
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        summaries = [summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]["summary_text"] for chunk in chunks]
        return " ".join(summaries)
    else:
        return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]
