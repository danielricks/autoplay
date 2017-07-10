import random as rand
import scholar.scholar as sch
import os, random, copy, re
import cPickle as pickle
import nltk

class AgentWord2Vec:

	# Sets all initial learning variables of behavior parameters
	def __init__(self, initial_epsilon, training_cycles):

		# GLOBAL VARIABLES
		# Used for making Word2Vec queries
		self.s = sch.Scholar()
		# Used for saving noun:verb lists in memory to limit the number of Word2Vec queries
		self.verb_dict = {}
		# Used for continuing to work within a game_text when the last command(s) didn't give you good output
		self.last_good_game_text = ''
		# Refreshes the debug log file to be empty at the beginning of a game run
		self.debug = True
		if self.debug:
			open('debugAgentWord2Vec.txt', 'w').close()
			open('bad_commands.txt', 'w').close()
#		open('good_commands.txt', 'w').close()
		# Used to guarantee that the same command won't be run twice in a row
		self.last_command = ''
		
		# Used to keep track of the commands that can be run in a given area (Resets when a unique output is encountered)
		self.possible_commands = []
		
		# Used for guaranteeing that commands that have failed in the past will not be executed again
		if os.path.exists('word_stale_dict.w2v') and os.path.exists('word_used_commands.w2v'):
			self.stale_output, self.used_commands = self.load_memories()
		else:
			# Used for keeping track of unique outputs and removing the possibility of re-running commands that lead to non-unique outputs
			self.stale_output = {}
			self.used_commands = {}

		# PARAMETERS
		# Used to set the number of characters in the game_text that are unique
		# So ( I don't know the word "shove".) turns to ( I don't know the wo)
		self.OUTPUT_CHARACTER_COUNT = 20
		# Used to set the number of commands that lead to an output before it's not considered 'unique'
		self.ARBITRARY_COMMAND_CONTROL_COUNT = 30
		# Used as verbs for every noun in command generation
		self.STANDARD_VERBS = ['open', 'take']
		# Used to set the number of commands returned when Word2Vec is queried.
		# (Make sure that this number is smaller than self.ARBITRARY_COMMAND_CONTROL_COUNT)
		# Also keep in mind that the first x verbs are the standard verbs, and are included in this number
		self.COMMANDS_RETURNED_COUNT = 15


	# Prepares the agent for a new round of training (i.e. prepares to restart the game, but does not erase any learned knowledge)
	def refresh(self):
		self.total_points_earned = 0


	# This is a not-so-stupid, now very complicated agent.
	def take_action(self, game_text, evaluation_flag = False):

		# Take note of output given command
		game_text_clip = game_text[:self.OUTPUT_CHARACTER_COUNT]
		self.track_output(game_text_clip)

		# If the output is bad... (if the game is just beginning or if the output to command ratio is 1:20 ish)
		if self.last_good_game_text != '' and len(self.stale_output[game_text_clip]) >= self.ARBITRARY_COMMAND_CONTROL_COUNT:

			# We used to just append to a list, now we take advantage of Python's dictionary's use of hashing
			try:
				self.used_commands[self.last_command] += 1
			except:
				self.used_commands[self.last_command] = 0
				if self.debug:
					with open('bad_commands.txt', 'a') as f:
						f.write(self.last_command + '\n')

			# If there are still commands to be run...
			if len(self.possible_commands) > 0:
				# Take the first command in the list...
				current_command = self.possible_commands[0]
				# Remove it from the list
				del self.possible_commands[0]
				# Save the command
				self.last_command = current_command
				self.write_to_file('Running command: ' + current_command + ' out of ' + str(len(self.possible_commands) + 1) + '\n')
				# Return the command
				return current_command
		else:
