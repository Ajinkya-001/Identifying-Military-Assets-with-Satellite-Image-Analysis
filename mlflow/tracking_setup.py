import mlflow

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("military-infra-detection")
    print("✅ MLflow tracking set up")
