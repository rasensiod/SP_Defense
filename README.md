# SP_Defense


## Intro
The objective of this project is to create a simple smart hospital website and database with patient data to attack it
using both DDoS and SQL injections. Then, in order to protect the confidentiality and accessibility of the data, we create a set of measures such as identifying different attacks by using machine learning techniques and publishing notification by AWS SNS.



The final accuracy results is shown in the following table:
|  | DDoS attack | SQL injection | 
| :----:| :----:| :----: |
| NN | 90% | / | 
| NN(weight) | 87% | / |
| Random Forest | 86% | / |
| SVM | / | 99.3% |


## Role of each file
The current project structure is shown below
```
.
├── DDoS
│   ├── Dataset
│   │   └── df_sample.csv
│   ├── Model
│   │   └── NN_large.h5
│   ├── Module
│   │   ├── __pycache__
│   │   ├── data_exploration.py
│   │   ├── data_preprocessing.py
│   │   ├── notification_sns.py
│   │   └── results_visualization.py
│   ├── Neural_Network
│   │   ├── Base_model.py
│   │   └── __pycache__
│   ├── Random_Forest
│   │   ├── __pycache__
│   │   └── rf_model.py
│   ├── Results_img
│   │   ├── bar_backward_packets.png
│   │   ├── base_nn_curves.png
│   │   ├── base_nn_matrix.png
│   │   ├── base_nn_weighted_curves.png
│   │   ├── base_nn_weighted_matrix.png
│   │   ├── heatmap_features.png
│   │   ├── histogram_label.png
│   │   ├── notification_mail.jpeg
│   │   ├── notification_message.jpeg
│   │   ├── pie_gragh_label.png
│   │   ├── rf_matrix.png
│   │   └── stem_fwd_packets.png
│   ├── main.py
│   └── test.py
├── Datasets
│   └── Modified_SQL_Dataset.csv
├── README.md
├── model_training.ipynb
├── sqli_train.py
└── web_app
    ├── db.sqlite3
    ├── db_patients.json
    ├── hospital
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── sqli_alert
    │   ├── sqli_ml
    │   ├── static
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    └── web_app
        ├── __init__.py
        ├── __pycache__
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

**DDoS**: Contains all the process to do data preprocessing, data exploration, model training, model evulation, and notification module on DDoS attack.  

**sql_train**: Contains the process of traning the svm model on sql injection dataset. 

**web_app**: Contains all the process to build a website. 



## How to start
If all the dependencies required for the current project are already installed, you can run manage.py to start a local website.  
```
python ./web_app/manage.py runserver
```
You can also change the security level in views.py to adjust defense level on SQL injection
In terms of DDoS attack model training, you could run the main.py to automatically do data preprocessing and model training.
```
python ./DDoS/main.py
```
You can also run the test.py to veirfy the performance of the model about identifying DDoS attack and it will trigger notification service automatically.
```
python ./DDoS/test.py
```

Due to the monthly limitation of Git LFS uploading large files, it is not possible to upload the dataset to github, so you need to copy the datasets to the Datasets directory. 


