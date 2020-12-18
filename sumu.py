import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    '''
    It will wish you as a starting
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning !')
    elif hour>=12 and hour<=18:
        speak('Good Afternoon !')
    else:
        speak('Good Evening !')
    speak('I am sumu here. How may I help you sharif?')

def takecommand():
    '''
        It will take command what you will say and returnt command as string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        # r.energy_threshold =50
        audio = r.listen(source)
        
    try:
        print('recognizing...')
        # for english en-GB
        query = r.recognize_google(audio,language='en_GB')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sharif.hossain.iubat@gmail.com','Sharifiubat@1394')
    server.sendmail('sharif.hossain.iubat@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    # speak('hello sharif, how are you?')
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            try:
                    
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia','')
                result = wikipedia.summary(query,sentences=2)
                speak("According to wikipedia ")
                print(result)
                speak(result)
            except Exception as e:
                speak('No content found in wikipedia.')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open file' in query:
            directory = 'C:\\Users\\Sharif Hossain\\Desktop\\spring2020\\SE'
            files = os.listdir(directory)
            os.startfile(os.path.join(directory,files[0]))


        elif 'open program' in query:
            programpath = "C:\\Users\\Sharif Hossain\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(programpath)
        elif 'send email' in query:
            speak('Whom you want to send?')
            # to = takecommand()+'@gmail.com' 
            to = 'sharifhossain582@gmail.com'
            speak(f'you are sending an email to {to}. Is it ok?')
            ok_or_not=takecommand()
            if 'yes' in ok_or_not:
                speak('What should i say?')
                content = takecommand()
                speak(f'Content of your email is {content}. Is it ok?')
                ok_or_not=takecommand()
                if 'yes' in ok_or_not:
                    # speak('Email successfully sent')
                    try:
                        sendEmail(to,content)
                    except Exception as e:
                        speak('failed to send mail')
                        print(e)
                else:
                    continue
                    
            else:
                speak('Please try again, sir.')
                continue


        elif 'goodbye'in query or 'good bye' in query:
            speak('Thank you sir.')
            break

