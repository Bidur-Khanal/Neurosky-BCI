### run as main module

import cv2 
import numpy as np
import blinkcheck1 as bc
import timeit
w = 52
h = 52


def main_program():

    blink = bool(0)
    finished = bool(0)
    start = timeit.default_timer()

#Your statements here

 
    size = 600,1000, 3
    background = np.zeros(size, dtype=np.uint8)
    img = cv2.imread('./data/arrow.jpg')
    cv2.putText(background, " Blink to select the correct direction",\
                (165,52), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
 
    start_pos_x = 140
    start_pos_y = 300
    
    # position to place rect box
    
    backgnd = cv2.addWeighted(img,0.5,background,0.9,0)  # add two images
    temp = backgnd.copy()
    cv2.rectangle(temp,(start_pos_x, start_pos_y),(start_pos_x+w,\
                    start_pos_y+h),(25,2,255),25)
    cv2.imshow('Vehicle Guidance' , temp)
    while 1:
        
        temp = backgnd.copy()
        #place rect

        blink = bc.check_blink()   #bc module returns true if blinked
        print ("blink = " , blink)


        if blink == True:          #if blinked, check the arrow direction
           if start_pos_x==140:
               stop = timeit.default_timer()
               
           start_pos_y = start_pos_y-h

           cv2.rectangle(temp,(859,38),(859+w,38+h),(25,2,255),2)                     #change the color of rect
           cv2.putText(temp, "Blinked!!",\
             (856,32), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
                 
        else:  #false
            
            cv2.rectangle(temp,(859,38),(859+w,38+h),(0,255,0),2)

        if start_pos_x < 880:  #check the box has reached the end mark
            cv2.rectangle(temp,(start_pos_x, start_pos_y),(start_pos_x+w,\
                    start_pos_y+h),(25,2,255),25)   #move forward
        else:
            if finished == False:
                
                stop = timeit.default_timer()
            finished = True
            time = int(stop - start)
            
            start_pos_x = 900
            start_pos_y = 300
            cv2.putText(temp, "Completed!",\
             (400,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
            cv2.putText(temp, str(time)+" seconds",\
             (407,228), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
            cv2.rectangle(temp,(start_pos_x, start_pos_y),(start_pos_x+w,\
                    start_pos_y+h),(25,200,255),25)
        

            
        cv2.imshow('Vehicle Guidance' ,temp)
        key = cv2.waitKey(10)
        if key == 27:
            break;
        
    key = cv2.waitKey()
    if key == 27:
        cv2.destroyAllWindows()
    return;
main_program()
