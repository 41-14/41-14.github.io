import json
import sys
import urllib
import urlparse
import oauth2 as oauth
import pandas

consumer_key = 'OQUXepRijCnpWyuAnmcm'
consumer_secret = 'KByTrRvGfBhzcoLqbrKfLJjGPXPNclIf'
request_token_url = 'https://api.discogs.com/oauth/request_token'
authorize_url = 'https://www.discogs.com/oauth/authorize'
access_token_url = 'https://api.discogs.com/oauth/access_token'
user_agent = '41-14/dashboardcollection'


consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)
resp, content = client.request(request_token_url, 'POST', headers={'User-Agent': user_agent})


if resp['status'] != '200':
    sys.exit('Invalid response {0}.'.format(resp['status']))

request_token = dict(urlparse.parse_qsl(content))

print 'Please browse to the following URL {0}?oauth_token={1}'.format(
        authorize_url, request_token['oauth_token'])

oauth_verifier = raw_input('Verification code :')


token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)

resp, content = client.request(access_token_url, 'POST', headers={'User-Agent': user_agent})


access_token = dict(urlparse.parse_qsl(content))
token = oauth.Token(key=access_token['oauth_token'],
        secret=access_token['oauth_token_secret'])
client = oauth.Client(consumer, token)

csvpath = raw_input('CSV Path: ')
df = pandas.read_csv(r"{}".format(csvpath))
ids = df['release_id'].values.tolist()

for i in ids:
    resp, content = client.request('https://api.discogs.com/releases/{}'.format(i),
            headers={'User-Agent': user_agent})

    if resp['status'] != '200':
        sys.exit('Unable to fetch release {}'.format(i))

    release = json.loads(content)
    image = release['images'][0]['uri']


    try:
        urllib.urlretrieve(image, image.split('/')[-1])
    except:
        sys.exit('Unable to download image {0}'.format(image))

