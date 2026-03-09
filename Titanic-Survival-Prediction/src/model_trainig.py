import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, "..", "data", "titanic.csv")
df = pd.read_csv(data_path)
print(df.head())

# Data Cleaning
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Drop unnecessary columns
df.drop(["Cabin", "Ticket", "Name", "PassengerId"], axis=1, inplace=True)

# Convert categorical variables
df = pd.get_dummies(df, columns=["Sex","Embarked"], drop_first=True)

# Features and target
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
print(classification_report(y_test, predictions))


# Create models folder if it doesn't exist
model_dir = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(model_dir, exist_ok=True)

# Save model
model_path = os.path.join(model_dir, "model.pkl")
joblib.dump(model, model_path)

print("Model saved at:", model_path)