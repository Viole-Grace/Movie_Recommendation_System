from __future__ import print_function
from bs4 import BeautifulSoup as SOUP
#from feeling import feels
import re as regex
import requests as HTTP
import math 
def target(emotion):
    urlhere = ""
    if emotion == "sad":
        urlhere = 'http://www.imdb.com/search/title?genres=drama&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "disgust":
        urlhere = 'http://www.imdb.com/search/title?genres=musical&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "anger":
        urlhere = 'http://www.imdb.com/search/title?genres=family&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "anticipation" or "enjoyment":
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "fear":
        urlhere = 'http://www.imdb.com/search/title?genres=sport&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "trust":
        urlhere = 'http://www.imdb.com/search/title?genres=western&amp;title_type=feature&amp;sort=moviemeter, asc'
    elif emotion == "surprise":
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&amp;title_type=feature&amp;sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    field = SOUP(data, "lxml")
    #REGEX EXTRACTION OF TITLES
    title = field.find_all("a", attrs = {"href" : regex.compile(r'\/title\/tt+\d*\/')})
    return title 
def analyse():
    emotion = raw_input("Enter the emotion: ")
    sent=emotion.lower()
    n=int(raw_input("Enter no. of movie recommendations you want : "))
    print("Top",n," Recommended Movies : ")
    series = target(sent)
    count=0
    print_function(series)
    for i in series :
        movie = str(i).split('>')
        if(len(movie) == 3):
            print(movie[1][:-3]) 
            count+=1
        if(count == n+1):
            break
analyse()