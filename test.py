import mlflow
mlflow.set_tracking_uri('http://localhost:5001')
print(mlflow.get_tracking_uri())
