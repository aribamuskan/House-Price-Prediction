
# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on property features using **Linear Regression**. The project includes a Streamlit web application where users can enter house details and receive an estimated price.

## 🚀 Live Demo

**Try the application here:**  
[House Price Prediction — Live App](https://house-price-prediction-drsibvqvalx4waqcwzytuw.streamlit.app/)

## 📌 Project Overview

The goal of this project is to learn how to build a complete Machine Learning workflow, from understanding a dataset to training, evaluating, saving, and deploying a model.

## ✨ Features

- Predict house prices using property details.
- Accept area, bedrooms, bathrooms, and house age as inputs.
- Train a Linear Regression model.
- Evaluate predictions using multiple metrics.
- Save the trained model with Joblib.
- Use an interactive Streamlit web interface.
- Access the application through a live URL.

## 📂 Project Structure

```text
House-Price-Prediction/
├── dataset/
│   └── house_data.csv
├── model/
│   └── house_price_prediction.py
├── app.py
├── house_price_model.pkl
├── requirements.txt
└── README.md
```

## 📊 Dataset

The dataset contains **100 house records** with the following columns:

| Feature | Description |
|---|---|
| `area_sqft` | House area in square feet |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `age` | Age of the house in years |
| `price` | House price |

The input features are area, bedrooms, bathrooms, and age. The target variable is `price`.

> **Note:** This is a synthetic dataset created for learning and demonstration. It does not represent actual property market data.

## ⚙️ Machine Learning Workflow

1. **Load the data:** Read the CSV file using Pandas.
2. **Understand the data:** Inspect rows, shape, data types, and summary statistics.
3. **Select features and target:** Separate input features (`X`) from the target (`y`).
4. **Split the data:** Use 80% for training and 20% for testing.
5. **Train the model:** Fit a Linear Regression model using Scikit-learn.
6. **Make predictions:** Predict prices for the test data.
7. **Evaluate the model:** Calculate MAE, MSE, RMSE, and R².
8. **Save the model:** Store the trained model using Joblib.
9. **Build the frontend:** Create an interactive interface with Streamlit.
10. **Deploy the app:** Publish it using Streamlit Community Cloud.

## 🤖 Model and Evaluation

**Algorithm:** Linear Regression

The model was evaluated on the held-out test dataset.

| Evaluation Metric | Result |
|---|---:|
| MAE | 929,226.90 |
| MSE | 1,318,550,653,454.34 |
| RMSE | 1,148,281.61 |
| R² Score | 0.9551 |

The test-set R² score is approximately **0.955**. This means the model explains about 95.5% of the variation in house prices in this test set. It does **not** mean that predictions are 95.5% accurate.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Git and GitHub

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/aribamuskan/House-Price-Prediction.git
```

### 2. Open the project folder

```bash
cd House-Price-Prediction
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
python -m streamlit run app.py
```

## 🧪 Example Prediction

For a house with the following details:

- **Area:** 2,000 sqft
- **Bedrooms:** 4
- **Bathrooms:** 3
- **Age:** 10 years

The model predicts a price of approximately **Rs. 10,926,061** using the current trained model.

## 🔮 Future Improvements

- Train and evaluate the model on a real-world housing dataset.
- Compare Linear Regression with other regression algorithms.
- Improve model performance and test predictions on more data.
- Add input validation and improve the user interface.

## 👩‍💻 Author

**Ariba Muskan**

- GitHub: [aribamuskan](https://github.com/aribamuskan)
- Project Repository: [House Price Prediction](https://github.com/aribamuskan/House-Price-Prediction)
- Live Demo: [Open the App](https://house-price-prediction-drsibvqvalx4waqcwzytuw.streamlit.app/)