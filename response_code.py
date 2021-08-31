from Funcs import *
from secondary_GUI import *
from file_search_engine import *
from chatter import chatbot
import datetime
import pyjokes
#  ------DL model response retreival functions-------

import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from tensorflow.keras.models import load_model

model = load_model('chatbot_model.h5')
import json
import random

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def model_response(ints, intents_json):
    list_of_intents = intents_json['intents']
    result: str = ''
    for i in list_of_intents:
        if i['tag'] == ints:
            result = result + (random.choice(i['responses']))
            break
    return result


# ------real responses------


def first_check(query: str) -> dict:
    query = query.lower()
    try:
        if 'open youtube' in query:
            webbrowser.get('windows-default').open("https://www.youtube.com")
            final = {"speak": "opening youtube",
                     "display": "opening youtube..."}
            return final

        elif 'wikipedia' in query:
            final = {"query": query,
                     "speak": "searching wikipedia",
                     "display": "searching wikipedia"}
            return final

        elif 'play music'in query:
            play_music()
            final = {"query": query,
                     "speak": "playing music..",
                     "display": "playing music.."}
            return final

        elif 'open google' in query:
            webbrowser.get('windows-default').open("https://www.google.com")
            final = {"speak": "opening google",
                     "display": "opening google.."}
            return final

        elif 'open powerpoint' in query:
            os.startfile("shortcuts\\PowerPoint.lnk")
            final = {"speak": "opening powerpoint",
                     "display": "opening powerpoint.."}
            return final

        elif 'open word' in query:
            os.startfile("shortcuts\\Word.lnk")
            final = {"speak": "opening word",
                     "display": "opening word.."}
            return final

        elif 'open excel' in query:
            os.startfile("shortcuts\\Excel.lnk")
            final = {"speak": "opening excel",
                     "display": "opening excel.."}
            return final

        elif 'open outlook' in query:
            os.startfile("shortcuts\\Outlook.lnk")
            final = {"speak": "opening outlook",
                     "display": "opening outlook.."}
            return final

        elif 'open stackoverflow' in query:
            webbrowser.get('windows-default').open("https://www.stackoverflow.com")
            final = {"speak": "opening stackoverflow",
                     "display": "opening stackoverflow..."}
            return final

        elif 'exit' in query:
            final = {"speak": "goodbye",
                     "display": "exit"}
            return final

        elif 'shutdown system' in query:
            final = {"speak": "shutting down",
                     "display": "shutting down..."}
            return final

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            final = {"speak": "clearing recycle bin",
                     "display": "clearing recycle bin..."}
            return final

        elif "restart" in query:
            final = {"speak": "restaring",
                     "display": "restaring.."}
            return final

        else:
            final = {"speak": "",
                     "display": ""}
            return final

    except Exception as e:
        final = {"speak": "", "display": str(e)}
        return final


def model_actions(query: str) -> dict:
    try:
        res = predict_class(query, model)
        intent = res[0]['intent']
        prob = res[0]['probability']
        if float(prob) > 0.9:
            if 'greeting' in intent:
                res1 = model_response(intent, intents)
                final = {"query": query, "speak": res1, "display": res1}
                return final

            elif 'goodbye' in intent:
                res1 = model_response(intent, intents)
                final = {"query": query, "speak": res1, "display": res1}
                return final

            elif 'thanks' in intent:
                res1 = model_response(intent, intents)
                final = {"query": query, "speak": res1, "display": res1}
                return final

            elif 'options' in intent:
                res1 = model_response(intent, intents)
                final = {"query": query, "speak": res1, "display": res1}
                return final

            elif 'file_search' in intent:
                final = {"query": query, "speak": "opening file search engine",
                         "display": "opening file search engine..."}
                return final


            elif 'mail' in intent:
                final = {"query": query, "speak": "opening mail", "display": "opening mail.."}
                return final


            elif 'question' in intent:
                final = {"query": query, "speak": "getting info", "display": "getting info.."}
                return final


            elif 'google_search' in intent:
                final = {"query": query, "speak": "searching google", "display": "searching google..."}
                return final

            elif 'time' in intent:

                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                final = {"query": query, "speak": f"the time is {strtime}", "display": f"the time is {strtime}"}
                return final

            elif 'joke' in intent:
                joke = pyjokes.get_joke()
                final = {"query": query, "speak": "here's a random joke", "display": joke}
                return final

            elif 'news_search' in intent:
                final = {"query": query, "speak": "here's the news", "display": "here's the news..."}
                return final

            elif 'location' in intent:
                final = {"query": query, "speak": "locating", "display": "locating..."}
                return final

            elif 'weather' in intent:
                final = {"query": query, "speak": "searching weather", "display": "searching weather..."}
                return final
        else:
            final = {"query": query, "speak": "", "display": ""}
            return final

    except Exception as e:
        final = {"query": query, "speak": "", "display": str(e)}
        return final


def final_response(query: str) -> dict:
    query.lower()
    first_chk = first_check(query)
    if first_chk["display"]:
        return first_chk

    model_act = model_actions(query)
    if model_act["display"]:
        return model_act

    res = chatbot.get_response(query)
    res = str(res)
    res = res.replace("<Statement text:", "")
    res = res.replace(">", "")
    final = {"query": "chatter", "speak": res, "display": res}
    return final
