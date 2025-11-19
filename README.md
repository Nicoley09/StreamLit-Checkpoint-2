
## Overview

The **Financial Inclusion Predictor** is a machine learning application that predicts whether an individual in East Africa is likely to have a bank account based on demographic and socio-economic features.

Financial inclusion ensures that individuals and businesses have access to useful and affordable financial products and services such as transactions, payments, savings, credit, and insurance. This project aims to identify individuals who are more likely to be included in formal financial systems.

---

## Features

* **Interactive Streamlit app** with sidebar inputs for user-friendly predictions.
* Predicts **bank account ownership** for individuals based on:

  * Country
  * Year
  * Unique ID
  * Location type (Urban/Rural)
  * Cellphone access
  * Household size
  * Age
  * Gender
  * Relationship with head of household
  * Marital status
  * Education level
  * Job type
* Displays **prediction** and **probability** of having a bank account.

---

## Dataset

The dataset contains **demographic and financial information for ~33,600 individuals across East Africa**.

* **Source:** Zindi – Financial Inclusion in Africa competition
* **Features:** 13 columns including `country`, `year`, `uniqueid`, `location_type`, `cellphone_access`, `household_size`, `age_of_respondent`, `gender_of_respondent`, `relationship_with_head`, `marital_status`, `education_level`, `job_type`, and `bank_account` (target).

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/financial-inclusion-predictor.git
cd financial-inclusion-predictor
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Make sure the trained model file `financial_inclusion_model.pkl` is in the same directory as `app.py`.

---

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Enter the demographic details in the sidebar.
3. Click **Predict** to see whether the individual is likely to have a bank account, along with the probability.

---

## Deployment

* The app is **ready for deployment** on [Streamlit Community Cloud](https://share.streamlit.io/).
* Steps:

  1. Push your project to GitHub.
  2. Log in to Streamlit Share and connect your GitHub repo.
  3. Deploy the app directly from the repo.

---

## Model

* **Type:** Random Forest Classifier (trained using scikit-learn)
* **Purpose:** Predicts bank account ownership
* **Input:** Preprocessed demographic features
* **Output:** Binary classification (1 = has a bank account, 0 = does not have a bank account)

---

## Folder Structure

```
financial-inclusion-predictor/
│
├── app.py                     # Streamlit application
├── financial_inclusion_model.pkl  # Trained ML model
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── data/                      # (Optional) dataset folder
```

---

## Technologies Used

* Python 3.x
* pandas
* scikit-learn
* Streamlit

---

## Author

**Nicole Mugo**

* Passionate about data science and financial inclusion.
* GitHub: [https://github.com/yourusername](https://github.com/yourusername)

---


