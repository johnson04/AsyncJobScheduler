#!/usr/bin/python
"""
Author		: Chuan Zhang
Date		: March 2016
Description	: This toy webservice is used to demonstrate how to use Flask + redis + celery to build a webservice to 
			: implement asynchronous tasks/jobs scheduling
"""
import random, os
random = random.SystemRandom()

def get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
	"""
	Returns a security generated random string.
	The default length of 12 with the a-z, A-Z, 0-9 character set returns
	a 71-bit value. log_2((26+26+10)^12) =~ 71 bits.
	
	Taken from the django.utils.crypto module.
	"""
	return ''.join(random.choice(allowed_chars) for i in range(length))

def get_secret_key():
	"""
	Create a random secret key.
	Taken from the Django project.
	"""
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
	return get_random_string(50, chars)
