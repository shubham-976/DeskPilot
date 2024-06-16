import win32com.client
import speech_recognition as sr
import webbrowser
import os
import subprocess
import datetime
import requests
from bs4 import BeautifulSoup
import wikipedia
import time
from mutagen.mp3 import MP3 # to get duration of a song (i.e. MP3 file)
import pyautogui # for capturing screenshot
import smtplib # for sending email 
from dotenv import load_dotenv # to load API_secrets/passwords/keys related variables from env file
from email.message import EmailMessage # to handle subject,message,to,from all 4 components of an email effectively

load_dotenv(".\\config.env") # all secret variables loaded from given file path

# Task-1 : Take voice input from user through microphone and convert it into text
def voiceInputFromUser():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            queryText = r.recognize_google(audio, language='en-in')
            print(f"     You said : {queryText}")
            return queryText
        except Exception as e:
            # means either no sound for time greater than 'pause threshold' or sound is there but unable to convert that into text
            print(f"    -----------")
            return " "
        
# Task-2 : text to speech as output through speaker
def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


# Task-3 : open the sites / applications
def openSiteApps(queryText):
    sites = [["youtube", "https://youtube.com"], ["you tube", "https://youtube.com"], 
             ["google drive", "https://drive.google.com"], ["drive", "https://drive.google.com"],
             ["email", "https://mail.google.com"], ["mail", "https://mail.google.com"], ["gmail", "https://mail.google.com"],
             ["google", "https://google.com"], 
             ["wikipedia", "https://wikipedia.com"], ["wiki pedia", "https://wikipedia.com"], 
             ["whatsapp", "https://web.whatsapp.com"], 
             ["chatgpt", "https://chat.openai.com"], ["chat gpt", "https://chat.openai.com"], ["gpt", "https://chat.openai.com"]]
    apps = [['calculator', 'calc'], 
            ['camera', 'start microsoft.windows.camera:'], 
            ["vscode", 'code'], ["vs code", 'code'], ["v s code", 'code'], ["visual studio code", 'code'],
            ["notepad", "Notepad"], ["note pad", "Notepad"],
            ["excel", "start excel.exe"], ["ms excel", "start excel.exe"], ["m s excel", "start excel.exe"], ["microsoft excel", "start excel.exe"],
            ["powerpoint", "start powerpnt.exe"], ["ms powerpoint", "start powerpnt.exe"], ["m s powerpoint", "start powerpnt.exe"], ["microsoft powerpoint", "start powerpnt.exe"], ["ppt", "start powerpnt.exe"], ["p p t", "start powerpnt.exe"],
            ["word", "start winword.exe"], ["ms word", "start winword.exe"], ["m s word", "start winword.exe"], ["microsoft word", "start winword.exe"],
            ["chrome", "start chrome.exe"], ["google chrome", "start chrome.exe"], ["browser", "start chrome.exe"], ["chrome browser", "start chrome.exe"], ["google chrome browser", "start chrome.exe"],
            ["edge", "start msedge.exe"], ["edge browser", "start msedge.exe"], ["microsoft edge", "start msedge.exe"], ["microsoft edge browser", "start msedge.exe"]]
    flag = False
    for site in sites:
        if f"open {site[0]}" in queryText.lower():
            say(f"opening {site[0]} . . . ")
            webbrowser.open(site[1])
            flag = True
    for app in apps:
        if f"open {app[0]}" in queryText.lower():
            say(f"opening {app[0]}")
            os.system(app[1])
            flag = True
    if ".com" in queryText.lower():
        idx = queryText.find(".com")
        name = ""
        for i in range(idx-1, -1, -1):
            if queryText[i]==" ":
                break
            name += queryText[i]
        name = name[::-1]
        say(f"opening {name}.com . . . ")
        # print(f"https://www.{name}.com")
        webbrowser.open(f"https://www.{name}.com")
        flag = True
    if ".in" in queryText.lower():
        idx = queryText.find(".in")
        name = ""
        for i in range(idx-1, -1, -1):
            if queryText[i]==" ":
                break
            name += queryText[i]
        name = name[::-1]
        say(f"opening {name}.in . . . ")
        webbrowser.open(f"https://www.{name}.in")
        flag = True
        
    if flag==False:
        say("Sorry! No such website or application found.")
    
