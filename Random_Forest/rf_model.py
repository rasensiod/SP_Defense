import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split,StratifiedKFold,GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier,VotingClassifier
from Module.results_visualization import *


class random_forest:
    def __init__(self):
        print("===== Construct rf model  =====")
        self.model = RandomForestClassifier()

    def train(self, train_X, train_y):
        print("===== Training rf model =====")
        self.model.fit(train_X, train_y)



    def test(self, test_X,test_y, confusion_mat=False):
        print("===== Test rf model on test set=====")
        pred_y = self.model.predict(test_X)
        test_y = np.argmax(test_y, axis=1)
        test_accuracy = accuracy_score(test_y,pred_y)
        if confusion_mat:
            plot_confusion_matrix(test_y,pred_y)
        return test_accuracy