import urllib.request
from urllib import parse

resp = urllib.request.urlopen('https://s-m.com.sa/')

#avialable functions from the library
print("The type of response for the usrl: " , type(resp))
print("The response code: " , resp.code)
print("The length of the reponse: " , resp.length)
print("Peeking on the response: " , resp.peek()) #returns bytes object

data = resp.read()
html = data.decode("UTF-8") #decode based on the used encoding
print("The html code of this page: " , html)

print("IS there still connection? " , ("no" if resp.isclosed() else "yes"))



