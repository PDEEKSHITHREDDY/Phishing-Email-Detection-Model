import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

import subprocess

from predict import predict_email
from utils.report_generator import generate_report


# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Advanced Phishing Email Detector")
root.geometry("900x700")
root.configure(bg="#0f172a")

# ---------------- FUNCTIONS ---------------- #


def analyze_email():

    sender = sender_entry.get()
    subject = subject_entry.get()

    email_text = text_area.get("1.0", tk.END).strip()

    if not email_text:
        messagebox.showerror("Error", "Please enter email content.")
        return

    full_email = f"""
    Sender: {sender}
    Subject: {subject}

    {email_text}
    """

    result = predict_email(full_email)

    prediction = result["prediction"]

    confidence = result["confidence"]

    keywords = ", ".join(result["keywords"])

    urls = result["url_count"]

    # Result Color
    if prediction == "PHISHING":
        result_color = "#ff4d4d"
    else:
        result_color = "#4dff88"

    result_box.config(
        bg=result_color,
        fg="black"
    )

    result_text = (
        f"Prediction : {prediction}\n\n"
        f"Confidence : {confidence:.2f}%\n\n"
        f"URLs Found : {urls}\n\n"
        f"Keywords : {keywords}"
    )

    result_box.config(text=result_text)

    # Generate Report
    report_file = generate_report(
        full_email,
        prediction,
        confidence
    )

    messagebox.showinfo(
        "Report Saved",
        f"Report generated successfully!\n\n{report_file}"
    )


def clear_fields():

    sender_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)

    text_area.delete("1.0", tk.END)

    result_box.config(
        text="Detection Result Appears Here",
        bg="#1e293b",
        fg="white"
    )


def train_model():

    subprocess.run(["python", "train_model.py"])

    messagebox.showinfo(
        "Training Complete",
        "Machine Learning model trained successfully!"
    )


# ---------------- TITLE ---------------- #

title = tk.Label(
    root,
    text="PHISHING EMAIL DETECTION SYSTEM",
    font=("Helvetica", 24, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=20)

# ---------------- MAIN FRAME ---------------- #

main_frame = tk.Frame(
    root,
    bg="#1e293b",
    padx=20,
    pady=20
)

main_frame.pack(pady=10)

# ---------------- SENDER ---------------- #

sender_label = tk.Label(
    main_frame,
    text="Sender Email",
    font=("Arial", 12, "bold"),
    bg="#1e293b",
    fg="white"
)

sender_label.grid(row=0, column=0, sticky="w", pady=10)

sender_entry = tk.Entry(
    main_frame,
    width=70,
    font=("Arial", 12),
    bg="#334155",
    fg="white",
    insertbackground="white"
)

sender_entry.grid(row=0, column=1, pady=10)

# ---------------- SUBJECT ---------------- #

subject_label = tk.Label(
    main_frame,
    text="Subject",
    font=("Arial", 12, "bold"),
    bg="#1e293b",
    fg="white"
)

subject_label.grid(row=1, column=0, sticky="w", pady=10)

subject_entry = tk.Entry(
    main_frame,
    width=70,
    font=("Arial", 12),
    bg="#334155",
    fg="white",
    insertbackground="white"
)

subject_entry.grid(row=1, column=1, pady=10)

# ---------------- EMAIL BODY ---------------- #

body_label = tk.Label(
    main_frame,
    text="Email Content",
    font=("Arial", 12, "bold"),
    bg="#1e293b",
    fg="white"
)

body_label.grid(row=2, column=0, sticky="nw", pady=10)

text_area = ScrolledText(
    main_frame,
    width=65,
    height=15,
    font=("Consolas", 11),
    bg="#334155",
    fg="white",
    insertbackground="white"
)

text_area.grid(row=2, column=1, pady=10)

# ---------------- BUTTONS ---------------- #

button_frame = tk.Frame(
    root,
    bg="#0f172a"
)

button_frame.pack(pady=20)

analyze_btn = tk.Button(
    button_frame,
    text="Analyze Email",
    command=analyze_email,
    font=("Arial", 12, "bold"),
    bg="#06b6d4",
    fg="black",
    width=18,
    height=2,
    relief="flat",
    cursor="hand2"
)

analyze_btn.grid(row=0, column=0, padx=15)

train_btn = tk.Button(
    button_frame,
    text="Train Model",
    command=train_model,
    font=("Arial", 12, "bold"),
    bg="#f59e0b",
    fg="black",
    width=18,
    height=2,
    relief="flat",
    cursor="hand2"
)

train_btn.grid(row=0, column=1, padx=15)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Arial", 12, "bold"),
    bg="#ef4444",
    fg="white",
    width=18,
    height=2,
    relief="flat",
    cursor="hand2"
)

clear_btn.grid(row=0, column=2, padx=15)

# ---------------- RESULT SECTION ---------------- #

result_title = tk.Label(
    root,
    text="Detection Result",
    font=("Arial", 18, "bold"),
    bg="#0f172a",
    fg="white"
)

result_title.pack(pady=10)

result_box = tk.Label(
    root,
    text="Detection Result Appears Here",
    font=("Arial", 14),
    bg="#1e293b",
    fg="white",
    width=50,
    height=8,
    justify="left",
    padx=20,
    pady=20
)

result_box.pack(pady=10)

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    root,
    text="Cybersecurity Mini Project using Machine Learning",
    font=("Arial", 10),
    bg="#0f172a",
    fg="gray"
)

footer.pack(pady=20)

# ---------------- RUN ---------------- #

root.mainloop()