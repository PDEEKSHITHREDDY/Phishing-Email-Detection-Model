# Phishing Email Detection System

A GUI-based Machine Learning project that detects whether an email is:

- PHISHING
- SAFE

This project is built using:

- Python
- Scikit-learn
- Tkinter
- Pandas
- NumPy
- Matplotlib

It analyzes email content, detects suspicious keywords and URLs, and predicts phishing attempts using Machine Learning.

---

# Features

## Email Analysis

- Detect phishing emails
- Detect safe emails
- Analyze suspicious content
- Detect URLs inside emails

---

## Machine Learning

- TF-IDF Vectorizer
- Naive Bayes Classifier
- Model Training
- Prediction Confidence Score

---

## GUI Features

- Modern Dark Theme UI
- Sender Email Field
- Subject Field
- Email Content Area
- Analyze Button
- Train Model Button
- Clear Button
- Result Display Box

---

## Detection Information

The application shows:

- Prediction Result
- Confidence Percentage
- URL Count
- Suspicious Keywords

---

## Report Generation

Automatically generates TXT reports inside:

```plaintext
reports/
```

Each report contains:

- Email content
- Prediction result
- Confidence score
- Timestamp

---

# Project Structure

```plaintext
phishing_detector/
│
├── dataset/
│   └── emails.csv
│
├── models/
│   ├── phishing_model.pkl
│   └── vectorizer.pkl
│
├── reports/
│
├── gui/
│   └── app.py
│
├── utils/
│   ├── preprocess.py
│   ├── feature_extractor.py
│   └── report_generator.py
│
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
└── main.py
```

---

# Installation Guide

## Step 1 — Install Python

Download and install Python 3.10 or later:

- https://www.python.org/downloads/

IMPORTANT:
During installation, enable:

```plaintext
✓ Add Python to PATH
```

---

# Step 2 — Create Project Folder

```bash
mkdir phishing_detector
cd phishing_detector
```

---

# Step 3 — Create Virtual Environment (Recommended)

## Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

## Linux / Mac

```bash
python3 -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

---

# Step 4 — Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# requirements.txt

```txt
pandas
numpy
scikit-learn
matplotlib
joblib
```

---

# Step 5 — Train the Machine Learning Model

Run:

```bash
python train_model.py
```

This will:

- Load dataset
- Preprocess emails
- Train model
- Generate accuracy results
- Show confusion matrix
- Save trained model

Saved files:

```plaintext
models/phishing_model.pkl
models/vectorizer.pkl
```

---

# Step 6 — Run the GUI Application

```bash
python main.py
```

The application window will open.

---

# How to Use

## 1. Enter Sender Email

Example:

```plaintext
support@paypal-security.com
```

---

## 2. Enter Subject

Example:

```plaintext
Verify Your Account Immediately
```

---

## 3. Enter Email Content

Example:

```plaintext
Dear User,

Your account has been suspended.

Click here immediately to verify your password:
http://fake-paypal-login.com

Failure to verify within 24 hours will result in account termination.
```

---

## 4. Click "Analyze Email"

The system will display:

```plaintext
Prediction : PHISHING
Confidence : 96%
URLs Found : 1
Keywords : verify, password, click
```

---

# Example Safe Email

```plaintext
Sender: hr@company.com

Subject: Team Meeting Tomorrow

Hello Team,

Tomorrow's project meeting is scheduled at 10 AM.

Regards,
HR Team
```

---

# Example Phishing Email

```plaintext
Sender: security@paypal-alert.com

Subject: Urgent Account Verification

Dear User,

Your account has been compromised.

Click here immediately to verify your password:
http://paypal-security-check.com

Failure to verify will suspend your account.
```

---

# Machine Learning Workflow

## Data Preprocessing

- Lowercase conversion
- Special character removal
- Stopword removal
- URL extraction

---

## Feature Extraction

The system extracts:

- TF-IDF text features
- URL count
- Email length
- Suspicious keywords

Keywords include:

- verify
- urgent
- login
- password
- click
- bank

---

# Model Evaluation

The system displays:

- Accuracy Score
- Classification Report
- Confusion Matrix

---

# Output Reports

Generated reports are stored in:

```plaintext
reports/
```

Example:

```plaintext
report_20260527_184500.txt
```

---

# Common Errors and Fixes

## Error: No module named sklearn

Solution:

```bash
pip install scikit-learn
```

---

## Error: Model file not found

Solution:

Train the model first:

```bash
python train_model.py
```

---

## Error: Python not recognized

Solution:

Reinstall Python and enable:

```plaintext
Add Python to PATH
```

---

# Future Improvements

You can upgrade this project by adding:

- SQLite database
- Gmail API integration
- Real-time URL scanning
- Deep Learning models
- Spam score analysis
- Drag-and-drop email files
- Dashboard analytics
- Light/Dark mode switch
- PDF report generation

---

# Technologies Used

- Python
- Tkinter
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Regex
- Joblib

---

# Educational Purpose

This project is developed for:

- Cybersecurity learning
- Internship tasks
- Academic mini projects
- Machine Learning practice

---

# PINNINTI DEEKSHITH REDDY


Phishing Email Detection System using Machine Learning and GUI.
