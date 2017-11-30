# -*- coding: utf-8 -*-
import tweepy, time, sys
 
class Bot:
	def __init__(self):
		self.CONSUMER_KEY = 'bD2H43VoGQYGnMyTeXxEhZsko'
		self.CONSUMER_SECRET = 'bjJqI8tQvyYDvrYz8P1nXWcVPpu3Zybq76YQcwqM7iG0c6gw92'
		self.ACCESS_KEY = '935835875547676672-33ibHPxXykKIUzR8Vrwi07AMsXoCKHj'
		self.ACCESS_SECRET = 'R25wpoon7SBES3GTmj9lJyt7gFYdD3bJylLeVob7URJIn'
		self.api = self.authenticate()

	
	def authenticate(self):
		auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
		auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
		api = tweepy.API(auth)

		try:
			api.verify_credentials();
		except:
			print('El bot no se pudo autenticar, por favor comprueba tus datos de acceso.')
		else:
			print('El bot se pudo conectar.')
			return api

	def txtTwittear(self):
		argfile = str('r.txt')
		filename = open(argfile,'r')
		f = filename.readlines()
		filename.close()
		for line in f:
		    print("[+] Tweeteando...")
		    self.api.update_status(status = line)
		    print("[+] Tweet: ", line)
		    time.sleep(10)
	def followAll(self):
		for follower in tweepy.Cursor(api.followers).items():
    		follower.follow()

twitter_bot = Bot()
twitter_bot.txtTwittear()
