"""Base_CNN contains the content about model construction, training and testing.

"""

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import numpy as np
np.random.seed(2)
from sklearn.metrics import f1_score
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.optimizers import Adam
from keras.callbacks import ReduceLROnPlateau
from sklearn.metrics import accuracy_score
from Module.results_visualization import plot_confusion_matrix, plot_history




class Base_NN:
    """
     Define class of Base_NN and compile

    """
    def __init__(self):
        print("===== Construct Base_NN model =====")
        self.model = Sequential([
            Dense(128, input_shape=(69,), activation='relu'),
            Dense(256, activation="relu"),
            Dense(512, activation="relu"),
            Dropout(0.3),
            Dense(14, activation='softmax')
        ])
        print("Summary of the Base_NN model")
        self.model.summary()
        optimizer = Adam(lr=0.001)
        self.model.compile(optimizer = optimizer, loss="categorical_crossentropy", metrics=["accuracy"])


    def load_weights(self, path):
        self.model.load_weights(path)

    def train(self, train_X, train_y, valid_x, valid_y, path, epochs= 50, plot= True):
        """
        training model and plot the learning curves
        Args:
            train_batch: training set
            valid_batch: validation set
            path: path to save the learning curves
        Returns:
            result of training process contains accuracy and loss
        """
        print("===== Training Base_NN model =====")
        learning_rate_reduction = ReduceLROnPlateau(monitor="val_loss",
                                                     patience=3,
                                                     verbose=1,
                                                     factor=0.5,
                                                     min_lr=0.00001)
        history = self.model.fit(train_X, train_y, batch_size=1024, epochs=epochs,
                            validation_data=(valid_x, valid_y), verbose=1, callbacks=[learning_rate_reduction])
        if plot:
            plot_history(history, path)
        return history

    def train_weighted(self, train_X, train_y, valid_x, valid_y, class_weights, path, epochs= 50, plot= True):
        """
        training model and plot the learning curves
        Args:
            train_batch: training set
            valid_batch: validation set
            path: path to save the learning curves
        Returns:
            result of training process contains accuracy and loss
        """
        print("===== Training Base_NN model =====")
        learning_rate_reduction = ReduceLROnPlateau(monitor="val_loss",
                                                     patience=3,
                                                     verbose=1,
                                                     factor=0.5,
                                                     min_lr=0.00001)
        history = self.model.fit(train_X, train_y, batch_size=1024, epochs=epochs,
                            validation_data=(valid_x, valid_y), verbose=1, callbacks=[learning_rate_reduction],
                                 class_weight=class_weights)
        if plot:
            plot_history(history, path)
        return history


    def test(self, test_X, test_y, confusion_mat=False):
        """
        verify the model on test set
        Args:
            test_batch: test data set
        Returns:
            accuracy score
        """
        print("===== Test Base_NN model on test set=====")
        Y_pred = self.model.predict(test_X, verbose=1)
        # Convert predictions classes to one hot vectors
        Y_pred_classes = np.argmax(Y_pred, axis=1)
        # Convert validation observations to one hot vectors
        Y_true = np.argmax(test_y, axis=1)
        score = accuracy_score(Y_true, Y_pred_classes)
        print(score)
        if confusion_mat:
            plot_confusion_matrix(Y_true,Y_pred_classes)
        return score

    def test_demo(self, test_X):
        """
         simultae the attack for notification
         Args:
             test_batch: test data set
         Returns:
             label of prediction
         """
        Y_pred = self.model.predict(test_X, verbose=1)
        # Convert predictions classes to one hot vectors
        Y_pred_classes = np.argmax(Y_pred, axis=1)
        return Y_pred_classes