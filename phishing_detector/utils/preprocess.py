import re

STOPWORDS = {
    "the", "is", "in", "at", "which", "on",
    "and", "a", "an", "to", "for", "of"
}


def clean_text(text):
    text = text.lower()

    # Extract URLs
    urls = re.findall(r'https?://\S+|www\.\S+', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]

    cleaned_text = " ".join(words)

    return cleaned_text, urls