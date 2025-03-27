import mlflow
import mlflow.sklearn
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load Wine dataset
wine = load_wine()
X = wine.data
y = wine.target

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)

# Define the params for RF model
max_depth = 5
n_estimators = 8
mlflow.set_tracking_uri('http://localhost:5001')


# Auto log Automatically log accuracy, model , parameter, metrics and many more things. 
mlflow.autolog()

mlflow.set_experiment("Wine_experiment")


with mlflow.start_run(): 
    rf=RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)
    rf.fit(X_train, y_train)
    

    y_pred=rf.predict(X_test)

    accuracy=accuracy_score(y_test, y_pred)


    # creating a confusion matrix.
    cm=confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,6))
    sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.ylabel('Acutal')
    plt.xlabel('predicated')
    plt.title("confusion matrix")

    # save plot of confusion matrix
    plt.savefig("confusion-matrix.png")

    # logging saved plot in mlflow as artifact.

     
    mlflow.log_artifact(__file__)

    # Setting the tag

    # setting the model



    print(accuracy)

