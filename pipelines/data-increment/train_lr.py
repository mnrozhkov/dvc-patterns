import pandas as pd
import joblib
import random
from sklearn.linear_model import LogisticRegression 
import time

from dvclive import Live
from dvc.api import params_show


def train_model_LR():

    print("Training Logistic Regression model - START")
    time.sleep(3)

    # Load the prepared data
    data = pd.read_csv('data/features.csv')

    # Extract features and target variable
    X = data.drop('target', axis=1)
    y = data['target']

    # Train the model
    model = LogisticRegression()
    model.fit(X, y)

    with Live(save_dvc_exp=True) as live:
        time.sleep(3)
        epochs = 10
        
        for i in range(10):
            print(f"training on epoch: {i}")
            live.log_metric("accuracy", i + random.random())
            live.log_metric("f1", epochs - (i + random.random()))
            live.next_step()

            time.sleep(epochs)

    # Save the trained model
    joblib.dump(model, 'models/model_LR.pkl')

    print("Training Logistic Regression model - COMPLETE")

if __name__ == "__main__":
    train_model_LR()
