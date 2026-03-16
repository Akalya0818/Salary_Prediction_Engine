💰 SalaryPro AI: Multi-Page Machine Learning Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Project Overview
**SalaryPro AI** is a professional-grade, end-to-end Machine Learning application designed to classify individuals into income brackets (>$50K or ≤$50K) based on the UCI Adult Census dataset. 

This project goes beyond simple scripting by providing a **three-page interactive dashboard** that bridges the gap between complex data science and user-friendly web interfaces.

### 🔗 Live Deployment
> **Access the App:** [INSERT YOUR STREAMLIT OR NGROK LINK HERE]

---

## ✨ Key Features

### 🎮 1. Smart Predictor
* **Real-time Classification:** Input personal and professional data to get instant salary predictions.
* **Confidence Metrics:** Uses `predict_proba` to show the AI's certainty for each result.
* **Bulk Processing:** Support for batch CSV uploads to analyze multiple records simultaneously.

### 📊 2. Model Intelligence (Analytics)
* **Feature Importance:** Interactive Plotly charts showing which factors (Age, Education, Hours) drive the model's logic.
* **Explainable AI:** Provides transparency into the "Black Box" of Random Forest decision-making.

### 📂 3. Data Lab
* **Dataset Transparency:** Integrated view of the raw training data.
* **Exploratory Data Analysis (EDA):** Built-in charts to visualize age distributions and income splits.

---

## 🛠️ Tech Stack
* **Core:** Python 3.12
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Frontend/Deployment:** Streamlit
* **Data Handling:** Pandas, NumPy, Joblib
* **Visualization:** Plotly Express

---

## 📁 Repository Structure
```text
├── app.py              # Main Multi-page Streamlit Application
├── train_model.py      # Script used for model training and balancing
├── best_model.pk1      # Serialized Random Forest Model
├── model_columns.pk1   # Serialized Feature Index (ensures input alignment)
├── requirements.txt    # Project dependencies
├── adult 3.csv         # UCI Census Dataset
└── README.md           # Professional Documentation
----

## Installation & Usage

Clone the Project:

Bash
git clone [https://github.com/YOUR_USERNAME/salary-prediction-app.git](https://github.com/YOUR_USERNAME/salary-prediction-app.git)
cd salary-prediction-app
Install Libraries:

Bash
pip install -r requirements.txt
Run Locally:

Bash
streamlit run app.py
🧠 Model Logic & Optimization
To combat the common "Class Imbalance" issue in census data (where ≤50K earners are the majority), this model was trained using Balanced Class Weights. This ensures that high-earning profiles are identified with significantly higher sensitivity than standard models.

🤝 Contact
Developed by Akalya Looking for data-driven roles and collaboration.





2.  **Edit** the parts in brackets, like `[Your Name]`, `YOUR_USERNAME`, and `[INSERT LINK HERE]`.
3.  **Add a Screenshot:** If you can, take a screenshot of your working app and upload it to your GitHub repo, then link it in the README. It makes the project look 10x more impressive!

**Would you like me to show you how to add a "License" file to your repository to make it officially Open Source?**
