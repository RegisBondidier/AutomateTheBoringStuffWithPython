#!/usr/bin/env python3

# coinToss.py

import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
logging.debug('guess = ' + guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
	toss = 'tails'
else:
	toss = 'heads'
logging.debug('toss = ' + toss)
if toss == guess: 
	print('You got it!') 
else: 
	print('Nope! Guess again!') 
	guess = input()
	logging.debug('guess = ' + guess)
	if toss == guess: 
		print('You got it!') 
	else: 
		print('Nope. You are really bad at this game.')




