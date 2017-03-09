import sys, os, time
import textplayer.textPlayer as tp

if len(sys.argv) < 2:
	print 'Needs more parameters. Try \'python autoplay.py zork1.z5\'.'
	print 'Available games include: ',
	game_directory = os.listdir('textplayer/games')
	for game in sorted(game_directory):
		print game,
	sys.exit()
else:
	print 'Running ' + sys.argv[1]

current_game_file = sys.argv[1]
t = tp.TextPlayer(current_game_file)

current_game_text = t.run()
print current_game_text
current_command = raw_input('>')

while current_command != 'exit':
	current_game_text = t.execute_command(current_command)
	print current_game_text
	if t.get_score() != None:
		score, possible_score = t.get_score()
		print 'Current score is: ', score
	current_command = raw_input('>')

