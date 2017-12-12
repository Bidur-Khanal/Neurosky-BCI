import sys
import csv
from neuroskymain import *
import time



class collect_data:
 def collector (self):
  record_from_brain = Brain()
  while not record_from_brain.isConnected():
  		print ('brain not yet connected, trying again in 5 seconds')
  		time.sleep(5)
  print ("brain now connected presumably, lets get some data")
  print("sleep for 3 seconds then check again")
  time.sleep(3)


  #print(record_from_brain.fullstr())

  with open('EEG_new.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(record_from_brain.justheaders())
      for i in range(120):
          time.sleep(2)
          print(record_from_brain.fullstr())
          #print("blink",record_from_brain.getProperty(blinkStrength))
          writer.writerow(record_from_brain.fullstr())

