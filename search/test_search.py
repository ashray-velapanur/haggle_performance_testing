import threading
import datetime
import urllib2
import urllib
import random
import os
import subprocess
import json

url = 'https://www.haggle-test1.appspot.com/api/vendors/search'

HAGGLE_CUISINES = ['BBQ',
                   'Bar',
                   'Burgers',
                   'Cafe',
                   'Chinese',
                   'Dessert',
                   'FastFood',
                   'French',
                   'Indian',
                   'Italian',
                   'Mexican',
                   'MiddleEastern',
                   'Pizza',
                   'Seafood',
                   'Steakhouse',
                   'Japanese',
                   'Vegetarian',
                   'Other']

with open('../cookies.txt') as file:
    cookies = json.load(file)

def worker(cookie):
    category = random.choice(HAGGLE_CUISINES)
    dollar_rating = str(random.randrange(1,6,1)) 
    party_size = str(random.randrange(1,7,1))
    request = '?category=' + category + '\&dollar_rating=' + dollar_rating + '\&time=\&party_size=' + party_size
    subprocess.call('ab -n 200 -C ' + cookie + ' ' + url, shell=True)

for cookie in cookies[:5]:
    t = threading.Thread(target=worker, args=(cookie,))
    t.start()
    
