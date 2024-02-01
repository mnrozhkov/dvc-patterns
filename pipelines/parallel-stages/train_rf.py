import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import time

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
    joblib.dump(model, 'models/model_RF.pkl')

    time.sleep(20)
    print("Training Random Forest model - COMPLETE")

if __name__ == "__main__":
    train_model_RF()
