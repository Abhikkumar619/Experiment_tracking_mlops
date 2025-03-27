# Experiment_tracking_mlops
This repo has complete demonstration of performing experiment tracking using MLflow.


## pip install mlflow

## mlflow ui (It show the mlflow interface in dafault port 5000)

## mlflow ui --port port_number (to lunch interface on different port)

## python src/flie1.py (file contain mlflow experiment tracking code)


# settting tracking ui on localhost. 
- mlflow.set_tracking_uri('http://localhost:5001')

# setting the name of experiment. 
- mlflow.set_experiment("Wine_experiment")

# to log metric and parameter 
- mlflow.log_metric("Accuracy", accuracy)
- mlflow.log_param("max_depth", max_depth)
- mlflow.log_param("n_estimater", n_estimators)

## To log artifact
- plt.savefig("confusion-matrix.png")

## To log file which contain mlflow experiment 

-  mlflow.log_artifact(__file__)

## setting the tag (tage means giveing identification to experiment)
- mlflow.sklearn.log_model(model, "model_name")



