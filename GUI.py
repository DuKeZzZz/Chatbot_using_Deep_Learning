from tkinter import *
import threading
import pyttsx3
import speech_recognition as sr
from response_code import *
from file_search_engine import *
from Funcs import *


class App():
    def __init__(self, main):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('volume', 1.5)

        self.main = main
        self.main.geometry("400x500")
        self.main.configure(background='#383A49')
        self.ChatLog = Text(main, bg="#383A49", fg="#ffffff", bd=0, height="8", width="50", font="Arial", wrap=WORD)
        self.ChatLog.config(state=DISABLED)

        self.scrollbar = Scrollbar(main, command=self.ChatLog.yview, cursor="heart")
        self.ChatLog['yscrollcommand'] = self.scrollbar.set

        self.SendButton = Button(main, font=("Verdana", 12, 'bold'), text="Send", width=6, height=5,
                                 bd=0, bg="#FE79C7", activebackground="#6272A4", fg='#ffffff',
                                 command=self._send)
        self.isrecording = False
        self.photo = PhotoImage(file="microphone.png").subsample(15, 15)
        self.mic_button = Button(main, image=self.photo, width=38, height=5,
                                 bd=0, bg="#FE79C7", activebackground="#6272A4", fg='#ffffff')
        self.mic_button.bind("<Button-1>", self.startrecording)
        self.mic_button.bind("<ButtonRelease-1>", self.stoprecording)
        self.mic_button.pack()

        self.EntryBox = Text(main, font=("Verdana", 8, 'bold'), bd=0, bg="white", width="29", height="5", wrap=WORD, )
        self.EntryBox.bind("<Return>", self.entersend)
        self.EntryBox.bind("<Button-1>", self.entersend)

        self.on_img = PhotoImage(file="speaker_on.png").subsample(15, 15)
        self.off_img = PhotoImage(file="speaker_off.png").subsample(30, 30)
        self.speak_is_on = True
        self.speak_flag = Button(main, image=self.on_img, width=19, bd=0, command=self.speak_mode,
                                 bg="#FE79C7", activebackground="#6272A4", fg='#ffffff')

        # Place all components on the screen
        self.scrollbar.place(x=376, y=6, height=435)
        self.ChatLog.place(x=6, y=6, height=435, width=370)
        self.EntryBox.place(x=128, y=449, height=45, width=240)
        self.SendButton.place(x=50, y=449, height=45)
        self.mic_button.place(x=6, y=449, height=45)
        self.speak_flag.place(x=374, y=449, height=22)

    def speak_given(self, audio: str):
        self.engine.say(audio)
        self.engine.runAndWait()

    def startrecording(self, event):
        self.isrecording = True
        t = threading.Thread(target=self._record)
        t.start()

    def stoprecording(self, event):
        self.isrecording = False


    def _record(self):
        while self.isrecording:
            self.r = sr.Recognizer()

            with sr.Microphone() as source:
                print("speak")
                self.r.adjust_for_ambient_noise(source, duration=3)
                self.audio = self.r.listen(source)
                # self.r.pause_threshold = 1
                print("done")
            try:
                query = self.r.recognize_google(self.audio, language='en-in')
                print(query)
                self.EntryBox.insert("1.0", query)
            except Exception as e:
                print(e)

    def _send(self):
        self.msg = self.EntryBox.get("1.0", 'end-1c').strip()
        self.EntryBox.delete("0.0", END)

        if self.msg != '':
            self.ChatLog.config(state=NORMAL)
            self.ChatLog.insert(END, "You: " + self.msg + '\n\n')
            self.ChatLog.config(foreground="#ffffff", font=("Verdana", 12))

            res = final_response(self.msg)

            if res["display"] != '':
                try:
                    if self.speak_is_on:
                        self.speak_given(res["speak"])

                    # if res["query"] == "chatter":
                    #     self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')

                    if res["display"] == "exit":
                        main.destroy()

                    elif res["display"] == "shutting down...":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        os.system("shutdown /s /t 1")

                    elif res["display"] == "restaring..":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        os.system("shutdown -t 0 -r -f")

                    elif res["display"] == "opening file search engine...":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        file_GUI()

                    elif res["display"] == "searching wikipedia" :
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        wiki = wiki_search(query=res["query"])
                        self.ChatLog.insert(END, "Bot: " + wiki + '\n\n')

                    elif res["display"] == "opening mail..":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        info: dict = mail_GUI()
                        if info['username'] and info['password']:
                            mail = sendmail(username=info['username'], password=info['password'], receiver=info['receiver'],
                                            subject=info['subject'], body=info['body'])
                            self.ChatLog.insert(END, "Bot: " + mail + '\n\n')

                    elif res["display"] == "getting info..":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        wolfram_Api_id = 'WJWXA7-4Q3XKPGKK8'
                        info: str = wolfram_resp(res["query"], wolfram_Api_id)
                        self.ChatLog.insert(END, "Bot: " + info + '\n\n')

                    elif res["display"] == "searching google...":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        nouns = noun_adj_finder(res["query"])
                        print(nouns)
                        try:
                            nouns.remove('google')
                        except ValueError:
                            pass
                        try:
                            nouns.remove('search')
                        except ValueError:
                            pass
                        s = ' '
                        s = s.join(nouns)
                        search_google(s)

                    elif res["display"] == "here's the news...":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        nouns = noun_adj_finder(res["query"])
                        try:
                            nouns.remove('news')

                        except ValueError:
                            pass
                        try:

                            nouns.remove('latest')
                        except ValueError:
                            pass
                        if nouns:
                            s = ' '
                            s = s.join(nouns)
                            newss = news(s)
                        else:
                            newss = news()
                        self.ChatLog.insert(END, newss + '\n\n')

                    elif res["display"] == "locating...":
                        nouns = noun_adj_finder(res["query"])
                        try:
                            nouns.remove('location')

                        except ValueError:
                            pass
                        try:

                            nouns.remove('locate')

                        except ValueError:
                            pass
                        try:

                            nouns.remove('map')
                        except ValueError:
                            pass
                        s = ' '
                        s = s.join(nouns)
                        loc = locate(s)
                        self.ChatLog.insert(END, "Bot: " + loc + '\n\n')

                    elif res["display"] == "searching weather...":
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')
                        city = weather_GUI()
                        if city['city']:
                            weather_info = weather(city['city'])
                            self.ChatLog.insert(END, "Bot: " + weather_info + '\n\n')

                    else:
                        self.ChatLog.insert(END, "Bot: " + res["display"] + '\n\n')


                except:
                    self.ChatLog.insert(END, "Bot: " + "Something went wrong!" + '\n\n')

                self.ChatLog.config(state=DISABLED)
                self.ChatLog.yview(END)

    def entersend(self, event):
        t = threading.Thread(target=self._send)
        t.start()

    def speak_mode(self):

        # Determine it is on or off
        if self.speak_is_on:
            self.speak_flag.config(image=self.off_img)
            self.speak_is_on = False
        else:
            self.speak_flag.config(image=self.on_img)
            self.speak_is_on = True


main = Tk()
app = App(main)
main.mainloop()
