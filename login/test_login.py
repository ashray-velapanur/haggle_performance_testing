import threading
import datetime
import urllib2
import urllib
import random
import os
import subprocess
import json

url = 'https://haggle-test1.appspot.com/users/login'
access_tokens = {}

with open('../cookies.txt') as file:
    cookies = json.load(file)

with open('../ThirdPartyUserData') as file:
    for line in file.readlines():
        access_tokens[str(line.split(',')[1])] = str(line.split(',')[0])

def worker(id, access_token):
    file = open('post_data', 'w')
    print >> file, 'id=' + id + '&access_token=' + access_token
    file.close()
    subprocess.call('ab -n 200 -p post_data ' + url, shell=True)

for id, access_token in access_tokens.iteritems():
    t = threading.Thread(target=worker, args=(id,access_token,))
    t.start()
