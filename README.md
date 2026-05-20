# 🚀 Student Performance Prediction System

An end-to-end Machine Learning project built using a modular and production-oriented architecture.

This application predicts a student's **Math Score** based on demographic and academic performance data using multiple regression models and a complete ML pipeline.

---

# 🌐 Live Demo

👉 [Live Application](https://ml-project-deployment.onrender.com)

---

# 📌 Project Highlights

✅ End-to-End ML Pipeline  
✅ Modular Project Architecture  
✅ FastAPI Backend  
✅ Interactive Frontend using HTML/CSS  
✅ Multiple ML Models with Hyperparameter Tuning  
✅ Custom Logging & Exception Handling  
✅ Model Serialization using Pickle  
✅ Cloud Deployment on Render  
✅ Production-Oriented Folder Structure  

---

# 🧠 Problem Statement

The objective of this project is to predict a student's **math score** using the following features:

- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

---

# 🏗️ Project Architecture

```text
ML_project_deployment/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── logs/
│
├── notebooks/
│
├── src/
│   │
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   └── __init__.py
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── render.yaml
├── .python-version
├── README.md
└── .gitignore
```

---

# ⚙️ Tech Stack

## 🧪 Machine Learning

- Scikit-learn
- XGBoost
- CatBoost
- Pandas
- NumPy

---

## 🌐 Backend

- FastAPI
- Uvicorn

---

## 🎨 Frontend

- HTML
- CSS
- Jinja2 Templates

---

## ☁️ Deployment

- Render Cloud Platform

---

# 🔄 ML Pipeline Workflow

## 1️⃣ Data Ingestion

Responsible for:

- reading dataset
- train-test split
- saving raw artifacts

---

## 2️⃣ Data Transformation

Handles:

- missing value handling
- categorical encoding
- feature scaling
- preprocessing pipeline creation

---

## 3️⃣ Model Training

Multiple regression models are trained and evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- AdaBoost Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor

Features:

- GridSearchCV
- Hyperparameter tuning
- Best model selection
- R² score evaluation

---

## 4️⃣ Prediction Pipeline

The prediction pipeline:

- loads trained model
- loads preprocessing object
- transforms incoming user data
- returns predicted math score

---

# 📜 Core Modules

## ✅ logger.py

Custom logging system for:

- execution tracking
- debugging
- timestamped logs
- monitoring pipeline flow

---

## ✅ exception.py

Custom exception handling with:

- filename tracking
- line-number tracking
- readable error messages

---

## ✅ utils.py

Reusable helper functions for:

- saving objects
- loading objects
- evaluating models
- serialization utilities

---

# 🌐 Frontend Features

The web interface allows users to:

- input student details
- submit prediction requests
- instantly receive predicted math score

The frontend is connected to FastAPI using HTML forms and Jinja2 templates.

---

# 🚀 Running the Project Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Abhoy-Ghosh/ML_project_deployment.git
```

---

## 2️⃣ Move Into Project

```bash
cd ML_project_deployment
```

---

## 3️⃣ Create Local Conda Environment

```bash
conda create --prefix ./venv python=3.11
```

Activate environment:

```bash
conda activate ./venv
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Train Model Pipeline

```bash
python -m src.components.data_ingestion
```

This generates:

- `model.pkl`
- `preprocessor.pkl`

inside the `artifacts/` folder.

---

## 6️⃣ Run FastAPI Application

```bash
uvicorn app:app --reload
```

---

# 🌐 Open Application

Visit locally:

```text
http://127.0.0.1:8000
```

Live deployment:

👉 :contentReference[oaicite:1]{index=1}

---

# 📊 Input Features

| Feature | Type |
|---|---|
| Gender | Categorical |
| Race/Ethnicity | Categorical |
| Parent Education | Categorical |
| Lunch Type | Categorical |
| Test Preparation Course | Categorical |
| Reading Score | Numerical |
| Writing Score | Numerical |

---

# ☁️ Deployment Journey

This project was deployed on Render using:

- FastAPI
- Uvicorn
- Python 3.11
- Render YAML configuration
- Production dependency optimization

During deployment, major engineering concepts explored included:

- dependency management
- Python version compatibility
- cloud deployment debugging
- ML package optimization
- inference deployment workflows

---

# 🎯 Future Improvements

- Docker Support
- CI/CD Pipeline
- AWS Deployment
- Authentication System
- Database Integration
- Model Monitoring
- Experiment Tracking
- Advanced UI/UX
- REST API Documentation

---

# 🧠 Learning Outcomes

This project helped in understanding:

- production-grade ML architecture
- modular coding practices
- ML pipelines
- model deployment
- FastAPI integration
- debugging production environments
- cloud infrastructure basics
- dependency resolution workflows

---

# 👨‍💻 Author

## Abhoy Ghosh

Machine Learning & Full Stack Development Enthusiast

GitHub: :contentReference[oaicite:2]{index=2}

---

# ⭐ Support

If you found this project useful, consider giving the repository a star ⭐