# Task-4 : Tell the current time
def sayTime():
    H = datetime.datetime.now().strftime("%H")
    M = datetime.datetime.now().strftime("%M")
    S = datetime.datetime.now().strftime("%S")
    str = f"    The time is : {H} hours {M} minutes and {S} seconds."
    print(str)
    say(str)

# Task-5 : Tell the todays date
def sayDate():
    day = datetime.datetime.now().strftime("%d")
    day = int(day)
    month = datetime.datetime.now().strftime("%B")
    year = datetime.datetime.now().strftime("%Y")

    weekDaysMapping = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    idx = datetime.datetime.now().weekday()

    str = f"    Today, its {day} {month}, {year} that is {weekDaysMapping[idx]} "
    print(str)
    say(str)

# Task-6 : Tell the current weather 
def sayWeather():
    # using web scrapping
    url = "https://www.google.com/search?q="+"weather"
    html = requests.get(url).content
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    # temp[2] = °
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # saying all data
    print(f"Temperature is {temp}")
    say(f"Temperature is {temp}")
    print(f"Time: {time}")
    say(f"Time: {time}")
    print(f"Sky Description: {sky}")
    say(f"Sky Description: {sky}")

# Task-7 : set Alarm (will ring as soon as the mentioned time comes irrespective of day)
def setAlarm(queryText):
    set_alarm_time = ""
    # a.m. case
    if 'a.m.' in queryText.lower() or 'a.m' in queryText.lower() or 'A.M.' in queryText or 'am' in queryText.lower() or 'a m' in queryText.lower():
        idx = queryText.find(':')
        if(idx<0 or idx>=len(queryText)):
            print('     !! Unable to detect time for setting up Alarm. Please try Again.')
            say('Unable to detect time for setting up Alarm. Please try Again.')
            return
        hour = int(queryText[idx-2:idx])
        minute = int(queryText[idx+1: idx+3])
        if(hour==12):  # special case , in speech 12:02 am it means night 12 am means for clock its 00:02:00 
            set_alarm_time += "00"
        elif(hour<=9): 
            set_alarm_time += '0'
            set_alarm_time += str(hour)
        set_alarm_time += ":"
        if(minute <= 9):
            set_alarm_time += '0'
        set_alarm_time += str(minute)
        set_alarm_time += ":00"
        # special case , in speech 12:00 am it means night 12 am means for clock its 00:00:00 
        if(hour==12 and minute==0): 
            set_alarm_time = "00:00:00"
        say(f"Setting up the alarm.")
        # instead of calling setAlarmRingAlarm() function from file setAlarm.py, we need to execute this file 'setAlarm.py' in separate terminal
        # because if that function is called then current terminal will wail until alarm rings and will not be able to hear any other new
        # command until alarm rings, that's why to avoid that to keep current terminal active for new commands we executed setAlarm.py filr
        # in seperate terminal.
        print("     set alarm time = ",set_alarm_time)
        os.system('start python setAlarm.py -timestrflag %s'%(set_alarm_time)) 
        say("Done. Alarm will ring on time.")
        return
    # p.m. case
    if 'p.m.' in queryText.lower() or 'p.m' in queryText.lower() or 'P.M.' in queryText or 'pm' in queryText.lower() or 'p m' in queryText.lower():
        idx = queryText.find(':')
        if(idx<0 or idx>=len(queryText)):
            print('     !! Unable to detect time for setting up Alarm. Please try Again.')
            say('Unable to detect time for setting up Alarm. Please try Again.')
            return
        hour = int(queryText[idx-2:idx])
        minute = int(queryText[idx+1: idx+3])
        if(hour==12):  # special case , in speech 12:02 pm it means night afternoon 12 pm means for clock its 12:02:00 
            set_alarm_time += "12"
        elif(hour<=11): 
            x = 12+hour
            set_alarm_time += str(x)
        set_alarm_time += ":"
        if(minute <= 9):
            set_alarm_time += '0'
        set_alarm_time += str(minute)
        set_alarm_time += ":00"
        say(f"Setting up the alarm.")
        print("     set alarm time = ",set_alarm_time)
        os.system('start python setAlarm.py -timestrflag %s'%(set_alarm_time)) 
        say("Done. Alarm will ring on time.")
        return
    
