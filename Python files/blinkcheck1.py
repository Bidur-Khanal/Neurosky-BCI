#set up connection to device
#collect realtime data from device
#return true if blincked

import cv2 
raw_data =54  #supppose


def check_blink():
        ## pressing enter retunrs True - moves the tect forward
        key = cv2.waitKey(3000)
        if key == 13:
            return True;
        else:
            
            return False;
        

