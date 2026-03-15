from transformers import pipeline

# Load model
model_name = "facebook/bart-large-cnn"

summarizer = pipeline(
    task="summarization",
    model=model_name
)

def summarize_text(text, max_len, min_len):

    result = summarizer(
        text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )

    return result[0]["summary_text"]