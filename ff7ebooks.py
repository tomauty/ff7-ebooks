import twitter
import random
import os
#log into the API
api = twitter.Api(consumer_key = os.environ['CONSUMER_KEY'],
		  consumer_secret=os.environ['CONSUMER_SECRET'],
		  access_token_key=os.environ['ACCESS_TOKEN_KEY'],
		  access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])

#read in quotes
quotes 	= open('ff7quotes.txt','r').read().splitlines()
random.seed(None)

#choose quotes at random
status	= ""
while len(status) > 140 or len(status) <= 5:
	index	= random.randint(0, len(quotes) - 1)
	status	= quotes[index].rstrip()
	#Concatenate next line if quote continues on next line
	if len(status) is 0:
		status = "NULL"
	if status[-1].islower():
		status = status + " " + quotes[index+1]
	if status[0].islower():
		status = quotes[index-1] + " " + status
api.PostUpdate(status)
