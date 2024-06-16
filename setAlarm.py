
import winsound
import datetime
import argparse 
import time
from art import tprint # art is an external repo found on github, for printing big size aplhabets

def setAlarmRingAlarm(set_alarm_time):

    # Get current time.
    # print("sel alarm time = ", set_alarm_time)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Check whether set alarm is equal to current time or not.
    # keep waiting until current time becomes = alarm_time
    
    while current_time != set_alarm_time:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time :", current_time, "  ||  Alarm Time :", set_alarm_time, end="\r") # \r is used to print at same line, overwriting the previously printed line
        time.sleep(1) #so that printing of milliseconds again and again can be avoided, print only after 1 sec interval


    # Playing sound.
    print("\n\n")
    tprint("   A L A R M   R I N G I N G   ")
    tprint(set_alarm_time)
    winsound.PlaySound(".\\audioFiles\\alarm.wav",winsound.SND_ALIAS)


if __name__ == '__main__':
    # extracting time string from the argument of script being run in main.py using system.os('start python setAlarm.py -timestr timestring')
    parser = argparse.ArgumentParser()
    parser.add_argument('-timestrflag', nargs='+')
    args = parser.parse_args()
    set_alarm_time = ""
    set_alarm_time = args.timestrflag[0]

    # Call alarm function.
    setAlarmRingAlarm(set_alarm_time)

