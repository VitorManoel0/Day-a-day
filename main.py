import tweepy

ACCESS_KEY = '2641570857-uDFJc7AIZLVTBobgHPzxI61J1Cnx7ZfBXmZxBnq'
ACCESS_SECRET = 'PuR7u8rTcUJlvZTR9PvCNvjiGiAggNonSNpLiT7NjIa2I'
CONSUMER_KEY = '3GoPPYdVnEj3mqrBmQURObsmk'
CONSUMER_SECRET = '8joQWrNZtJX05qBi3nmyNZwy7VCZ4p7Ezbxgi4h62VWDAIAUed'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status('FUNFO FML')