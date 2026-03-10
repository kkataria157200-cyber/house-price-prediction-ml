# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project implements a **Machine Learning model to predict house prices** using the **California Housing Dataset**.
The goal is to build a regression model that learns relationships between housing features such as income, population, and geographic location, and then predicts the average house price.

The project demonstrates the **complete machine learning workflow**, including data exploration, visualization, model training, and evaluation.

---

## 📊 Dataset

The dataset used in this project is the **California Housing Dataset**, which is available through Scikit-Learn.

It contains information collected from the **1990 California census** and includes various demographic and geographic features.

### Features in the Dataset

| Feature    | Description                                    |
| ---------- | ---------------------------------------------- |
| MedInc     | Median income of households in the block group |
| HouseAge   | Median age of houses in the block              |
| AveRooms   | Average number of rooms per household          |
| AveBedrms  | Average number of bedrooms per household       |
| Population | Total population in the block                  |
| AveOccup   | Average number of occupants per household      |
| Latitude   | Latitude of the block                          |
| Longitude  | Longitude of the block                         |
| PRICE      | Median house value (target variable)           |

---

## ⚙️ Technologies and Libraries Used

The project uses the following Python libraries:

* **NumPy** – Numerical computing
* **Pandas** – Data manipulation and analysis
* **Matplotlib** – Data visualization
* **Seaborn** – Statistical data visualization
* **Scikit-Learn** – Machine learning models and utilities

---

## 🔬 Machine Learning Workflow

The project follows the standard machine learning pipeline:

### 1️⃣ Data Loading

The California housing dataset is loaded using Scikit-Learn.

### 2️⃣ Data Exploration

The dataset is converted into a Pandas DataFrame to allow easier analysis and manipulation.

The first few rows of the dataset are displayed to understand the structure of the data.

### 3️⃣ Data Visualization

Two visualizations are created:

**Correlation Heatmap**

This heatmap shows relationships between different features in the dataset.

**Scatter Plot**

A scatter plot is used to visualize the relationship between:

* Median income (`MedInc`)
* House price (`PRICE`)

This helps identify whether income influences housing prices.

---

### 4️⃣ Feature Selection

The dataset is divided into:

**Features (X)**
All columns except the target variable.

**Target Variable (y)**
The column representing the house price.

---

### 5️⃣ Train-Test Split

The dataset is divided into training and testing sets:

* **80% Training Data**
* **20% Testing Data**

This ensures that the model is evaluated on unseen data.

---

### 6️⃣ Model Training

A **Linear Regression model** from Scikit-Learn is used to train the model.

Linear regression attempts to find the best linear relationship between input features and the target variable.

---

### 7️⃣ Model Prediction

After training the model, predictions are generated using the testing dataset.

---

### 8️⃣ Model Evaluation

The model performance is evaluated using **Mean Squared Error (MSE)**.

Mean Squared Error measures the average squared difference between:

* Actual house prices
* Predicted house prices

Lower MSE values indicate better model performance.

---

### 9️⃣ Model Visualization

A scatter plot of **Actual vs Predicted house prices** is created.

This plot helps visually inspect how well the model predicts housing prices.

If the predictions are accurate, the points should lie close to a straight diagonal line.

---

## 📂 Project Structure

```
house-price-prediction-ml
│
├── house_price_prediction.py
├── requirements.txt
└── README.md
```

### File Descriptions

**house_price_prediction.py**
Contains the complete machine learning pipeline including data loading, visualization, training, prediction, and evaluation.

**requirements.txt**
Lists the Python libraries required to run the project.

**README.md**
Documentation explaining the project.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-prediction-ml.git
```

### Step 2: Navigate to the Project Folder

```bash
cd house-price-prediction-ml
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Python Script

```bash
python house_price_prediction.py
```

---

## 📈 Example Outputs

The project generates several visual outputs:

* Correlation heatmap
* Median income vs house price scatter plot
* Actual vs predicted price comparison plot

These visualizations help understand the dataset and model performance.

---

## 🚀 Future Improvements

Possible improvements to this project include:

* Implementing **Random Forest Regression**
* Using **Gradient Boosting models**
* Adding **cross-validation**
* Performing **feature engineering**
* Comparing multiple regression algorithms
* Deploying the model using **Flask or FastAPI**

---

## 🎯 Learning Outcomes

This project helps understand:

* Machine learning regression workflows
* Data visualization techniques
* Model training and evaluation
* Feature relationships in datasets
* Practical usage of Scikit-Learn

---

## 👩‍💻 Author

**Khushi Kataria**

This project is part of my learning journey in **Machine Learning and Artificial Intelligence**.
# house-price-prediction-ml
House price prediction using Linear Regression and the California Housing dataset
