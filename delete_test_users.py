import json
import urllib
import urllib2

client_id = '491304740899241'
client_secret = '52c2d82565745aa4f2e203baa3867eac'

access_token = urllib.urlopen('https://graph.facebook.com/oauth/access_token?client_id=' + client_id + '&client_secret=' + client_secret + '&grant_type=client_credentials').read()
url = 'https://graph.facebook.com/' + client_id + '/accounts/test-users?' + access_token

ids = []
count = 0

def get_ids(url):
    response = json.loads(urllib.urlopen(url).read())
    for user in response['data']:
        ids.append(user['id'])
    if 'paging' in response and 'next' in response['paging']:
        get_ids(response['paging']['next'])
        
get_ids(url)

for id in ids:
    print count
    count += 1
    urllib.urlopen('https://graph.facebook.com/' + id + '?method=delete&' + access_token)
