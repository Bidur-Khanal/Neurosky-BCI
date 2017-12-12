#set up connection to device
#collect realtime data from device
#return true if blincked


class blinkcheck():
 x=0.0
 @staticmethod
 def get_blink(self,blink):
    self.x=blink
    #print("yoyo",self.x)


 def got_blink(self):
  #print("momo")
  return self.x



  

