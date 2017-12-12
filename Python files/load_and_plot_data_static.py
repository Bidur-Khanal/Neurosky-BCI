import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import math
style.use('seaborn-deep')




class load_plot:
 def __init__(self):
  fig = plt.figure()
  ax1 = fig.add_subplot(2, 2, 1)
  ax2 = fig.add_subplot(2, 2, 2)
  ax3 = fig.add_subplot(2, 2, 3)
  ax4 = fig.add_subplot(2, 2, 4)

  #x=[]
  #x = np.array(np.loadtxt('EEG_database_Satish_baseline.csv',dtype=float,delimiter=',',skiprows=1, unpack=True))
  data=[]
  data.append(pd.read_csv('EEG_database_Satish_baseline.csv'))
  data.append(pd.read_csv('EEG_database_Pankaj_baseline.csv'))
  data.append(pd.read_csv('EEG_database_reading.csv'))
  data.append(pd.read_csv('EEG_poorsignal.csv'))
  #print(data)
  #z=x.transpose()
  #=np.log10(x)
  #data=np.log10(data)
  data[0]=np.log10(data[0])
  data[1]=np.log10(data[1])
  data[2] = np.log10(data[2])
  data[3] = np.log10(data[3])
  for i in range(4):
   Alphamean= (data[i]['lowAlpha']+data[i]['highAlpha'])/2
   Betamean = (data[i]['lowBeta'] + data[i]['highBeta']) / 2
   data[i]['checkattention']=(Betamean/Alphamean)
  #result = pd.concat(data, keys=['x', 'y'])
  #ax1.plot(result.ix['x']['lowAlpha'])
  ax1.plot(data[0]['lowAlpha'])
  ax2.plot(data[1]['lowAlpha'])
  ax3.plot(data[2]['lowAlpha'])
  ax4.plot(data[3]['lowAlpha'])





  #y= np.loadtxt('EEG_database_Pankaj_baseline.csv',dtype=float,delimiter=',',skiprows=1, unpack=True)


  bins = [0, 10, 20,30,40,50,60,70,80,90,100]

  #sns.boxplot(data=[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9]], orient="v")
  #sns.boxplot(data=data[0], orient="v")
  #sns.boxplot(data=data[0],orient="v")




  #sns.boxplot(data=[y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9]], orient="v")

  #sns.swarmplot(data=x)

  '''with open('EEG_database.csv','r') as csvfile:
      plots = csv.reader(csvfile, delimiter=',')
      for row in plots:
          items = zip(csvfile, row)
          x = []
          y=[]
          # Add the value to our dictionary
          for (lowAlpha, value) in items:
              x[lowAlpha] = int(value.strip())
          for (highAlpha, value) in items:
              y[highAlpha]= int(value.strip())

  plt.plot(x,y, label='Loaded from file!')'''

  plt.xlabel('EEG Parameters')
  plt.ylabel('Log values')
  plt.title('Comparison Between Two Sets')
  #plt.legend()
  plt.show()
