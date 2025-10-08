from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

MAX_TOKENS = 800  # safe limit for BART

def chunk_text(text, max_tokens=MAX_TOKENS):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + max_tokens, len(words))
        chunks.append(" ".join(words[start:end]))
        start = end
    return chunks

def auto_summarize(text):
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        input_length = len(chunk.split())
        max_length = max(10, input_length // 2)
        summary = summarizer(
            chunk, max_length=max_length, min_length=5, do_sample=False
        )[0]["summary_text"]
        summaries.append(summary)

    return " ".join(summaries)
