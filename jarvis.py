# packages required are imported
import json
import os
import ctypes
import subprocess
import tkinter
import webbrowser
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import speech_recognition as sr
from urllib.request import urlopen
from tkinter.messagebox import askyesno

# tkinter window is created

window = tkinter.Tk()
window.geometry("1024x768")
window.title("J.A.R.V.I.S--by--SANKET PATIL")

# speech recognition is enabled

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# background image has been set

bg = tkinter.PhotoImage(file="bg.gif")
label1 = tkinter.Label(window, image=bg)
label1.place(x=0, y=0)
frame1 = tkinter.Frame(window)
frame1.pack(pady=20)


# commands which you hear are spoken through this function

def talk(text):
    engine.say(text)
    engine.runAndWait()


# this function listens to the user

def take_command():
    try:
        with sr.Microphone() as source:
            lis = "listening"
            talk(lis)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except sr.UnknownValueError:
        pass
    return command


# main function containing all code

def run_jarvis():
    command = take_command()
    window.update()
    a = tkinter.Label(window, text=command, bg="black", fg="white")
    a.pack(pady=200)
    window.update()
    a.after(1000, a.destroy())
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'say' in command:
        say = command.replace('say', '')
        talk(say)
    elif 'yourself' in command:
        talk('Hello, I am Jarvis. I am a Ai voice bot made by Sanket Patil. I can help you. Say something')
    elif 'Who are you' in command:
        talk('Hello, I am Jarvis. I am a Ai voice bot made by Sanket Patil. I can help you. Say something')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        window.update()
        b = tkinter.Label(window, text=time, bg="black", fg="white")
        b.pack(side="bottom", pady=200)
        window.update()
        talk('Current time is ' + time)
        window.update()
        b.after(3000, b.destroy())
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        window.update()
        c = tkinter.Label(window, text=os.linesep + info + os.linesep, bg="black", fg="white")
        c.pack(side="bottom", pady=200)
        window.update()
        talk(info)
        c.after(1000, c.destroy())
    elif 'how are you' in command:
        talk("I am fine, Thank you")
        talk("How are you, Sir")
    elif 'fine' in command or "good" in command:
        talk("It's good to know that your fine")
    elif 'exit' in command:
        talk("Thanks for giving me your time")
        window.destroy()
    elif "who made you" in command or "who created you" in command:
        talk("I have been created by Sanket.")
    elif "who am i" in command:
        command("If you talk then definitely your human.")
    elif "why you came to world" in command:
        talk("Thanks to Sanket. further It's a secret")
    elif "who are you" in command:
        talk("I am your virtual assistant created by Sanket")
    elif 'reason for you' in command:
        talk("I was created as a Minor project by Mister Sanket ")
    elif 'tell me news' in command:

        try:
            urll = 'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=\\timesofIndiaApikey\\'
            jsonObj = urlopen(urll)
            data = json.load(jsonObj)
            i = 1

            talk('here are some top news from the times of india')

            for item in data['articles']:
                h = tkinter.Label(window, text=item['title'], bg="black", fg="white")
                h.pack(side="bottom", pady=200)
                h.after(1000, h.destroy())
                g = tkinter.Label(window, text=item['description'], bg="black", fg="white")
                g.pack(side="bottom", pady=200)
                g.after(1000, g.destroy())
                talk(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:
            f = tkinter.Label(window, text=e, bg="black", fg="white")
            f.pack(side="bottom", pady=200)
            f.after(1000, f.destroy())
    elif "write a note" in command:
        talk("What should i write, sir")
        note = take_command()
        file = open('jarvis.txt', 'w')
        i = tkinter.Label(window, text=note, bg="black", fg="white")
        i.pack(side="bottom", pady=200)
        i.after(1000, i.destroy())
        talk("Sir, Should i include date and time")
        snfm = take_command()
        if 'yes' in snfm or 'sure' in snfm:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)
        else:
            file.write(note)

    elif "show note" in command:
        talk("Showing Notes")
        file = open("jarvis.txt", "r")
        j = tkinter.Label(window, text=file.read(), bg="black", fg="white")
        j.pack(side="bottom", pady=200)
        j.after(1000, j.destroy())
        talk(file.read(6))
    elif 'what is' in command:
        word = command.replace('what is', '')
        infor = wikipedia.summary(word, 2)
        window.update()
        d = tkinter.Label(window, text=infor, bg="black", fg="white")
        d.pack(side="bottom", pady=200)
        window.update()
        talk(infor)
        d.after(1000, d.destroy())
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif "will you be my girlfriend" in command or "will you be my boyfriend" in command:
        talk("I'm not sure about, may be you should give me some time")
    elif 'lock window' in command:
        talk("locking the device")
        ctypes.windll.user32.LockWorkStation()
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'shutdown system' in command:
        talk("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')
    elif 'I love you' in command:
        talk('Aww, So Sweet, But Sorry, I am in a relationship with wifi')
    elif "restart" in command:
        subprocess.call(["shutdown", "/r"])
    elif "hibernate" in command or "sleep" in command:
        talk("Hibernating")
        subprocess.call("shutdown / h")
    elif "log off" in command or "sign out" in command:
        talk("Make sure all the application are closed before sign-out")
        subprocess.call(["shutdown", "/l"])
    elif "where is" in command:
        command = command.replace("where is", "")
        location = command
        talk("Tracing Location")
        talk(location)
        url = "https://www.google.nl/maps/place/" + location + ""
        webbrowser.open(url, new=0)
    elif "camera" in command or "take a photo" in command:
        subprocess.run('start microsoft.windows.camera:', shell=True)
    elif "search on google" in command:
        command = command.replace("search on google", "")
        search = command
        talk("searching"+search+"on google")
        urrl = "https://www.google.com/search?q=" + search + ""
        webbrowser.open(urrl, new=0)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        window.update()
        e = tkinter.Label(window, text=joke, bg="black", fg="white")
        e.pack(side="bottom", pady=200)
        window.update()
        e.after(1000, e.destroy())
    else:
        talk('Sorry, I did not get it, Please say the command again.')
        run_jarvis()


# executed after button "Click To Speak" is Clicked

def listen():
    window.update()
    tkinter.Label(window, text="Hello I Am Jarvis", bg="black", fg="white").place(x=510, y=100, anchor="s")
    tkinter.Label(window, text="Please Be Patient While Using Me", bg="black", fg="white").place(x=510, y=130, anchor="s")
    tkinter.Button(bg="black", fg="white", width=20, activeforeground="grey", activebackground="black",
                   text="Run",
                   command=run_jarvis).place(x=510, y=700, anchor="n")
    window.update()
    talk("Hello I am Jarvis, Click On Run Button And Speak Something")


# executed after button "Click To Stop" is Clicked
def confirm():
    answer = askyesno(title='confirmation',
                      message='Are you sure that you want to quit?')
    if answer:
        window.destroy()


# both buttons on main screen

btn1 = tkinter.Button(text="Click To Speak", bg="black", fg="white", width=20, activeforeground="grey",
                      activebackground="black", command=listen)

btn1.pack(padx=0, pady=0, side="bottom")
btn1.pack(side="left")

btn2 = tkinter.Button(text="Click To Stop", bg="black", fg="white", width=20, activeforeground="grey",
                      activebackground="black", command=confirm)

btn2.pack(padx=0, pady=0, side="bottom")
btn2.pack(side="right")

# main executable loops

window.resizable(False, False)
window.mainloop()
