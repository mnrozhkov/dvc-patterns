import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression 

def train_model_LR():
    # Load the prepared data
    data = pd.read_csv('data/features.csv')

    # Extract features and target variable
    X = data.drop('target', axis=1)
    y = data['target']

    # Train the model
    model = LogisticRegression()
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'models/model_LR.pkl')

if __name__ == "__main__":
    train_model_LR()
