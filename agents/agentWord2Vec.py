import random as rand
import parseyMethods
import scholar.scholar as s
import conceptnetter.conceptNetter as cn

class AgentWord2Vec:

	# Sets all initial learning variables of behavior parameters
	def __init__(self, initial_epsilon, training_cycles):
		pass

	# Prepares the agent for a new round of training (i.e. prepares to restart the game, but does not erase any learned knowledge)
	def refresh(self):
		self.total_points_earned = 0

	# Yes, this is a very stupid agent.
	def take_action(self, game_text, evaluation_flag = False):
		movement_type = rand.random()
		if movement_type < 0.4:
			direction = rand.random()
			if direction < 0.25:
				return 'n'
			elif direction < 0.5:
				return 's'
			elif direction < 0.75:
				return 'e'
			else:
				return 'w'
		elif movement_type < 0.8:
			direction = rand.random()
			if direction < 0.25:
				return 'ne'
			elif direction < 0.5:
				return 'nw'
			elif direction < 0.75:
				return 'se'
			else:
				return 'sw'
		else:
			return 'climb'

	# If overwritten in a derived class, this function should still be sure to update total_points_earned
	def update(self, reward, new_game_text):
		self.total_points_earned += reward

	# Generates a 'status update' which will be printed to the screen by autoplay.py
	def get_status(self):
		return 'TOTAL POINTS = ' + str(self.total_points_earned)

	# Useful for writing date files that track obtained reward over time
	def get_total_points_earned():
		return self.total_points_earned

	# Returns a string containing data such as learning rate, loss function, and various hyperparameters which can then be written to a data file
	# This is very helpful when you want to repeat a learning run, but can't remember which hyperparameters you used the first time.
	def get_learning_parameters(filename):
		pass

	# Returns a sentence that has been tagged by Parsey McParseface.
	def get_tagged(self, text):
		text = text.replace('!', '.').replace('?', '.').replace('\'', '')
		if '.' in text:
			sentences = text.split('.')
		else:
			sentences = text
		tagged_sentences = ''
		for sentence in sentences:
			tagged_sentences += parseyMethods.pos_sentence(sentence) + ' '
		return tagged_sentences
