import matplotlib.pyplot as plt
from matplotlib import style
from neuroskymain import *
from collect_data import *
import time
import matplotlib.animation as animation
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import math
style.use('seaborn-whitegrid')


class plot_dynamic:
 def __init__(self):

  fig = plt.figure()
  ax1 = fig.add_subplot(2, 2, 1)
  ax2 = fig.add_subplot(2, 2, 2)
  ax3 = fig.add_subplot(2, 2, 3)
  ax4 = fig.add_subplot(2, 2, 4)
  ax1.set_title("lowAlpha")
  ax2.set_title("lowBeta")
  ax3.set_title("meditation")
  ax4.set_title("attention")

  # immediately extract data for live plotting

  record_from_brain = Brain()
  while not record_from_brain.isConnected():
      print('brain not yet connected, trying again in 5 seconds')
      time.sleep(5)
  print("brain now connected presumably, lets get some data")
  print("sleep for 3 seconds then check again")
  time.sleep(3)

  data = pd.DataFrame(columns=record_from_brain.justheaders())
  #print(data)
  #data = pd.DataFrame()




  #function to extract and plot data once every 2 seconds
  def live(i):

   #data=pd.read_csv('EEG_normal.csv')

   #temp = record_from_brain.fullstr()
   #print(temp)
   #data.append(temp)
   #data1 =pd.DataFrame()

   data1=np.array(record_from_brain.fullstr())
   data1=np.log10(data1)


   #ndlist = list(data1)
   #data.append(data1)
   #data1.tolist()
   #print(data1)
   #data.append(ndlist, ignore_index=True)
   #print(data)
   data.loc[i] = data1
   # data=np.log10(data)

   #for i in range(11):
    #data.loc[i] = data1[i]
    #print(data1[i])

   #data['lowAlpha', 'highAlpha', 'lowBeta', 'highBeta','lowGamma', 'highGamma', 'delta', 'theta','poorSignalLevel','meditation', 'attention']=[data1[0],data1[1],data1[2],data1[3],data1[4],data1[5],data1[6],data1[7],data1[8],data1[9],data1[10]]

   #data.loc= [list(record_from_brain.fullstr())]

   #print(data1)
   #time.sleep(2)





   #x=[]
   #x = np.array(np.loadtxt('EEG_database_Satish_baseline.csv',dtype=float,delimiter=',',skiprows=1, unpack=True))
   '''data=[]
   data.append(pd.read_csv('EEG_database_Satish_baseline.csv'))
   data.append(pd.read_csv('EEG_database_Pankaj_baseline.csv'))
   data.append(pd.read_csv('EEG_database_Pranjal_class.csv'))
   data.append(pd.read_csv('EEG_database_Deep_class.csv'))'''
   #print(data)
   #z=x.transpose()
   #=np.log10(x)

   '''data[0]=np.log10(data[0])
   data[1]=np.log10(data[1])
   data[2] = np.log10(data[2])
   data[3] = np.log10(data[3])'''

   '''for i in range(4):
    Alphamean= (data[i]['lowAlpha']+data[i]['highAlpha'])/2
    Betamean = (data[i]['lowBeta'] + data[i]['highBeta']) / 2
    data[i]['checkattention']=(Betamean/Alphamean)'''
   #result = pd.concat(data, keys=['x', 'y'])
   #ax1.plot(result.ix['x']['lowAlpha'])
   ax1.clear()
   ax2.clear()
   ax3.clear()
   ax4.clear()
   ax1.set_title("lowBeta")
   ax2.set_title("highAlpha")
   ax3.set_title("meditation")
   ax4.set_title("attention")
   ax1.plot(data['lowBeta'])
   ax2.plot(data['highAlpha'])
   ax3.plot(data['meditation'])
   ax4.plot(data['attention'])





   #y= np.loadtxt('EEG_database_Pankaj_baseline.csv',dtype=float,delimiter=',',skiprows=1, unpack=True)


   bins = [0, 10, 20,30,40,50,60,70,80,90,100]

   #sns.boxplot(data=[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9]], orient="v")
   #sns.boxplot(data=data[0], orient="v")
   #sns.boxplot(data=data[0],orient="v")




   #sns.boxplot(data=[y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9]], orient="v")

   #sns.swarmplot(data=x)



  # plt.xlabel('EEG Parameters')
  #plt.ylabel('Log values')
  #plt.title('Comparison Between Two Sets')
   #plt.legend()

  #while 1:
   #time.sleep(2)
   #live()
  ani = animation.FuncAnimation(fig, live, interval=1000)
  plt.show()
