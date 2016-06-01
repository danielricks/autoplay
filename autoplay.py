import textplayer.textPlayer as tp
import scholar.scholar as sch
import conceptnetter.conceptNetter as cn
import agents

#t = tp.TextPlayer('zork1.z5', False)
#scholar = sch.Scholar()
#c = cn.ConceptNetter()

epochs = 1000
counter = 0

t = tp.TextPlayer('zork1.z5', False)
a1 = agents.agentDumb.AgentDumb()
current_game_text = t.run()

while (counter < epochs):
	current_game_text = a1.take_action(current_game_text)
	reward = 1
	a1.update(reward, current_game_text)

print 'Agents are done.'

