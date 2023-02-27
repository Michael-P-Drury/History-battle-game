from troops_dict import *

money = 1000
troops = [archer, infantry]
f = open("save.txt", "w")
for troop in troops:
    f.write(troop['id'])
    f.write(' ')
f.write('\n')
f.write(str(money))
f.close()