#			with open('good_commands.txt', 'a') as f:
#				f.write(self.last_command + '\n')
			# If the output is good and we need commands to run...
			self.write_to_file(':::Relearning commands:::' + '\n')
			# Part-of-speech tag the game_text
			tagged_game_text = self.get_tagged_text(game_text)

			# Get commands from the tagged_game_text (nouns and noun phrases)
			local_commands = self.get_commands(tagged_game_text)

			# Shuffle the list of commands to add pseudo-randomness to the process
			list_commands = list(local_commands)
			random.shuffle(list_commands)
			self.possible_commands = list_commands

			# If there are now commands to run...
			if len(self.possible_commands) > 0:
				# Take the first command in the list...
				current_command = self.possible_commands[0]
				del self.possible_commands[0]
				# If that exact command was not run last time...
				if current_command != self.last_command:
					# Save the command and game_text
					self.last_command = current_command
					self.last_good_game_text = game_text
					self.write_to_file('Running command: ' + current_command + ' out of ' + str(len(self.possible_commands) + 1) + '\n')
					# Return the command
					return current_command
				else: #(else break and run a random movement instead)
					self.write_to_file(current_command + ' is the same as ' + self.last_command + '\n')

		# This should run when (the game_text is bad and there are no possible commands to be run) and when 
		# (the game_text is good but it can't find any valid commands to run)
		return self.get_random_movement_command()


	# Returns the list of commands given a list of identified nouns or noun phrases
	def get_commands(self, tagged_game_text):
		self.write_to_file("Tagged_game_text: " + str(tagged_game_text) + '\n')

		single_tagged_nouns = re.findall(r'[A-Za-z]+_NN[S]*', tagged_game_text)
		compound_tagged_nouns = re.findall(r'[A-Za-z]+_[J|N]+ [A-Za-z]+_NN[S]*', tagged_game_text)
		all_tagged_nouns = single_tagged_nouns + compound_tagged_nouns

		# Take out duplicates (remove 'door_NN' when 'trap_NN door_NN' is avilable)
		# This is no longer necessary ('take large egg' doesn't work, while 'take egg' does)
		if False:
			# For every noun phrase...
			for compound_tagged_noun in compound_tagged_nouns:
				second_word_and_tag = compound_tagged_noun.split()[1]
				# For every noun...
				for single_tagged_noun in single_tagged_nouns:
					# If the second word in the noun phrase (guaranteed to be a noun) and the noun are the same...
					if single_tagged_noun.lower() == second_word_and_tag.lower():
						# Remove the single noun from the list
						if single_tagged_noun in all_tagged_nouns:
							all_tagged_nouns.remove(single_tagged_noun)

		score = []
		tagged_words_in_game_text = tagged_game_text.split()
		for word_index in xrange(len(tagged_words_in_game_text)):
			current_tagged_word = tagged_words_in_game_text[word_index]
			other_tagged_words = []
			for inner_word_index in xrange(len(tagged_words_in_game_text)):
				if inner_word_index != word_index:
					other_tagged_words.append(tagged_words_in_game_text[inner_word_index])
			current_score = 0
			
			score.append(current_score)

		# If there are nouns in the list...
		if len(all_tagged_nouns) > 0:
			local_commands = set()
			# For every tagged noun (or noun phrase)
			for tagged_noun in all_tagged_nouns:
				# If it's actually a noun phrase (ex. 'wooden_JJ table_NN' or 'trap_NN door_NN')
				if ' ' in tagged_noun:
					first_word_and_tag = tagged_noun.split()[0].split('_')
					second_word_and_tag = tagged_noun.split()[1].split('_')
					# If the tag of the second word in the noun phrase is actually 'NN' (and not 'NNS', 'NNP')
					if second_word_and_tag[1] == 'NN' or second_word_and_tag[1] == 'NNS':
						# Ensure that every word is lowercase
						lower_tagged_noun_list = [first_word_and_tag[0].lower() + '_' + first_word_and_tag[1], second_word_and_tag[0].lower() + '_' + second_word_and_tag[1]]
						# Get commands for the phrase
						noun_commands = self.get_commands_for_noun(lower_tagged_noun_list)
						# For every command, add it to the list
						for noun_command in noun_commands:
							local_commands.add(noun_command)
				else:
					# For every noun (not noun phrases) (ex. 'door_NN')
					if tagged_noun.split('_')[1] == 'NN':
						# Ensure that every word is lowercase
						lower_tagged_noun_list = [tagged_noun.split('_')[0].lower() + '_NN']
						# Get commands for the noun
						noun_commands = self.get_commands_for_noun(lower_tagged_noun_list)
						# For every command, add it to the list
						for noun_command in noun_commands:
							local_commands.add(noun_command)
			return local_commands
		return []


	# Handles whether output should be considered 'bad' or not by keeping track of commands to output
	def track_output(self, game_text_clip):
		# The {output:command} is saved in a dictionary, so that we can track how many inputs return which outputs.
		# If there are tons of commands that return the same output, those particular commands are not worth executing.
		# We track them here.
		# Side note: We only track the first 20 chararacters in the output so that we can catch all
		# the "I don't know the word [word]" phrases as single outputs.
		try:
			if len(self.stale_output[game_text_clip]) < self.ARBITRARY_COMMAND_CONTROL_COUNT:
				self.stale_output[game_text_clip].add(self.last_command)
		except:
			self.stale_output[game_text_clip] = set()
			if len(self.stale_output[game_text_clip]) < self.ARBITRARY_COMMAND_CONTROL_COUNT:
				self.stale_output[game_text_clip].add(self.last_command)

		# Write the stale output to commands dictionary to the file
		self.write_to_file('\t' + str(self.stale_output) + '\n')


	# Writes to the debug file
	def write_to_file(self, text):
		if self.debug:
			with open('debugAgentWord2Vec.txt', 'a') as f:
				f.write(text)


	# Return a random movement command (or 'look')
	def get_random_movement_command(self):
		direction = rand.random()
		if direction < 0.10:
			return 'n'
		elif direction < 0.20:
			return 's'
		elif direction < 0.30:
			return 'e'
		elif direction < 0.40:
			return 'w'
		elif direction < 0.50:
			return 'ne'
		elif direction < 0.60:
			return 'nw'
		elif direction < 0.70:
			return 'se'
		elif direction < 0.80:
			return 'sw'
		elif direction < 0.85:
			return 'u'
		elif direction < 0.90:
			return 'd'
		elif direction < 0.95:
			return 'look'
		else:
			return 'i'

	# Return a list of commands for a given list of tagged words ('door_NN', 'trap_NN door_NN', 'wooden_JJ door_NN', etc.)
	def get_commands_for_noun(self, tagged_list):
		# Get a list of verbs for the noun
		tagged_noun = tagged_list[-1]
		verbs = self.get_verbs_for_noun(tagged_noun)

		# Add every verb plus the noun to the command list
		commands = []
		noun = tagged_noun.split('_')[0]
		for verb in verbs:
			# Add a describing word if it exists
			if len(tagged_list) > 1:
				command = verb + ' ' + tagged_list[0].split('_')[0] + ' ' + noun
			else:
				command = verb + ' ' + noun
			# Take advantage of Python's hashing to quickly check whether a command is valid
			try:
				self.used_commands[command] += 1
			except:
				commands.append(command)

		self.write_to_file(str(tagged_list) + '\t' + ",".join(commands) + '\n')

		# Return the list of commands (only a specified number are returned)
		return commands[:self.COMMANDS_RETURNED_COUNT]


	# Returns a list of verbs for a given tagged noun
	def get_verbs_for_noun(self, tagged_noun):
		# Begin with a list of standard verbs
		verbs = copy.deepcopy(self.STANDARD_VERBS)
		# Separate the noun from the list and its tag
		noun = tagged_noun.split('_')[0]
		# If the noun is too short to be a word, return nothing (this happened in the case of 'c' and 't')
		if len(noun) < 2:
			return []

		# Get the list of verbs for a noun, whether stored in memory...
		if tagged_noun in self.verb_dict.keys():
			tagged_verbs = self.verb_dict[tagged_noun]
		else:
			# Or from Word2Vec directly
			if tagged_noun.split('_')[1] == '_NNS':
				tagged_verbs = self.s.get_verbs_plural(noun, 20)
