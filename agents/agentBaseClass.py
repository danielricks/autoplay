import random as rand

class AgentBaseClass:

	def __init__(self, initial_epsilon, training_cycles):
		#sets all initial learning variables
		#or behavior parameters
		pass

	def refresh(self):
		#prepares the agent for a new round of training
		#(i.e. prepares to restart the game, but does not
		#erase any learned knowledge)
		self.total_points_earned = 0

	def take_action(self, game_text, evaluation_flag = False):
		#(Yes, this is a very stupid agent.)
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

	def update(self, reward, new_game_text):
		#if overwritten in a derived class, this 
		#function should still be sure to update
		#total_points_earned
		self.total_points_earned += reward

	def get_status(self):
		#generates a 'status update' which will be
		#printed to the screen by autoplay.py
		return 'TOTAL POINTS = ' + str(self.total_points_earned)

	def get_total_points_earned():
		#useful for writing data files that track 
		#obtained reward over time
		return self.total_points_earned

	def get_learning_parameters(filename):
		#returns a string containing data such as learning rate,
		#loss function, and various hyperparameters which can 
		#then be written to a data file
	
		#(This is very helpful when you want to repeat a 
		#learning run, but can't remember which hyperparameters
		#you used the first time.)
		pass
