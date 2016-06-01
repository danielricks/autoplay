import random as rand
import scholar.scholar as sch
import conceptnetter.conceptNetter as cn

class AgentDumb:

	def __init__(self, initial_epsilon, training_cycles):
		pass

	def take_action(self, game_text):
		if rand.random() < 0.5:
			if rand.random() < 0.5:
				return 'n'
			else:
				return 's'
		else:
			if rand.random() < 0.5:
				return 'e'
			else:
				return 'w'

	def update(self, reward, new_game_text):
		pass

