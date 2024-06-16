
import winsound
import datetime
import time
import os
import argparse 
from art import tprint  # art is an external repo found on github, for printing big size aplhabets

def setTimerRingTimer(timer_ring_time, total_seconds):
    # total_seconds variable is needed to represent time left on the terminal screen
    # but for ringing timer.wav file, the concept is wait until current time becomes equal to timer_ring_time
    
    # Get current time.
    # print("timer_ring_time = ", timer_ring_time)
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%Y-%m-%d %H:%M:%S") #remove milliseconds from seconds
    # strftime("%H:%M:%S") NOT USED means now time also contains DATE for matching

    # Check whether timer_ring_time is equal to current time (with Date) or not.
    # keep waiting until current time becomes = timer_ring_time
    while current_time != timer_ring_time:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        H,M,S =0,0,0
        S = total_seconds%60
        M = total_seconds//60
        H = M//60
        M = M%60
        # print("Current Time :",current_time, "  ||  Timer will ring at :", timer_ring_time, end="\r") 
        tprint("{:02d}  :  {:02d}  :  {:02d}".format(H,M,S))
        # print(end="\r") # end=\r is used to print at same line, overwriting the previously printed line
        time.sleep(1) #so that printing of milliseconds again and again can be avoided, print only after 1 sec interval
        total_seconds -= 1
        os.system('cls') #for clearing the terminal screen, to print next tiimestamp of timer at same place instead of below the previosly printed place.

    # Playing sound.
    tprint("   T I M E  U P   ")
    winsound.PlaySound(".\\audioFiles\\timer.wav",winsound.SND_ALIAS)


if __name__ == '__main__':
    # extracting time string from the argument of script being run in main.py using system.os('start python setTimer.py -timerFlag timestring')
    parser = argparse.ArgumentParser()
    parser.add_argument('-timerFlag', nargs='+')
    parser.add_argument('-totalSeconds', nargs='+')
    args = parser.parse_args()
    # print("args = ", args)
    timer_ring_time = ""
    timer_ring_time = args.timerFlag[0] #date from string
    # because in argumnet passed there is a space bw date and time, so argstimerFlag.[0], [1] both needed
    timer_ring_time += " "
    timer_ring_time += args.timerFlag[1] #time from string
    total_seconds = args.totalSeconds[0]
    total_seconds = int(total_seconds)

    # Call alarm function.
    setTimerRingTimer(timer_ring_time, total_seconds)

