import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

housing=fetch_california_housing()

data=pd.DataFrame(housing.data,columns=housing.feature_names)
data["PRICE"]=housing.target

print(data.head())

sns.heatmap(data.corr(),annot=True,cmap="coolwarm")
plt.title("correlation map")
plt.show()

plt.scatter(data["MedInc"],data["PRICE"])
plt.xlabel("median income")
plt.ylabel("average house price")
plt.title("Median income vs house price")
plt.show()

X=data.drop("PRICE",axis=1)
y=data["PRICE"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=LinearRegression()
model.fit(X_train,y_train)

Predictions=model.predict(X_test)

mse=mean_squared_error(y_test,Predictions)
print("mean squared error:",mse)

plt.scatter(y_test, Predictions)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Price")
plt.show()