#				with open('good_commands.txt', 'a') as f:
#					f.write(self.last_command + '\t' + str(tagged_verbs) + '\n')
			else:
				tagged_verbs = self.s.get_verbs(noun, 20)
			self.write_to_file(str(tagged_verbs) + '\n')
			self.verb_dict[tagged_noun] = tagged_verbs

		# Add every verb (without its tag) to a list and return it
		for tagged_verb in tagged_verbs:
			verb = tagged_verb.split('_')[0]
			verbs.append(verb)
		return verbs


	# Save agent progress to a pickle file
	def write_memories(self):
		pickle.dump(self.stale_output, open('word_stale_dict.w2v', 'wb'))
		pickle.dump(self.used_commands, open('word_used_commands.w2v', 'wb'))


	# Load agent progress from a pickle file
	def load_memories(self):
		return pickle.load(open('word_stale_dict.w2v', 'rb')), pickle.load(open('word_used_commands.w2v', 'rb'))


	# If overwritten in a derived class, this function should still be sure to update total_points_earned
	def update(self, reward, new_game_text):
		self.total_points_earned += reward


	# Generates a 'status update' which will be printed to the screen by autoplay.py
	def get_status(self):
		return 'TOTAL POINTS = ' + str(self.total_points_earned)


	# Useful for writing date files that track obtained reward over time
	def get_total_points_earned():
		return self.total_points_earned


	# Returns a string containing data such as learning rate, loss function, and various hyperparameters which can then be written to a data file.
	# This is very helpful when you want to repeat a learning run, but can't remember which hyperparameters you used the first time.
	def get_learning_parameters(filename):
		pass


	# Returns a sentence that has been tagged by NLTK.
	def get_tagged_text(self, text):
		tokenized_text = nltk.word_tokenize(text)
		pos_tagged_text = nltk.pos_tag(text)
		formatted_tagged_text = []
		for tuple_word in pos_tagged_text:
			formatted_tagged_text.append(tuple_word[0] + '_' + tuple_word[1])
		return formatted_tagged_text

