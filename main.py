from functionality import voiceInputFromUser, say
from functionality import openSiteApps, sayTime, sayDate, sayWeather
from functionality import setAlarm, setTimer, voiceToTextFile
from functionality import searchAtWikipedia, playMusic, captureScreenshot
from functionality import scrapTrendingNews, createSendEmail

import datetime

# Task-1  : Take voice input from user through microphone and convert it into text
# Task-2  : text to speech as output through speaker
# Task-3  : open the sites / applications
# Task-4  : Tell the current time
# Task-5  : Tell the todays date
# Task-6  : Tell the current weather 
# Task-7  : set Alarm (will ring as soon as the mentioned time comes irrespective of day)
# Task-8  : Set a timer
# Task-9  : convert Speech to text and save in a .txt file
# Task-10 : search about the query using Wikipedia API
# Task-11 : Play ALL songs one after another from a directory (whose path is provided in code, this directory contains music files to be played)
# Task-12 : capture Screenshot and save it.
# Task-13 : Provide top trending news and their links to read more about them.
# Task-14 : Sending email


# Execution of Program
# if this below 'if' statement is not used, then while importing variables in another file from this file, this file automatically starts executing :(
if __name__ == "__main__": 
    welcome_str1 = "Hi!, I am DeskPilot, your virtual desktop assistant."
    welcome_str2 = "How may i help you ? "
    print()
    print(welcome_str1)
    print(welcome_str2)
    say(welcome_str1)
    say(welcome_str2)
    print()
    # queryText = "play music"
    while True:
        print("Listening . . . . . . . . . ")
        queryText = voiceInputFromUser()
        # say(text)
        if "open" in queryText.lower():
            openSiteApps(queryText)
        elif "date and time" in queryText.lower() or "time and date" in queryText.lower() or "date time" in queryText.lower() or "time date" in queryText.lower():
            sayDate()
            sayTime()
        elif "the time" in queryText.lower() or "current time" in queryText.lower() or "time now" in queryText.lower() or "what time" in queryText.lower():
            sayTime()
        elif "the date" in queryText.lower() or "today's date" in queryText.lower() or "todays date" in queryText.lower() or "date today" in queryText.lower() or "what date" in queryText.lower():
            sayDate()
        elif "the weather" in queryText.lower() or "current weather" in queryText.lower() or "todays weather" in queryText.lower() or "today's weather" in queryText.lower() or "weather today" in queryText.lower():
            sayWeather()
        elif "alarm" in queryText.lower():
            setAlarm(queryText)
        elif "timer" in queryText.lower():
            setTimer(queryText)
        elif "take notes" in queryText.lower() or "make notes" in queryText.lower() or "speech to text" in queryText.lower() or "voice to text" in queryText.lower() or "save notes" in queryText.lower() or "voice to notes" in queryText.lower() or "speech to notes" in queryText.lower():
            voiceToTextFile()
        elif "according to wikipedia" in queryText.lower() or "as per wikipedia" in queryText.lower() or "according to the wikipedia" in queryText.lower() or "as per the wikipedia" in queryText.lower():
            searchAtWikipedia(queryText)
        elif "play music" in queryText.lower() or "start music" in queryText.lower() or "play song" in queryText.lower() or "start song" in queryText.lower() or "playlist" in queryText.lower():
            playMusic()
            # queryText = ""
        elif "screenshot" in queryText.lower():
            captureScreenshot()
        elif "news" in queryText.lower():
            scrapTrendingNews()
        elif "send email" in queryText.lower() or "write email" in queryText.lower() or "send an email" in queryText.lower() or "write an email" in queryText.lower():
            createSendEmail()
        elif "ok bye" in queryText.lower() or "stop stop" in queryText.lower() or "exit exit" in queryText.lower():
            print("\n=> Good Bye ! Have a nice day.")
            print("=> Thanks for Using deskPilot.\n")
            say("Good Bye ! Have a nice day.")
            exit()
        else:   
            say(queryText)


        