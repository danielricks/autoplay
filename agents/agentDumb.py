import random as rand
import scholar.scholar as sch
import conceptnetter.conceptNetter as cn

class AgentDumb:

	def __init__(self, initial_epsilon, training_cycles):
		pass

	def take_action(self, game_text):
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
		pass

