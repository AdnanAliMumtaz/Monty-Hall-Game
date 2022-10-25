import random
 
stay_door = 0
switch_door = 0
#"stay" and "switch" both variables define the choice of a player whether it is going to stay on the door after the host shows the goat door or they want to switch to another door.
 
for monty in range(1000):
    cargoatgoat = [1,0,0]
    random.shuffle(cargoatgoat)
 
    host = random.randrange(3)
 
    indegenouse_choice = cargoatgoat[host]
 
    del(cargoatgoat[host])
 
    Value = 0
    for monty in cargoatgoat:
        if monty == 0:
            del(cargoatgoat[Value])
            break
        Value+=1
 
    if indegenouse_choice ==1:
        stay_door+=1
 
    if cargoatgoat[0] == 1:
        switch_door+=1

Percentage_stay = "{:.2f}".format(stay_door/1000 * 100),"%"
Percentage_switch = "{:.2f}".format(switch_door/1000 * 100),"%"
print("Mondy Hall Games stimulated for thousand times")
print("**************************************************************")
print("Numbers of winning games if you choose to stay on the door =","[", stay_door,"]",)
print("Percentage of winning if you chose to stay on the door =", Percentage_stay)
print("---------------------------------------------------------")
print("Numbers of winning game if you chose to switch door =","[", switch_door,"]")
print("Percentage of winning if you chose to switch door =", Percentage_switch)
print("----------------------------------------------------------")

#----------------------------------

import matplotlib.pyplot as plt

print("Chances of Winning a Car")
 
labels = ['Stay Door Strategy', 'Switch Door Strategy']
quantity = [stay_door, switch_door]

colors = ['gold', 'yellowgreen']

plt.pie(quantity, labels=labels, colors=colors, autopct='%1.1f%%', 
    shadow=True, startangle=100)

plt.axis('equal')

plt.show()
