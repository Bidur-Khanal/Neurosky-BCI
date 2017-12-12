import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
from scipy.fftpack import fft, ifft, fftfreq
from sklearn import preprocessing
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import math
from itertools import tee
from sklearn import datasets, linear_model,tree,svm
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
    
    
style.use('classic')
import pywt
from pylab import *
import scipy.io
import scipy.signal
import scipy.fftpack
from scipy.signal import butter, lfilter
from numpy import *
from scipy.signal import *
from numpy.fft import *
from matplotlib import *
from scipy import signal
from pylab import *



#To run this import this module and create a class " ml=learning()"

class machinelearning:
    def __init__(self):
     fig = plt.figure()

     fig.canvas.set_window_title( "Plot Figures" )
     df = []
     ax1=fig.add_subplot(1,1,1)

     # function to generate PSD
     def PSD():

      #jati ota csv file cha tesko df[] ma append garna
      df.append(pd.read_csv("drowsy_satish.csv"))
      df.append(pd.read_csv("drowsy_satish2.csv"))
      #df.append(pd.read_csv("attention_satish3.csv"))


      # used to make a csv file with columns ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma', 'Attention']
      # put machinelearning0.csv for drowsy, machinelearning1.csv for attention and machinelearning2.csv for normal
      with open('machinelearning0.csv', 'w', newline='') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow(['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma', 'Attention'])

      #to go through all df[] list
       for i in range(len(df)):
        rawdata=df[i]['raw']
        windowed=[]

        window = np.hamming(1000)# to generate a hamming window for 1000 data samples

        # to generate sliding window of size Windowsize and how much step to slide "stepSize"
        def sliding_window(data, stepSize, windowSize):
         # slide a window across the data
         for y in range(0, data.shape[0], stepSize):
           # yield the current window
           if(len((data[y:y + windowSize]))==windowSize):
            yield (data[y:y + windowSize])





        def butter_bandpass(lowcut, highcut, fs, order=6):
         nyq = 0.5 * fs
         low = lowcut / nyq
         high = highcut / nyq
         b, a = butter(order, [low, high], btype='band')
         return b, a

        def butter_bandpass_filter(data, lowcut, highcut, fs, order=6):
         b, a = butter_bandpass(lowcut, highcut, fs, order=order)
         y = lfilter(b, a, data)
         return y




        band= butter_bandpass_filter(rawdata,0.5,60,512,4)


        #to store the window of 1000 sample each in a list
        for value in sliding_window(band,100,1000):
          windowed.append(value*window)


        # To get a single PSD of the signal from 1000 sample data each
        fs=512
        for i in range(len(windowed)):
          f5, Pxx_den5 = signal.periodogram(windowed[i], fs)
          normalized5 = (Pxx_den5 - np.min(Pxx_den5)) / (np.max(Pxx_den5) - np.min(Pxx_den5))
          i1= np.where(np.logical_and(f5>=0.5, f5<4))
          i2 = np.where(np.logical_and(f5 >= 4, f5 <7))
          i3 = np.where(np.logical_and(f5 >= 7, f5 < 12))
          i4 = np.where(np.logical_and(f5 >= 12, f5 < 30))
          i5 = np.where(np.logical_and(f5 >= 30, f5 <= 80))
          sum1=np.sum(normalized5[i1])
          sum2 = np.sum(normalized5[i2])
          sum3 = np.sum(normalized5[i3])
          sum4 = np.sum(normalized5[i4])
          sum5 = np.sum(normalized5[i5])
          writer.writerow([sum1,sum2,sum3,sum4,sum5,0]) # stores the value in machinelearning0.csv with columns ['Delta', 'Theta', 'Alpha', 'Beta', 'Gamma', 'Attention']. Put last value  0 for drowsy, 1 for attention and 2 for normal



          # Plot garna ho you don't require to run
          '''ax1.plot(f5, Pxx_den5)
          ax1.set_title("PSD ")
          ax1.set_ylabel('normalized PSD')
          ax1.set_xlabel('frequency')'''

     def learning():

      # if you wish to train with new datasets

      '''table1 = pd.read_csv('machinelearning0.csv')
      table2 = pd.read_csv('machinelearning1.csv')
      table3 = pd.read_csv('machinelearning2.csv')
      table4 = pd.read_csv('machinelearning.csv')
      table = pd.concat([table1, table2, table3])
      X_train = np.array(table.drop(['Attention'], 1))
      Y_train = np.array(table['Attention'])
      X_test = np.array(table1.drop(['Attention'], 1))
      Y_test = np.array(table1['Attention'])

      classifier = svm.SVC(C=100,gamma=1000)

           # Train the model using the training sets
           classifier.fit(X_train,Y_train)
           joblib.dump(classifier, 'model.pkl')# saves the trained model in pkl file'''

      # data has to be provided to the classifier in this manner. Each represents power of delta, theta, alpha, beta and gamma. This can be generated using the above PSD function
      m = np.array([2.74434841178, 1.86825117793, 1.08641894702, 0.802395862058, 0.108030521526])


      #To predict the value:

      # Predictions
      clf = joblib.load('model.pkl') #loads the already trained model "model.pkl"

      Predictions = clf.predict(m)# predicts and return either 0,1,2 for drowsy, attention and normal respectively. Use this to control the speed
      print(Predictions)
      #print(accuracy_score(Y_test, Predictions)) #to predict the modal accuracy with a new dataset CSV
     plt.show()

