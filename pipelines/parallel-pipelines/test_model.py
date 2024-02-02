import argparse
import joblib
import pandas as pd
import json
from sklearn.metrics import accuracy_score # Example metric

def test_model(model_path, model_name):
    # Load the model from the provided path
    model = joblib.load(model_path)

    # Load evaluation data
    eval_data = pd.read_csv('data/features.csv')
    X_eval = eval_data.drop('target', axis=1)
    y_eval = eval_data['target']

    # Evaluate the model
    predictions = model.predict(X_eval)
    
    accuracy = accuracy_score(y_eval, predictions)

    # Print or save the metric
    print(f"Accuracy of {model_name}: {accuracy}")

    # Save metrics to a file
    metrics_report_path = f'reports/{model_name}_metrics_report.json'
    metrics = {
        'accuracy': accuracy
    }
    with open(metrics_report_path, 'w') as f:
        json.dump(metrics, f)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Test a machine learning model and report accuracy.')
    parser.add_argument('--model_path', type=str, help='Path to the machine learning model file.')
    parser.add_argument('--model_name', type=str, help='Name of the model for reporting purposes.')
    
    args = parser.parse_args()

    test_model(args.model_path, args.model_name)
