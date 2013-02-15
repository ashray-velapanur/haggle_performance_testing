import json
import urllib
import urllib2
import cookielib

url = 'https://www.haggle-test1.appspot.com/login_help_haggler'

emails = []
cookies = []

count = 0

with open('User') as file:
    for line in file.readlines():
       emails.append(line.split(',')[2])

for email in emails:
    jar = cookielib.CookieJar()
    data = { 'email_ids': email }
    request = urllib2.Request(url, urllib.urlencode(data))
    response = urllib2.urlopen(request)
    jar.extract_cookies(response, request)
    
    for cookie in jar:
        cookies.append(cookie.name.strip('"') + '=' + cookie.value.strip('"'))

    count += 1
    print count

with open('cookies.txt', 'w') as file:
    json.dump(cookies, file)