# Task-8 : Set a timer
def setTimer(queryText):
    H, M, S = 0, 0, 0
    if "hour" in queryText.lower() or "hours" in queryText.lower():
        idx = queryText.find("hour")
        if(idx>=0 and idx<len(queryText)):
            H = int(queryText[idx-3:idx-1])
    if "minute" in queryText.lower() or "minutes" in queryText.lower():
        idx = queryText.find("minute")
        if(idx>=0 and idx<len(queryText)):
            M = int(queryText[idx-3:idx-1])
    if "second" in queryText.lower() or "seconds" in queryText.lower():
        idx = queryText.find("second")
        if(idx>=0 and idx<len(queryText)):
            S = int(queryText[idx-3:idx-1])
    # to handle few anomalies
    M += (S//60)  # if seconds >= 60 
    S = (S%60)

    H += (M//60)  # if minutes >= 60
    M = (M%60)

    total_seconds = H*60*60 + M*60 + S + 0 # sometine delay occurs of extra seconds to cover the procedure running time , so add 3 or 4 or 5 at place of 0 after S + 

    # rest will be handled by datetime.deltatime() function itself
    # this below time will include DATE also, so it will handle timer >= 24 hours also , no issue regarding that
    timer_ring_time = datetime.datetime.now() + datetime.timedelta(seconds=S+3, minutes=M, hours=H) #S+3 done because the whole process (saying by bot, printing in terminal etc) is taking around(estimate) 5 seconds extra just before the timer window opens
    timer_ring_time = timer_ring_time.strftime("%Y-%m-%d %H:%M:%S") #remove milli seconds from seconds
    say(f"Setting up the timer.")
    print("    Timer time = ",timer_ring_time)
    total_seconds = str(total_seconds)
    os.system('start python setTimer.py -timerFlag %s -totalSeconds %s'%(timer_ring_time, total_seconds)) 
    say("Done. Timer will ring on time.")

# Task-9 : convert Speech to text and save in a txt file

def voiceToTextFile():
    print("     Please tell Title  : ")
    print("   ",end="")
    say("Please Tell Title ")
    title = voiceInputFromUser()
    notes = ""
    notes += "Start Timestamp : "
    notes += datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes += "\n\n"
    notes += "Title : "
    notes += title
    notes += "\n\n"
    while True:
        print("     Listening for saving Speech to Text . . . . . . ")
        print("   ",end="")
        text_from_speech = voiceInputFromUser()
        if "stop stop" in text_from_speech.lower() or "wait wait" in text_from_speech.lower() or "exit exit" in text_from_speech.lower() or "quit quit" in text_from_speech.lower():
            notes += text_from_speech
            notes += "\n" 
            break
        elif text_from_speech == " ":
            continue
        else:
            notes += text_from_speech
            notes += "\n"

    notes += "\nEnd Timestamp : "
    end_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes += end_timestamp
    say("Saving the text . ")
    if len(title)>15:
        title = title[0:15]
    file_name = title #file_name should NOT contain symbols like :(colon), slash(\, /) because in path they have different meanings, will cause error
    file_name += " "
    file_name += datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    f = open(f".\\voiceToTextNotes\\{file_name}.txt", "w+") #filename
    f.write(notes)
    f.close()
    say(f"Done. Please Check 'Voice to text notes' directory.")

# Task-10 : search about the query using Wikipedia API
def searchAtWikipedia(queryText):
    if("according to wikipedia") in queryText.lower():
        queryText = queryText.replace("according to wikipedia", "")
    if("according to the wikipedia") in queryText.lower():
        queryText = queryText.replace("according to the wikipedia", "")
    if("as per wikipedia") in queryText.lower():
        queryText = queryText.replace("as per wikipedia", "")
    if("as per the wikipedia") in queryText.lower():
        queryText = queryText.replace("as per the wikipedia", "")
    try:
        results_say = wikipedia.summary(queryText, sentences=2)
        results_print = wikipedia.summary(queryText, sentences=13)
        results_print = results_print.split(". ") # instead of printing whole paragraph, just to print line by line
        for x in results_print:
            print("     ", end="")
            print("-> ",x,".")
        say(results_say)
    except Exception as e:
        print("     No response from Wikipedia API for this query.")
        say("No response from Wikipedia API for this query.")

# Task-11 : Play ALL songs one after another from a directory (whose path is provided in code, this directory contains music files to be played)
def playMusic():
    os.system('start python playMusic.py')

# Task-12 : take Screenshot and save it.
def captureScreenshot():
    image = pyautogui.screenshot()

    path_of_folder = ".\\capturedScreenshots"
    image_name = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S")
    image_name += ".jpg"

    image.save(os.path.join(path_of_folder, image_name))
    print("     Screenshot captured and saved.")
    say("Screenshot captured and saved.")

# Task-13 : Provide top trending news and their links to get details.
def scrapTrendingNews():
    # here ndtv.com website is scrapped to get trending news
    print("     Here are some top trending news . . .")
    say("Here are some top trending news.")
    r = requests.get('https://www.ndtv.com/trends')
    html_content = BeautifulSoup(r.content, 'html.parser')
    all_req_divs = html_content.find_all(class_="trenz_news_head lh22 listing_story_title") #figured out this class myself from above url page, it may change in future if url or website changes
    
    count = 1
    for req_div in all_req_divs:
        anchor = req_div.find('a')
        print("     ",count,".", anchor.string) #anchor.string will give text bw anchor tags i.e. <a>this is anchor string</a>
        print("        Link ->",anchor.get('href')) #.get('href) will fetch the link inside href i.e. <a href="link here">...</a>
        print()
        count += 1
        if(count > 10): #showing top 10 news only
            break

# Task-14 : Sending Email
def createSendEmail():
    print("     Please tell Subject of the email : ")
    print("   ",end="")
    say("Please tell Subject of the email .")
    subject = voiceInputFromUser()
    message = ""
    while True:
        print("     Listening for email content . . . . . . ")
        print("   ",end="")
        text_from_speech = voiceInputFromUser()
        if "stop stop" in text_from_speech.lower():
            idx = text_from_speech.find("stop")
            message += text_from_speech[0:idx]
            message += "\n" 
            break
        elif "next line" in text_from_speech.lower() or "blank line" in text_from_speech.lower() or "line break" in text_from_speech.lower() or "leave one line" in text_from_speech.lower() or "leave one line blank" in text_from_speech.lower() or "nothing" in text_from_speech.lower():
            idx = text_from_speech.find("next line")
            message += text_from_speech[0:idx]
            message += "\n"
        elif text_from_speech == " ":
            continue
        else:
            message += text_from_speech
            message += ". "
    message += "\n--------"
    
    say("Please TYPE Receiver's email id .")
    to = input("        Please type Receiver's email id : ")

    # now initialize EmailMessage object to handle its all 4 components
    msg = EmailMessage()
    msg['Subject'] = subject
    msg.set_content(message)
    msg['From'] = str(os.getenv("SMTP_MAIL_ID")) #getting my(sender) mail_id from .env file
    msg['To'] = to # receiver mail id

    # create smtp session and send email
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls() # starting Transport Layer Security
    session.login(os.getenv("SMTP_MAIL_ID"), os.getenv("SMTP_APP_PASSWORD"))
    session.send_message(msg)
    session.quit()
    print("\n       Email has been sent Successfully . ")
    say("Email has been sent successfully.")



    





        

