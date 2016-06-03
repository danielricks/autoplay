import os, sys, subprocess, nltk, re, time

# Run Parsey on a single sentence
def pos_sentence(sentence):

	# Preprocess a sentence
	sentence = sentence.replace('\n', '')
	sentence_per = sentence.replace('.', ' .')

	# Send command for sentence to be tagged
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
			pattern = '[0-9]*\t[A-Za-z.]*\t_\t[A-Z.]*\t[A-Z.]*'
			matchObj = re.search(pattern, line, re.M|re.I)
			# If the line matches traditional Parsey output for a word and a tag...
			if matchObj != None:
				match_list = matchObj.group().split('\t')
				# Add that word and tag to a string, separated by an underscore
				tagged_sentence += match_list[1] + '_' + match_list[4] + ' '
	return tagged_sentence[:-1]

