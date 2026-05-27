import joblib

from utils.preprocess import clean_text
from utils.feature_extractor import extract_features


model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_email(email_text):
    cleaned_text, urls = clean_text(email_text)

    features = extract_features(cleaned_text, urls)

    vectorized_text = vectorizer.transform([cleaned_text])

    prediction = model.predict(vectorized_text)[0]

    probability = model.predict_proba(vectorized_text)[0]

    confidence = max(probability) * 100

    label = "PHISHING" if prediction == 1 else "SAFE"

    return {
        "prediction": label,
        "confidence": confidence,
        "url_count": features["url_count"],
        "keywords": features["keywords"]
    }