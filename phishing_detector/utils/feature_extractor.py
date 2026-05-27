SUSPICIOUS_KEYWORDS = [
    "verify",
    "login",
    "urgent",
    "click",
    "password",
    "bank",
    "free",
    "winner"
]


def extract_features(text, urls):
    features = {}

    # URL count
    features["url_count"] = len(urls)

    # Email length
    features["email_length"] = len(text)

    # Suspicious keywords
    detected_keywords = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in text:
            detected_keywords.append(keyword)

    features["keywords"] = detected_keywords

    return features