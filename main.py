import logging
import random

# Setup logging options
logging.basicConfig(level=logging.DEBUG)
logging.info('Starting up...')

# Define the targets
targets = ['head','larm','rarm','lleg','rleg']

while True:
	target = targets[random.randint(0, len(targets)-1)]
	print('Please type: ' + target)
	user_input = input()
	print('You entered: ' + user_input)

	if user_input == target:
		print('CORRECT!')
	elif user_input == 'q':
		print('QUIT')
		break
	else:
		print('WRONG')

logging.info('Finish.')
