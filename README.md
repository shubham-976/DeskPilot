# DeskPilot
 Voice based Virtual Desktop Assistant to automate desktop/computer tasks.

# Voice-Based Virtual Assistant

Welcome to the Voice-Based Virtual Assistant project! This virtual assistant named as 'Deskpilot' is developed using various tools and technologies like Python, various libraries and modules of python, wikipedia API, web scraping techniques etc. In response to our voice-based commands, it automates various tasks on our desktop computer , making our life easier and more productive.

## Features
** Based on our voice commands , as of now, this assistant is able to automate the following tasks :

1. **Voice Input to Text Conversion**: 
   - Take voice input from the user through a microphone and convert it into text.
   
2. **Text to Speech Output**: 
   - Convert text to speech and output through the speaker.

3. **Open Sites/Applications**: 
   - Open specified websites or applications on our computer.

4. **Current Time**: 
   - Tell the current time.

5. **Today's Date**: 
   - Tell today's date.

6. **Current Weather**: 
   - Provide the realtime current weather information as per our location.

7. **Set Alarm**: 
   - Set an alarm to ring at the mentioned time..

8. **Set Timer**: 
   - Set a timer.

9. **Speech to Text File**: 
   - Convert speech to text and save it in a `.txt` file or Notes making feature.

10. **According to Wikipedia Search/Query**: 
    - Search for a query using the Wikipedia API and provide information.

11. **Play Songs/Music**: 
    - Play all songs one after another from a specified playlist.

12. **Capture Screenshot**: 
    - Capture a screenshot and save it.

13. **Trending News**: 
    - Provide top trending news and links to read more about these news.

14. **Send Email**: 
    - Send an email easily by voice commands.

## Installation and Configuration

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Required Python libraries (detailed below)

### 1. Clone the Repository

clone the repository or download the complete folder.

### 2. Install Dependencies

Install the Python and required Python libraries using pip. Required modules/libraries/packages are mentioned below : 

**SpeechRecognition** : To recognize the our voice commands  
**requests** : To request content from a URL for web scrapping  
**bs4** : (Beautiful Soup) used to parse the scrapped content from URLs during web scrapping  
**wikipedia** : To get answers to queries from the wikipedia API  
**mutagen** : To get duration of a music/song  
**pyautogui** : To capture the screenshot  
**dotenv** : To load API_keys/secrets/passwords from config.env to the program file/code  
  
**NOTE 1** : There might be some other dependencies/modules needed, that will be shown in terminal while running, install them using pip (if any)  
**NOTE 2** : In this repo, two .whl files are there, install any one of them or both, they are needed to convert text to voice using speaker in windows (This stuff is different for macOS or linux)  

### 3. Configure the config.env
Create a file named config.env in the same root directory.  
create two variables in this file and assign suitable values :  
i. **SMTP_MAIL_ID** = your_mail_id_here, this will be the default mail_id, from which emails will be sent  
ii. **SMTP_APP_PASSWORD** = your_above_account_password (this way is not recommended) or app_password_created_from_google_account (this way is recommended and preferred)  
(This configuraion is must for sending email functionality)

## 4. Ready to go

Now we are all set to go, Run the main script to start the 'DeskPilot' :

```bash
python main.py
```
Try the above mentioned features one by one, based on your voice commands.

## 5. To exit  
Say 'stop stop' (i.e. speak 'stop' keyword multiple times (>=2)).  


## ------------ T H A N K S  F O R  R E A D I N G ------------  



