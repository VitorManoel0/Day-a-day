import tweepy
import time

ACCESS_KEY = '2641570857-uDFJc7AIZLVTBobgHPzxI61J1Cnx7ZfBXmZxBnq'
ACCESS_SECRET = 'PuR7u8rTcUJlvZTR9PvCNvjiGiAggNonSNpLiT7NjIa2I'
CONSUMER_KEY = '3GoPPYdVnEj3mqrBmQURObsmk'
CONSUMER_SECRET = '8joQWrNZtJX05qBi3nmyNZwy7VCZ4p7Ezbxgi4h62VWDAIAUed'

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

