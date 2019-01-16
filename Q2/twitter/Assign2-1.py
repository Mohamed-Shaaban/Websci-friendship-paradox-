from twitter import *
import requests

consumer_key = "SaSW8NrEZRUsGfZlcOEwwJOoX"
consumer_secret = "C4K6cXR2fTVWhTDas4oJaQU4e3eUdfdrjM8qmaZmAEh1Dym2AC"
access_key = "4879994613-6ZGf0doVWQIMCTXgXLQZ72lVpwlOAhuSIwYc6UH"
access_secret = "BnmtgH0gVrMp5lni6c4sZKacW8Zqs6uCKIcBVwDVHVvQp"

auth = OAuth(access_key,access_secret,consumer_key,consumer_secret)
stream = TwitterStream(auth = auth, secure = True)


tweet_iter = stream.statuses.filter(track = "social")
i=0
ls=[]
ftext= open('weblinks.txt', 'w')
for tweet in tweet_iter:
	try:
		for url in tweet["entities"]["urls"]:
			while(i<1000):

				Website = url["expanded_url"]
				ls.insert(i,Website)
				x = ls.count(Website)
				if(x<=1): 
					ftext.write(Website + '\n')
					i+=1
					print  "th URL is : " + Website

				else:
					break
	except:
		 pass 
			
		
			#print("Crawling: {}".format(url))
			#resp = requests.get(url)
			#if resp.status_code == 200:
			#	print ("200")
ftext.close()						
	
