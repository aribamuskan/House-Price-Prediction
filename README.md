# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on area, number of bedrooms, number of bathrooms, and house age.

## 🚀 Live Demo

[House Price Prediction App](https://house-price-prediction-drsibvqvalx4waqcwzytuw.streamlit.app/)

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── dataset/
│   └── house_data.csv
│
├── model/
│   └── house_price_prediction.py
│
├── app.py
├── house_price_model.pkl
├── requirements.txt
└── README.md
🧠 Machine Learning Workflow
Loaded the house price dataset using Pandas.
Inspected the dataset using head(), shape, info(), and describe().
Selected the input features:
Area
Bedrooms
Bathrooms
House Age
Selected price as the target variable.
Split the dataset into 80% training and 20% testing data.
Trained a Linear Regression model.
Generated predictions on the test data.
Evaluated the model using MAE, MSE, RMSE, and R² Score.
Saved the trained model using Joblib.
Built a Streamlit frontend for making new predictions.
Deployed the application using Streamlit Community Cloud.
📊 Dataset

The dataset contains 100 house records with the following columns:

Feature	Description
area_sqft	House area in square feet
bedrooms	Number of bedrooms
bathrooms	Number of bathrooms
age	Age of the house
price	House price
🤖 Model

Algorithm: Linear Regression

Model Evaluation
Metric	Result
MAE	929,226.90
MSE	1,318,550,653,454.34
RMSE	1,148,281.61
R² Score	0.9551

The R² score on the test set was approximately 0.955, meaning the model explained about 95.5% of the variation in the test-set target values.

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
Git & GitHub
💻 Run Locally

Clone the repository:

git clone https://github.com/aribamuskan/House-Price-Prediction.git

Go into the project folder:

cd House-Price-Prediction

Install dependencies:

python -m pip install -r requirements.txt

Run the Streamlit app:

python -m streamlit run app.py
🎯 Example Prediction

For a house with:

Area: 2000 sqft
Bedrooms: 4
Bathrooms: 3
Age: 10 years

The model predicts approximately:

Rs. 10,926,061

⚠️ Note

This project uses a small synthetic dataset created for Machine Learning practice and demonstration. The model should not be considered a real-world house valuation system.

👩‍💻 Project Links

GitHub:
https://github.com/aribamuskan/House-Price-Prediction

Live Demo:
https://house-price-prediction-drsibvqvalx4waqcwzytuw.streamlit.app/