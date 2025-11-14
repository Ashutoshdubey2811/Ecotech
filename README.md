# End to end Data Science project
Ecotech is an end-to-end Machine Learning pipeline that automates data ingestion, EDA, data transformation, model benchmarking, and model selection.
The system evaluates multiple ML algorithms and automatically selects the best-performing model based on accuracy.
The final model (CatBoost in this case) is saved and ready for deployment.

⭐ Features
✅ 1. Automated Data Ingestion

Reads raw dataset

Validates and cleans data

Handles missing values

Splits into train & test

Stores outputs in artifacts/

✅ 2. Exploratory Data Analysis (EDA)

Summary statistics

Feature-wise relationships

Correlation heatmap

Outlier detection

Visualizations

✅ 3. Data Transformation Pipeline

Encoding

Scaling

Feature engineering

Saves transformer object for reuse

✅ 4. Automated Model Benchmarking & Selection

The system trains and evaluates multiple algorithms:

CatBoost

Random Forest

Logistic Regression

SVM

KNN

Decision Tree

Naive Bayes

Each model is scored using accuracy, and the algorithm with the highest accuracy is automatically selected.

➡️ CatBoost was selected as the final model due to superior accuracy and low preprocessing requirements.

✅ 5. Reproducible Outputs (Artifacts)

All essential files are stored in:

artifacts/
│── model.pkl
│── preprocessor.pkl
│── train.csv
│── test.csv
|__.gitignore


🧠 How the System Works

1️⃣ Load & clean dataset
2️⃣ Perform EDA
3️⃣ Transform features
4️⃣ Train multiple models
5️⃣ Compare accuracies
6️⃣ Pick the best one (AutoML style)
7️⃣ Save final model + preprocessing pipeline

🛠️ Tech Stack

Python 3.10+

Scikit-Learn

CatBoost

Pandas, NumPy

Matplotlib, Seaborn

Joblib / Pickle

Logging & Exception Handling

🏆 Results

CatBoost achieved the highest classification accuracy

Fully automated ML workflow

Reusable pipeline for any tabular dataset

Clean artifact management for reproducibility

📂 Installation & Setup
1. Clone the Repository
git clone https://github.com/Ashutoshdubey2811/Ecotech.git
cd Ecotech

2. Create Virtual Environment
python -m venv venv
source venv/Scripts/activate   # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the Pipeline
python main.py

📈 Future Enhancements

Add API endpoint (FastAPI/Flask)

Deploy as a web service

Add hyperparameter tuning

Add drift detection

Add UI for EDA and predictions

📜 License

This project is licensed under the MIT License – feel free to use and modify it.

✨ Author

Ashutosh Dubey
Machine Learning & Software Developer
📧itzykhan@gmail.com
