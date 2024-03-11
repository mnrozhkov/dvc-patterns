import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import time

from pathlib import Path
from dvclive import Live

def train_model_RF():

    print("Training Random Forest model - START")
    

    # Load the prepared data
    data = pd.read_csv('data/features.csv')

    # Extract features and target variable
    X = data.drop('target', axis=1)
    y = data['target']

    # Train the model
    model = RandomForestClassifier() # Example model
    model.fit(X, y)

    # Save the trained model
    MODEL_PATH = "models/model_RF_new.pkl"
    joblib.dump(model, MODEL_PATH)


    with Live() as live:
        live.log_artifact(
            path=MODEL_PATH,
            type="model",
            name="model_RF",
            labels=["rf"],
        )

    time.sleep(2)
    print("Training Random Forest model - COMPLETE")

if __name__ == "__main__":
    train_model_RF()
