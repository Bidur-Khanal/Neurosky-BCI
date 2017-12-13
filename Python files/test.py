import time
from neuroskymain import *
from collect_data import *
from load_and_plot_data_static import *
from plot_data_dynamic import *
from blink_only import *
from threading import Thread
from learning import *
from rawdata_collector import *
from ML import *


def testBrain():
    #learning= machinelearning()
    ml=learning()
    #th1 = Thread(target=blinking())
    #th2 = Thread(target=main_program())
    #main_program()
    # blinking()
    #th1.setDaemon(True)
    #th2.setDaemon(True)
    #th2.start()
    #th1.start()
    #th1.run()
    #th2.run()
    #learn= learning()

    # plot= load_plot()
    '''blinked=blink()
 while 1:

     i= blinked.getProperty(blinkStrength)
     if i>0.0:
      print("blink",i)'''

    #data= collect_rawdata ()

    #data.collector()
    #plot = plot_dynamic()



    '''my_brain = Brain()
  while not my_brain.isConnected():
 		print ('brain not yet connected, trying again in 5 seconds')
 		time.sleep(5)
  print ("brain now connected presumably, lets get some data")

  while 1:
   print ("sleep for 3 seconds then check again")
   time.sleep(3)
   #print ("lowAlpha: %d\tattention: %f" % (my_brain.getProperty(lowAlpha), my_brain.getProperty(attention)))
   print (" All data\n", my_brain.fullstr())
   #print(my_brain.justheaders())'''


if __name__ == '__main__':
    testBrain()
