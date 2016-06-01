import random as rand
import scholar.scholar as sch
import conceptnetter.conceptNetter as cn

class AgentDumb:

	def __init__(self, initial_epsilon, training_cycles):
		pass

	def take_action(self, game_text):
		if rand.random() < 0.4:
			if rand.random() < 0.25:
				return 'n'
			elif rand.random() < 0.5:
				return 's'
			elif rand.random() < 0.75:
				return 'e'
			else:
				return 'w'
		elif rand.random() < 0.8:
			if rand.random() < 0.25:
				return 'ne'
			elif rand.random() < 0.5:
				return 'nw'
			elif rand.random() < 0.75:
				return 'se'
			else:
				return 'sw'
		else:
			return 'climb'

	def update(self, reward, new_game_text):
		pass

