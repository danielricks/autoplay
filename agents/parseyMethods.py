import os, sys, subprocess, nltk, re, time

# Run Parsey on a single sentence
def pos_sentence(sentence):

	# Preprocess a sentence
	sentence = sentence.replace('\n', '')
	sentence_per = sentence.replace('.', ' .')

	# Send command for sentence to be tagged (using small demo script file)
	NULL = open(os.devnull, 'w')
	command = 'echo \"' + sentence + '\" | parsey/syntaxnet/smdemo.sh'
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=NULL, close_fds=True)
	process.wait()

	# Postprocess output from Parsey
	output = process.stdout.read()
	outputs = output.split('\n')

	tagged_sentence = ''
	# For every line in output...
	for line in outputs:
		# If the line actually has valuable output information...
		if not ('INFO' in line or 'I syntaxnet' in line or 'Parse:' in line or 'Input:' in line):
			pattern = '[0-9]*\\t[A-Za-z.]*\\t_\\t[A-Z.]*\\t[A-Z.]*'
			matchObj = re.search(pattern, line, re.M|re.I)
			# If the line matches traditional Parsey output for a word and a tag...
			if matchObj != None:
				match_list = matchObj.group().split('\t')
				# Add that word and tag to a string, separated by an underscore
				tagged_sentence += match_list[1] + '_' + match_list[4] + ' '
	return tagged_sentence[:-1]

# Return the words in a given sentence in order of how "important" a word is in relation to other words
def get_words_by_relative_importance(sentence):

	# Preprocess a sentence
	sentence = sentence.replace('\n', '')
	sentence_per = sentence.replace('.', ' .')

	# Send command for sentence to be tagged (using medium demo script file)
	NULL = open(os.devnull, 'w')
	command = 'echo \"' + sentence + '\" | parsey/syntaxnet/meddemo.sh'
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=NULL, close_fds=True)
	process.wait()

	# Postprocess output from Parsey
	output = process.stdout.read()
	outputs = output.split('\n')

	word_list = []
	pointer_list = [0]
	# For every line in output...
	for line in outputs:
		# If the line actually has valuable output information...
		if not ('INFO' in line or 'I syntaxnet' in line or 'Parse:' in line or 'Input:' in line):
			pattern = '[0-9]*\\t[A-Za-z.]*\\t_\\t[A-Z.]*\\t[A-Z.]*\\t_\\t[0-9]*'
			matchObj = re.search(pattern, line, re.M|re.I)
			# If the line matches traditional Parsey output for a word and a tag...
			if matchObj != None:
				match_list = matchObj.group().split('\t')
				# Add the word to a list of words
				word_list.append(match_list[1])
				# Add the index of the pointer to a list of pointers
				pointer_list.append(int(match_list[6]))

	# Create a list that will be used to count up the number of times a word is pointed to
	importance_counts = [0] * (len(word_list) + 1)
	# For every pointer...
	for pointer in pointer_list:
		current_pointer = pointer
		# Follow the pointers until it gets to the main word in the sentence (usually the verb)
		while current_pointer != 0:
			importance_counts[current_pointer] += 1
			current_pointer = pointer_list[current_pointer]

	# Cut off the first index (this is used to offset Parsey's 1-indexing scheme for pointers)
	importance_counts = importance_counts[1:]

	importance_count_to_word = {}
	# For every possible number of pointers...
	for count_index in xrange( len(importance_counts) ):
		# Add the word to a list denoted by the number of times a word is pointed to
		try:
			importance_count_to_word[ importance_counts[count_index] ].append(word_list[count_index])
		except:
			importance_count_to_word[ importance_counts[count_index] ] = []
			importance_count_to_word[ importance_counts[count_index] ].append(word_list[count_index])

	words_sorted_by_importance = []
	# For every number of pointer counts...
	for key in sorted(importance_count_to_word.iterkeys()):
		words = importance_count_to_word[key]
		# For every number of words that matched that number of pointer counts...
		for word in words:
			# Add the word to a list
			words_sorted_by_importance.append(word)

	# Reverse the list so that it's ordered from highest to lowest
	words_sorted_by_importance.reverse()

	return words_sorted_by_importance

