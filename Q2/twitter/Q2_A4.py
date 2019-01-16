import oauth, tweepy, sys, locale, threading 
from time import localtime, strftime, sleep

def init(): 
    global api
consumer_key = "SaSW8NrEZRUsGfZlcOEwwJOoX"
consumer_secret = "C4K6cXR2fTVWhTDas4oJaQU4e3eUdfdrjM8qmaZmAEh1Dym2AC"
access_key = "4879994613-6ZGf0doVWQIMCTXgXLQZ72lVpwlOAhuSIwYc6UH"
access_secret = "BnmtgH0gVrMp5lni6c4sZKacW8Zqs6uCKIcBVwDVHVvQp"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    user = api.get_user('Shaaban_Migo')
    print user.screen_name
    print user.followers_count