from datetime import datetime
import os


def generate_report(email_text, prediction, confidence):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"reports/report_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write("========== PHISHING EMAIL REPORT ==========\n\n")

        file.write(f"Timestamp : {timestamp}\n\n")

        file.write("EMAIL CONTENT\n")
        file.write("------------------------------------------\n")
        file.write(email_text + "\n\n")

        file.write("------------------------------------------\n")

        file.write(f"Prediction : {prediction}\n")
        file.write(f"Confidence : {confidence:.2f}%\n")

    return filename