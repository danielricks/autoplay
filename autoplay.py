import sys, os, time
import textplayer.textPlayer as tp
import agents.agentQuantizeActionSpace as ac

from multiprocessing import Process, Lock


# Describes an agents life span
def agent_action_loop(output_lock, a, t):

	counter = 0
	last_score = 0

	# A game is started
	current_game_text = t.run()

	# While training continues...
	while (counter < training_cycles):

		# Get the current command from the agent, given the current game text
		current_command = a.take_action(current_game_text, False)

		# New game text is acquired after executing the command
		current_game_text = t.execute_command(current_command)

		print_output(output_lock, str(counter) + ' ' + str(a) + ' ' + current_command + ' ' + current_game_text)

		# The agent is rewarded
		if t.get_score() != None:
			score, possible_score = t.get_score()
			reward = score - last_score
			last_score = score
			a.update(reward, current_game_text)

		counter += 1

	a.write_memories()

# Print standard output using a lock
def print_output(lock, text):
	lock.acquire()
	try:
		print(text)
	finally:
		lock.release()

# A lock is created for managing output
output_lock = Lock()

number_agents = 1
current_game_file = 'zork1.z5'

# Agents are created and assigned a process
for x in xrange(number_agents):
	initial_epsilon = 3
	training_cycles = 10000

	# An agent is created and a game is initialized
	a = ac.AgentQuantizeActionSpace(initial_epsilon, training_cycles)
	a.refresh()
	t = tp.TextPlayer(current_game_file)

	# Each agent gets it's own background process
	Process(target=agent_action_loop, args=(output_lock, a, t)).start()

