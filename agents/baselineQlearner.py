#standard Q-learning agent
#(Not very bright, but useful for baseline analysis.)

#STATE REPRESENTATION: elementary hash of game text
#acquired via 'look' commands

#ACTION SPACE: a set of permissible verbs and
#objects as read from user-defined input files

#Q-VALUES: learns joint Q-values representing all possible
#combinations of verbs and objects for a given state.

#EXPLORATION: Epsilon-greedy

import agentBaseClass
import random as rand
import numpy as np
import re


class BaselineQlearner(agentBaseClass.AgentBaseClass):

	def read_verbs(self, filename = "Zork_verbs.txt"):
		file = open(filename)
		self.verb_list=[]
		for line in file:
			self.verb_list.append(line.rstrip('\n').rstrip('\r'))
		file.close()

	def read_objects(self, filename = "Zork_objects.txt"):
		file = open(filename)
		self.object_list=[]
		for line in file:
			self.object_list.append(line.rstrip('\n').rstrip('\r'))
		file.close()

	def __init__(self, initial_epsilon, training_cycles):
		self.ALPHA = 0.1
		self.GAMMA = 0.95
		self.EPSILON = initial_epsilon
		self.read_verbs()
		self.read_objects()
		print self.verb_list
		print self.object_list
		self.Qvalues = np.random.random((len(self.verb_list), len(self.object_list)))
		print self.Qvalues

	def refresh(self):
		agentBaseClass.AgentBaseClass.refresh(self)

	def take_action(self, game_text, evaluation_flag = False):
		movement_type = rand.random()
		if movement_type < 0.2:
			direction = rand.random()
			if direction < 0.25:
				return 'n'
			elif direction < 0.5:
				return 's'
			elif direction < 0.75:
				return 'e'
			else:
				return 'w'
		elif movement_type < 0.4:
			direction = rand.random()
			if direction < 0.25:
				return 'ne'
			elif direction < 0.5:
				return 'nw'
			elif direction < 0.75:
				return 'se'
			else:
				return 'sw'
		elif movement_type < 0.6:
			action = rand.random()
			if action < 0.25:
				return 'open window'
			elif action < 0.5:
				return 'enter window'
			elif action < 0.75:
				return 'move rug'
			else:
				return 'get egg'
		else:
			return 'climb'

	def update(self, reward, new_game_text):
		agentBaseClass.AgentBaseClass.update(self, reward, new_game_text)

	def get_learning_parameters(filename):
		pass
	

