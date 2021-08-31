import subprocess
import winshell


# -----Mail Code-----

import yagmail
import getpass


def sendmail(username: str, password: str, receiver: str, subject: str, body: str) -> str:
    """
    sends an email to an input  email address
    user needs to provide:
        self mail: the mail id of the user.
        self password: The password of the user.
        receiver mail: mail of the recipient
        subject and body: contents of the email.
        :rtype: object
    """
    try:
        username = username

        passw = password

        reciever = receiver

        yag = yagmail.SMTP(username, password=passw)
        subject = subject
        contents = body
        yag.send(reciever, subject, contents)

    except Exception as e:
        return str(e)

    else:
        return f"mail sent successfully to {reciever}"


# -----wikipedia code-----

import wikipedia


def wiki_search(query: str) -> str:
    """
    :param query: The string user wants to search on wikipedia
    :return: results of the search
    """
    try:

        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=5)

        return results
    except Exception as e:
        return e


# -----play random music code-----

import os
import random


def play_music():
    """
    plays music at random in a specific folder: C:\\Users\\Jay\\Music
    """
    try:
        music_dir = "C:\\Users\\Jay\\Music"
        songs = os.listdir(music_dir)
        i = random.randint(1, len(songs))
        os.startfile(os.path.join(music_dir, songs[i]))

    except Exception as e:
        return e


# -----browser search-----

import webbrowser


def search_google(query: str):
    """"
    :param query: string to perform google search on.
    returns search results based upon the query, opens default browser.
    """
    try:
        query = query.replace("search", "")
        query = query.replace("google", "")
        url = "https://www.google.com.tr/search?q={}".format(query)
        webbrowser.get('windows-default').open(url, new=2, autoraise=True)
    except Exception as e:
        return e


# -----news_search------

from newsapi import NewsApiClient


def news(query: str = None) -> str:
    """"
    :param query: string to search for news articles, by default = None.
    prints the latest news articles
    """
    res = ""
    try:
        api = NewsApiClient(api_key='026019d869f44dfa8e81adf97cd7413f')
        if query:
            data = api.get_everything(q=query)
            i = 1
            for item in data['articles']:
                res = res + str(i) + '. ' + item['title'] + '\n'
                res = res + item['description'] + '\n'
                i += 1
                if i > 5:
                    break
            return res

        else:
            data = api.get_top_headlines(country='in')
            i = 1
            for item in data['articles']:
                res = res + str(i) + '. ' + item['title'] + '\n'
                res = res + item['description'] + '\n'
                i += 1
                if i > 5:
                    break
            return res

    except Exception as e:
        return e


# -----location-----

def locate(query: str) -> str:
    """
    opens google maps in default browser with query as location
    :param query: THe location user wants to search
    """
    try:
        location = query
        webbrowser.get('windows-default').open("https://www.google.com/maps/place/" + location + "")
        return f"locating {query}"
    except Exception as e:
        return str(e)


# -----weather-----

import requests


def weather(city: str) -> str:
    """"
    returns weather data on a certain location
    user need to input:
        city name: name of the City the user wants to return the weather of.
    """
    city_name = city
    try:
        api_key = "4976543d8c907988acd7253caeb603b1"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        weather_info = ""

        if x["cod"] != "404":
            weather_info += f"Description = {x['weather'][0]['description']}\n" \
                            f"Temperature (in Celsius unit) = {x['main']['temp'] - 273: .2f} feels like {x['main']['feels_like'] - 273: .2f}\n" \
                            f"Atmospheric pressure (in hPa) = {x['main']['pressure']}\n" \
                            f"Humidity(in percentage) = {x['main']['humidity']}\n"
            return weather_info

        else:
            return "city not found"
    except Exception as e:
        return e


#  ------noun Finder-------

import nltk


def noun_adj_finder(query: str) -> list:

    try:
        nouns = []  # empty to array to hold all nouns

        for word, pos in nltk.pos_tag(nltk.word_tokenize(query)):
            if pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS' or pos == 'JJ' or pos == 'JJS' or pos == 'JJR':
                nouns.append(word)

        return nouns
    except Exception as e:
        return e


# ------wolframalpha query pass------

import wolframalpha


def wolfram_resp(query: str, api_id: str):
    try:
        app = wolframalpha.Client(api_id)
    except:
        return "API not working"

    res = app.query(query)
    final_info = ""
    for pod in res.pods:
        for sub in pod.subpods:
            final_info += str(sub.plaintext) + "\n"

    return final_info
