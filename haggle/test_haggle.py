import json
import urllib
import random
import threading
import subprocess

url = 'https://www.haggle-test1.appspot.com/api/haggles'

vendor_ids = []

with open('../cookies.txt') as file:
    cookies = json.load(file)

with open('../Campaign') as file:
    for line in file.readlines():
        vendor_ids.append(line.split(',')[0])

def worker(cookie, count):
    data = {
            'vendor_id': random.choice(vendor_ids),
            'party_size': 1, 
            'bid': random.choice([10, 20, 30]),
            'time': random.choice(['9:00', '18:00'])
            }
    filename = 'data_' + str(count) 
    file = open(filename, 'w')
    print >> file, urllib.urlencode(data)
    file.close()
    subprocess.call('ab -n 5 -p ' + filename + ' -T application/x-www-form-urlencoded -C ' + cookie + ' ' + url, shell=True)

for count, cookie in enumerate(cookies[:5]):
    t = threading.Thread(target=worker, args=(cookie,count,))
    t.start()

