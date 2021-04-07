import tweepy
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

anos = 3
dias = 337

while True:
    a = api.user_timeline('RolinhaG')

    for i in a:
        if i.text == f'{anos} anos {dias} dias':
            if dias == 0:
                dias = 365
                anos -= 1
            dias -= 1
            api.update_status(f'{anos} anos {dias} dias', i.id)

    time.sleep(86000)

