# # from Assistant import Assistant
# # import webbrowser
# from response_code import *
# from Funcs import *
#
# # Assistant = Assistant(as_name="bro")
#
# # res = first_check('open youtube')
# # Assistant.speak(res)
#
#
# # if __name__ == "__main__":
# #     while True:
# #         msg = input("msg:")
# #         res = predict_class(msg, model)
# #         print(res)
#
#
# # from newsapi import NewsApiClient
# #
# # res = ""
# # query = "covid-19"
# # api = NewsApiClient(api_key='026019d869f44dfa8e81adf97cd7413f')
# # data = api.get_everything(q=query)
# # i = 1
# # for item in data['articles']:
# #     res = res + str(i) + '. ' + item['title'] + '\n'
# #     res = res + item['description'] + '\n'
# #
# #     i += 1
# #     if i > 5:
# #         break
# #
# # print(res)
#
# # import requests
# #
# # api_key = "4976543d8c907988acd7253caeb603b1"
# # base_url = "http://api.openweathermap.org/data/2.5/weather?"
# # city_name = input("Enter city name : ")
# # complete_url = base_url + "appid=" + api_key + "&q=" + city_name
# # response = requests.get(complete_url)
# # x = response.json()
# # weather_info = f"description = {x['weather'][0]['description']} \n" \
# #                 f"Temperature (in Celsius unit) = {x['main']['temp'] - 273: .2f} feels like {x['main']['feels_like'] - 273: .2f} \n" \
# #                 f"atmospheric pressure (in hPa) = {x['main']['pressure']} \n" \
# #                 f"humidity(in percentage) = {x['main']['humidity']}"
# # print(weather_info)
# #
# # Assistant.speak(weather_info)
#
#
# # import nltk
# # nltk.download('averaged_perceptron_tagger')
# #
# # lines = "locate rome"
# # nouns = []  # empty to array to hold all nouns
# #
# # for word, pos in nltk.pos_tag(nltk.word_tokenize(lines)):
# #     if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS':
# #         nouns.append(word)
# # try:
# #     nouns.remove('locate')
# # except:
# #     pass
# #
# #
# # print(nouns)
#
# # from Funcs import *
# # import nltk
# #
# # query = 'please find todays latest news for covid_19'
# # sentence_words = noun_adj_finder(query)
# # sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
# # print(sentence_words)
#
# #
# # import datetime
#
# # if "mail" in res:
# #     ChatLog.insert(END, "\n Enter your gmail username: ")
# #     uname = ChatLog.get("1.0", 'end-1c')
# #     ChatLog.insert(END, "\n password: ")
# #     ChatLog.config(show="*")
# #     passw = ChatLog.get("1.0", 'end-1c')
# #     ChatLog.config(show="")
# #     ChatLog.insert(END, "\n reveiver's mail:")
# #     rec = ChatLog.get("1.0", 'end-1c')
# #     ChatLog.insert(END, "\n Subject:")
# #     subject = ChatLog.get("1.0", 'end-1c')
# #     ChatLog.insert(END, "\n Body:")
# #     body = ChatLog.get("1.0", 'end-1c')
# #     res = sendmail(uname, passw, rec, subject, body)
#
# # from email_GUI import mail_GUI
# #
#
# # from tkinter import *
# # import threading
# # import pyttsx3
# # import speech_recognition as sr
# # from response_code import *
# # #
# # #
# # class App():
# #     def __init__(self, main):
# #         self.main = main
# #         self.main.geometry("400x500")
# #         self.ChatLog = Text(main, bd=0, bg="white", height="8", width="50", font="Arial", wrap=WORD)
# #         self.ChatLog.config(state=DISABLED)
# #
# #         self.scrollbar = Scrollbar(main, command=self.ChatLog.yview, cursor="heart")
# #         self.ChatLog['yscrollcommand'] = self.scrollbar.set
# #
# #         self.SendButton = Button(main, font=("Verdana", 12, 'bold'), text="Send", width=6, height=5,
# #                                  bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
# #                                  command=self._send)
# #         self.isrecording = False
# #         self.photo = PhotoImage(file="microphone.png").subsample(15, 15)
# #         self.mic_button = Button(main, image=self.photo, width=38, height=5,
# #                                  bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff')
# #         self.mic_button.bind("<Button-1>", self.startrecording)
# #         self.mic_button.bind("<ButtonRelease-1>", self.stoprecording)
# #         self.mic_button.pack()
# #
# #         self.EntryBox = Text(main, bd=2, bg="white", width="29", height="5", font="Arial", wrap=WORD, )
# #         # EntryBox.bind("<Return>", send)
# #
# #         # Place all components on the screen
# #         self.scrollbar.place(x=376, y=6, height=386)
# #         self.ChatLog.place(x=6, y=6, height=386, width=370)
# #         self.EntryBox.place(x=128, y=449, height=45, width=265)
# #         self.SendButton.place(x=50, y=449, height=45)
# #         self.mic_button.place(x=6, y=449, height=45)
# #
# #     def startrecording(self, event):
# #         self.isrecording = True
# #         t = threading.Thread(target=self._record)
# #         t.start()
# #
# #     def stoprecording(self, event):
# #         self.isrecording = False
# #
# #     def _record(self):
# #         while self.isrecording:
# #             r = sr.Recognizer()
# #
# #             with sr.Microphone() as source:
# #
# #                 audio = r.listen(source)
# #
# #             try:
# #                 query = r.recognize_google(audio, language='en-in')
# #                 self.EntryBox.insert("1.0", query)
# #             except Exception as e:
# #                 print(e)
# #
# #     def _send(self):
# #         self.msg = self.EntryBox.get("1.0", 'end-1c').strip()
# #         self.EntryBox.delete("0.0", END)
# #
# #         if self.msg != '':
# #             self.ChatLog.config(state=NORMAL)
# #             self.ChatLog.insert(END, "You: " + self.msg + '\n\n')
# #             self.ChatLog.config(foreground="#442265", font=("Verdana", 12))
# #
# #             res = final_response(self.msg)
# #             self.ChatLog.insert(END, "Bot: " + str(res) + '\n\n')
# #
# #             self.ChatLog.config(state=DISABLED)
# #             self.ChatLog.yview(END)
# #
# #
# # main = Tk()
# # app = App(main)
# # main.mainloop()
#
# # from tkinter import *
# # import pyttsx3
# # import speech_recognition as sr
# # from response_code import *
# #
# # def send():
# #     msg = EntryBox.get("1.0",'end-1c').strip()
# #     EntryBox.delete("0.0",END)
# #
# #     if msg != '':
# #         ChatLog.config(state=NORMAL)
# #         ChatLog.insert(END, "You: " + msg + '\n\n')
# #         ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
# #
# #         res = final_response(msg)
# #         ChatLog.insert(END, "Bot: " + str(res) + '\n\n')
# #
# #         ChatLog.config(state=DISABLED)
# #         ChatLog.yview(END)
# #
# # def use_mic(event):
# #     r = sr.Recognizer()
# #
# #     with sr.Microphone() as source:
# #
# #         audio = r.listen(source)
# #
# #     try:
# #         query = r.recognize_google(audio, language='en-in')
# #         print(query)
# #     except Exception as e:
# #         pass
# #
# # base = Tk()
# # base.title("Hello")
# # base.geometry("400x500")
# # base.resizable(width=FALSE, height=FALSE)
# #
# # photo = PhotoImage(file="microphone.png").subsample(15,15)
# #
# # ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
# #
# # ChatLog.config(state=DISABLED)
# #
# # #Bind scrollbar to Chat window
# # scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
# # ChatLog['yscrollcommand'] = scrollbar.set
# #
# # #Create Button to send message
# # SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width=6, height=5,
# #                     bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
# #                     command= send )
# #
# #
# # #Create the box to enter message
# # EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
# # #EntryBox.bind("<Return>", send)
# #
# #
# # #Place all components on the screen
# # scrollbar.place(x=376,y=6, height=386)
# # ChatLog.place(x=6,y=6, height=386, width=370)
# # EntryBox.place(x=128, y=449, height=45, width=265)
# # SendButton.place(x=50, y=449, height=45)
# #
# #
# # base.mainloop()
#
#
#
# # nouns = noun_adj_finder(query)
# #                 try:
# #                     nouns.remove('google')
# #                 except ValueError:
# #                     pass
# #                 try:
# #                     nouns.remove('search')
# #                 except ValueError:
# #                     pass
# #                 s = ' '
# #                 s = s.join(nouns)
# #                 search_google(s)
#
# # nouns = noun_adj_finder(query)
# #                 try:
# #                     nouns.remove('news')
# #
# #                 except ValueError:
# #                     pass
# #                 try:
# #
# #                     nouns.remove('latest')
# #                 except ValueError:
# #                     pass
# #                 if nouns:
# #                     s = ' '
# #                     s = s.join(nouns)
# #                     newss = news(s)
# #                 else:
# #                     newss = news()
#
# # nouns = noun_adj_finder(query)
# #                 try:
# #                     nouns.remove('location')
# #
# #                 except ValueError:
# #                     pass
# #                 try:
# #
# #                     nouns.remove('locate')
# #
# #                 except ValueError:
# #                     pass
# #                 try:
# #
# #                     nouns.remove('map')
# #                 except ValueError:
# #                     pass
# #                 s = ' '
# #                 s = s.join(nouns)
# #                 loc = locate(s)
# #
# # city = weather_GUI()
# #                 final = {"query": query, "speak": "searching google", "display": "searching google..."}
# #                 if city['city']:
# #                     res = weather(city['city'])
# #                     return res
# #                 else:
# #
# #                    return ""
#
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("speak")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)
    r.pause_threshold = 1
    print("done")
try:
    query = r.recognize_google(audio, language='en-in')
    print(query)
except Exception as e:
    print(e)


# from response_code import *
# from chatter import chatbot
#
# while 1:
#     query = input("Enter query:")
#     res = final_response(query)
#     print(res)

# from Funcs import *
#
# from secondary_GUI import *
# try:
#     # sendmail(username='bloothhoondr', password='Blooth!99', receiver='jayymahajan291999', subject='helllasda', body='working?')
#     yag = yagmail.SMTP('bloothhoondr', password='Blooth!99')
#     subject = 'helllasda'
#     contents = 'body'
#     yag.send('jayymahajan291999@gmail.com', subject, contents)
# except Exception as e:
#     print(e)
# import os
# os.system("shutdown /s /t 1")