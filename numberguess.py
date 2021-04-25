#made by omlet.gg/dominocgaming46
#All rights reserved
from random import randrange, randint, choice
from time import time, sleep, clock
from sys import *

guess = 0
num = 0
gameover = False
chance = 10
taken = 0
low = 0
high = 100
chancetaken = 0

def main():
	global guess, num, gameover, chance, taken, low, high
	
	print(f'======================')
	print(f'Welcome to')
	print(f'Number guessing game')
	print(f'start game? (y/n)')
	a = input()
	
	if a == 'y':
		taken = 0
		gameover = False
		print('Loading...')
		sleep(3)
		num = randint(1,100)
		print(f'Guess a number from 1 to 100')
		print(f'you have 10 chances')
		print(f'======================')
		
		while chance > 0 and not gameover:
			try:
				guess = int(input('Your Guess: '))
				
				if guess > num:
					high = guess
					print(f'Smaller! %d ~ %d (%d chances left)'%(low, high, chance))
					print(f'======================')
					chance -= 1
					continue
				
				elif guess < num:
					low = guess
					print(f'Larger! %d ~ %d (%d chances left)'%(low, high, chance))
					print(f'======================')
					chance -= 1
					continue
				
				elif guess == num:
					print(f'You win!')
					taken = 11 - chance
					print(f'Chances taken : %d'%taken)
					gameover = True
				
				elif guess <= 0 or guess > 100:
					print(f'invalid guess! between 1 and 100!')
				
			except Exception as guess:
				print('invalid guess!')
			
		if chance == 0:
			print(f'No more chances!')
			gameover = True
		
	elif a == 'n':
		print('Game stoped')
	else:
		print(f'system error')

while True:
	main()
