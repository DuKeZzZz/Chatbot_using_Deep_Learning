import webbrowser
query = input("Search : ")
url = "https://www.google.com.tr/search?q={}".format(query)
webbrowser.get('windows-default').open(url, new=2, autoraise=True)