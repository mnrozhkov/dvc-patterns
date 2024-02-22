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

    # Log the metrics 
    errors = []
    max_leaf_nodes = [5, 50, 500, 5000]
     
    for nodes in max_leaf_nodes:
        error = random.random()
        errors.append(error)
        print(f"Max leaf nodes: {nodes}  \t ➡ Mean Absolute Error:  {error}")
    
    # Create a DataFrame from the lists
    datapoints = pd.DataFrame({
        'Max Leaf Nodes': max_leaf_nodes,
        'Error': errors
    })

    with Live(
        dir="reports/train_lr",
        save_dvc_exp=True,
        dvcyaml=False
    ) as live:
        live.log_plot(
            "errors_vs_leafs",
            datapoints,
            x="Max Leaf Nodes",
            y="Error",
            template="simple",
            title="Errors vs Max Leaf Nodes")

    # Save the trained model
    joblib.dump(model, 'models/model_LR.pkl')
    print("Training Logistic Regression model - COMPLETE")

if __name__ == "__main__":
    train_model_LR()
