from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.decomposition import PCA
import pylab as pl
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import math
from sklearn import preprocessing
from sklearn import datasets, linear_model,tree,svm
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from mlxtend.plotting import plot_decision_regions
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets


class learning():
 def __init__(self):

     table1=pd.read_csv('machinelearning0.csv')
     table2=pd.read_csv('machinelearning1.csv')
     table3=pd.read_csv('machinelearning2.csv')
     table4 = pd.read_csv('machinelearning.csv')
     table=pd.concat([table1,table2,table3])
     print(table)
     X_train=np.array(table.drop(['Attention'], 1))
     Y_train=np.array(table['Attention'])

     #print(X_train)
    # X_train, X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5)
     X_test=np.array(table1.drop(['Attention'], 1))
     Y_test = np.array(table1['Attention'])


     '''X_test=np.array(table1.drop(['meditation','attention','poorSignalLevel],1))
     Y_test = np.array(table1['attention'])
     X_train=X_train/10000
     X_test = X_test / 10000'''

     '''X_train= preprocessing.scale(X_train)
     X_test = preprocessing.scale(X_test)
     Y_train = preprocessing.scale(Y_train)
     Y_test = preprocessing.scale(Y_test)'''

     pca = PCA(n_components=2).fit(X_train)
     pca_2d = pca.transform(X_train)
     print(pca_2d)

     X, y = datasets.make_blobs(n_samples=600, n_features=3,
                                centers=[[2, 2, -2], [-2, -2, 2]],
                                cluster_std=[2, 2], random_state=2)
     #print(X)
     #print(y)
     k = svm.SVC(C=10,gamma=500)
     k.fit(pca_2d,Y_train)
     m=np.array([2.74434841178,1.86825117793,1.08641894702,0.802395862058,0.108030521526])
     # Your classifier model
     #regr = linear_model.LinearRegression()
     '''classifier = svm.SVC(C=100,gamma=1000)

     # Train the model using the training sets
     classifier.fit(X_train,Y_train)
     joblib.dump(classifier, 'model.pkl')'''




     # Update plot object with X/Y axis labels and Figure Title
     '''plt.xlabel(X.columns[0], size=14)
     plt.ylabel(X.columns[1], size=14)
     plt.title('SVM Decision Region Boundary', size=16)'''




     '''# for linear regression
     # The coefficients
     print('Coefficients: \n', regr.coef_)
     # The mean squared error
     print("Mean squared error: %.2f"
           % np.mean((regr.predict(X_test) - Y_test) ** 2))
     # Explained variance score: 1 is perfect prediction
     print('Variance score: %.2f' % regr.score(X_test, Y_test))'''

     #Predictions
     pca_2d_X_test = pca.transform(X_test)
     #clf = joblib.load('model.pkl')
     Predictions= k.predict(pca_2d_X_test)
     #print(Predictions)
     print( accuracy_score(Y_test,Predictions))
    # plt.scatter(X_train[0:],X_train[1:], alpha=0.5)

     plot_decision_regions(X=pca_2d,
                           y=Y_train,
                           clf=k)


     # Plot outputs


     plt.show()