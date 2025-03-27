# Experiment_tracking_mlops
This repo has complete demonstration of performing experiment tracking using MLflow.

```bash
pip install mlflow
```

```bash
mlflow ui (It show the mlflow interface in dafault port 5000)
```

```bash
 mlflow ui --port port_number (to lunch interface on different port)
 ```

```bash
python src/flie1.py (file contain mlflow experiment tracking code)
```


# settting tracking ui on localhost. 
```bash
mlflow.set_tracking_uri('http://localhost:5001')
```

# setting the name of experiment. 
```bash
mlflow.set_experiment("Wine_experiment")
```

# to log metric and parameter 
```bash
mlflow.log_metric("Accuracy", accuracy)
mlflow.log_param("max_depth", max_depth)
mlflow.log_param("n_estimater", n_estimators)
```

## To log artifact
```bash
plt.savefig("confusion-matrix.png")
```

## To log file which contain mlflow experiment 

```bash
mlflow.log_artifact(__file__)
```

## setting the tag (tage means giveing identification to experiment)
```bash
- mlflow.sklearn.log_model(model, "model_name")
```



# Experiment Tracking in remote server using Daghub
- log in to dagshub
- connecting dagshub with github mlops repo. 
- After connecting get tracking uri from dags hub. 
- Finally configure to code to evaluation model part. 

# Auto Logging

```bash
mlflow.autolog()  # It automaticlly log all the metrics, paramter, model, artifact and many more things. 

```

# Hyperparameter Tuneing tracking using mlflow


<img width="1797" alt="Screenshot 2025-03-27 at 9 02 30 PM" src="https://github.com/user-attachments/assets/0f41add7-143e-44ee-8d10-c8ec6f5e0caf" />



