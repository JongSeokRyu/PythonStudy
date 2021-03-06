# ID: 2021220942
# NAME: 류종석
# File name: hw02-5.py
# Platform: Python 3.9.0 on Window 10 (PyCharm)
# Required Package(s): numpy, pandas, matplotlib, sklearn

"""Iris Perceptron

Automatically generated by Colaboratory.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score


class Perceptron:
    """
    Perceptron neuron
    """

    def __init__(self, learning_rate=0.1):
        """
        instantiate a new Perceptron

        :param learning_rate: coefficient used to tune the model
        response to training data
        """
        self.learning_rate = learning_rate
        self._b = 0.0  # y-intercept
        self._w = None  # weights assigned to input features
        # count of errors during each iteration
        self.misclassified_samples = []

    def fit(self, x: np.array, y: np.array, n_iter=10):
        """
        fit the Perceptron model on the training data

        :param x: samples to fit the model on
        :param y: labels of the training samples
        :param n_iter: number of training iterations
        """
        self._b = 0.0
        self._w = np.zeros(x.shape[1])
        self.misclassified_samples = []

        for _ in range(n_iter):
            # counter of the errors during this training iteration
            errors = 0
            for xi, yi in zip(x, y):
                # for each sample compute the update value
                update = self.learning_rate * (yi - self.predict(xi))
                # and apply it to the y-intercept and weights array
                self._b += update
                self._w += update * xi
                errors += int(update != 0.0)

            self.misclassified_samples.append(errors)

    def f(self, x: np.array) -> float:
        """
        compute the output of the neuron
        :param x: input features
        :return: the output of the neuron
        """
        return np.dot(x, self._w) + self._b

    def predict(self, x: np.array):
        """
        convert the output of the neuron to a binary output
        :param x: input features
        :return: 1 if the output for the sample is positive (or zero),
        -1 otherwise
        """
        return np.where(self.f(x) >= 0, 1, -1)

# download and convert the csv into a DataFrame
df = pd.read_csv('wine.csv', header=None)

# 첫째 행 삭제
df.drop(df.index[0],inplace=True)
# print(df)

# extract the label column
# 0열 클래스 번호 추출
y = df.iloc[:, 0].values
#print(y)

# extract features
# 1열 부터 데이터 추출
x = df.iloc[:, 1:].values
#print(x)


# 클래스 1, 2 데이터만 가져와서 배열 재조합
x1 = np.array(x[59:130])    # class 2 데이터
x2 = np.array(x[130:])      # class 3 데이터
x = np.concatenate((x1,x2))
x = np.float64(x)

#클래스 1, 2 데이터만 가져와서 배열 재조합
y1 = np.array(y[59:130])    # class 2
y2 = np.array(y[130:])      # class 3 데이터
y = np.concatenate((y1,y2))
y = np.where(y == '2', 1, -1)
y = np.float64(y)

from sklearn.model_selection import train_test_split

# standardization of the features
# 데이터프레임 열개수 -1 만큼 반복 (데이터 열만 정규화)
for i in range(0, df.shape[1]-1):
    x[:, i] = (x[:, i] - x[:, i].mean()) / x[:, i].std()


# split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

# train the model
classifier = Perceptron(learning_rate=0.01)
classifier.fit(x_train, y_train)
print(classifier.misclassified_samples)
print("accuracy %f" % accuracy_score(classifier.predict(x_test), y_test))

# plot the number of errors during each iteration
plt.plot(range(1, len(classifier.misclassified_samples) + 1), classifier.misclassified_samples, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Errors')
plt.show()

