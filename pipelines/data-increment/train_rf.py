import pandas as pd
import joblib
import random
from sklearn.ensemble import RandomForestClassifier
import time

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

    # Log the metrics
    with Live(
        dir="reports/train_rf",
        save_dvc_exp=True,
        dvcyaml=False
    ) as live:
        for max_leaf_nodes in [5, 50, 500, 5000]:
            error = random.random()
            live.step = max_leaf_nodes
            live.log_metric("Error", error)
            live.log_metric("Max_Leaf_Nodes", max_leaf_nodes)

    # Log the metrics
    with Live(
        dir="reports/dvclive",
        save_dvc_exp=True,
        dvcyaml=False
    ) as live:
        for max_leaf_nodes in [5, 50, 500, 5000]:
            error = random.random()
            live.log_metric("Error", error)
            live.log_metric("Max_Leaf_Nodes", max_leaf_nodes)
            live.next_step()

    # Save the trained model
    joblib.dump(model, 'models/model_RF.pkl')
    print("Training Random Forest model - COMPLETE")


if __name__ == "__main__":
    train_model_RF()
