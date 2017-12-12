### run as main module


import cv2 
import numpy as np
import blinkcheck as bc
from blink_only import *
from threading import Thread
import random
import time

w = 52
h = 52

blinked = bool(0)
top = "Top"
left = "Left"
right= "Right"
down= "Down"

def main_program():
    blinking=blink() #from blink_only module, blink class instantiation
    i= 0
    '''size = 600,1000, 3
    background = np.zeros(size, dtype=np.uint8)
    img = cv2.imread('./data/arrow.jpg')
    cv2.putText(background, " Blink to select the correct direction",\
                (165,52), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)

    rect_position = [(859,38),(793,82),(860,131),(920,83)]   # position to place rect box
    backgnd = cv2.addWeighted(img,0.5,background,0.9,0)  # add two images'''

    rect_position = [(859, 38), (795, 82), (859, 132), (922, 81)]
    size = 600, 1000, 3
    background = np.zeros(size, dtype=np.uint8)
    img = cv2.imread('./data/arrow.jpg')
    cv2.putText(background, " Blink to select the correct direction", \
                (165, 52), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 58, 255), 2)

    start_pos_x = 140
    start_pos_y = 300
    i = 0;
    score = 0

    # position to place rect box

    backgnd = cv2.addWeighted(img, 0.5, background, 0.9, 0)  # add two images
    temp = backgnd.copy()
    #cv2.rectangle(temp, (start_pos_x, start_pos_y), (start_pos_x + w, \
    #                                                 start_pos_y + h), (25, 2, 255), 25)
    cv2.imshow('Vehicle Guidance', temp)

    food_pos_x = random.randint(200, 650)
    food_pos_y = random.randint(220, 400)


    while i < 4:

        blinked=False
        blinkvalue =0.0
        m = blinking.getProperty(blinkStrength)
        time.sleep(0.1)
        blinkvalue=blinkcheck.got_blink(blinkcheck)
        blinkcheck.get_blink(blinkcheck,0.0)
        temp = backgnd.copy()
        cv2.rectangle(temp,rect_position[i],(rect_position[i][0]+w,\
                      rect_position[i][1]+h),(0,255,0),2)                     #place rect

         #returns blinkstrength value
        print(blinkvalue)
        if blinkvalue >0.0:
            blinked = True
        else:
            blinked= False
        #print ("blink = " , blinked)

        if blinked == True:                 #if blinked, check the arrow direction


            cv2.rectangle(temp,rect_position[i],(rect_position[i][0]+w,\
                      rect_position[i][1]+h),(25,2,255),2)                     #change the color of rect
            if i==0:
                start_pos_x = start_pos_x
                start_pos_y = start_pos_y - h
                cv2.putText(temp, top,\
                (856,232), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
                print (top)
            elif i==1:
                start_pos_x = start_pos_x - w
                start_pos_y = start_pos_y
                cv2.putText(temp, left,\
                (856,232), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
                print (left)
            elif i==2:
                start_pos_x = start_pos_x
                start_pos_y = start_pos_y + h
                cv2.putText(temp, down,\
                (856,232), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
                print(down)
            else:
                start_pos_x = start_pos_x + w
                start_pos_y = start_pos_y
                cv2.putText(temp, right,\
                (856,232), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,58, 255),2)
                print (right)
        #else:  # false
         #   cv2.rectangle(temp, rect_position[i], (rect_position[i][0] + w, \
          #                                         rect_position[i][1] + h), (25, 2, 255), 2)

        if start_pos_x < 80:  # check the box has reached the end mark
            start_pos_x = 80
        if start_pos_y < 150:  # check the box has reached the end mark
            start_pos_y = 150
        if start_pos_x > 880:  # check the box has reached the end mark
            start_pos_x = 880
        if start_pos_y > 520:  # check the box has reached the end mark
            start_pos_y = 520

        if (abs(start_pos_x - food_pos_x) < w and abs(start_pos_y - food_pos_y) < h):

            food_pos_x = random.randint(150, 720)
            food_pos_y = random.randint(220, 400)
            score = score + 10

        else:

            print("dfj")

        cv2.putText(temp, "Score " + str(score), \
                    (320, 92), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 228, 205), 2)
        cv2.rectangle(temp, (food_pos_x, food_pos_y), (food_pos_x + w, \
                                                       food_pos_y + h), (215, 20, 25), 25)
        cv2.rectangle(temp, (start_pos_x, start_pos_y), (start_pos_x + w, \
                                                         start_pos_y + h), (25, 200, 255), 25)

        i = i+1
        if i == 4:
            i=0

        key = cv2.waitKey(500)  #delay for 3 seconds (can be reduced!!!!!!!!)

        if key == 27:                    #if esc pressed
            print ("exit")
            break
        cv2.imshow('Vehicle Guidance' ,temp)

    key = cv2.waitKey()
    cv2.destroyAllWindows()

    return;




