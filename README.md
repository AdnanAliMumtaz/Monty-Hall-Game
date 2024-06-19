
# Monty Hall Game

This is a Python program that simulates the Monty Hall problem. The Monty Hall problem is a probability puzzle that is named after the host of the American television game show "Let's Make a Deal," Monty Hall. The problem is as follows:

You are a contestant on a game show. There are three doors: behind one door is a valuable prize (e.g., a car), and behind the other two doors are less valuable prizes (e.g., goats). You are asked to choose one door.

After you make your initial choice, the host, who knows what is behind each door, opens one of the other two doors to reveal a less valuable prize (a goat). At this point, there are two unopened doors: the one you initially chose and the other unopened door.

Now, the host gives you a choice: you can either stick with your original choice or switch to the other unopened door. The question is, what is the best strategy to maximize your chances of winning the valuable prize?

This program simulates the Monty Hall problem by running a specified number of iterations (in this case, 1000). In each iteration, the program randomly assigns the valuable prize behind one door and the goats behind the other doors. Then, the host randomly chooses one of the doors to open, revealing a goat. The program keeps track of the number of times the player wins if they stick with their initial choice (the "stay" strategy) and the number of times they win if they switch doors (the "switch" strategy).

## Explanation

1. The program starts by importing the required modules: random for generating random numbers and matplotlib.pyplot for creating the pie chart.
2. The variables stay_door and switch_door are initialized to 0, which will keep track of the number of wins for the "stay" and "switch" strategies, respectively.
3. The program enters a loop that simulates the Monty Hall problem for a specified number of iterations (1000 in this case).
4. In each iteration, a list cargoatgoat is created with 1 representing the valuable prize (car) and 0 representing the goats.
5. The list is shuffled randomly to assign the locations of the prize and goats behind the doors.
6. The host randomly selects one of the doors to open and stores its index in the variable host.
7. The player's initial choice is stored in the variable indegenouse_choice, which represents the value behind the door chosen by the player.
8. The list cargoatgoat is modified by removing the element corresponding to the host's choice.
9. The loop iterates through the remaining elements of cargoatgoat to find the index of the remaining goat.
10. If the player's initial choice was the valuable prize (1), it increments the stay_door counter.
11. If the remaining element in cargoatgoat is the valuable prize (1), it increments the switch_door counter.
12. After the iterations, the program calculates the percentages of winning for both the "stay" and "switch" strategies.
13. The program prints the number of winning games and the percentage of winning for each strategy.
14. Finally, a pie chart is created using matplotlib.pyplot to visualize the chances of winning a car for each strategy.

## Usage 

1. Ensure you have Python installed on your system.
2. Save the code in a Python file with a .py extension, for example, monty_hall.py.
3. Run the program using the command python monty_hall.py.
4. The program will simulate the Monty Hall problem for 1000 iterations.
5. The output will display the number of winning games and the percentage of winning for both the "stay" and "switch" strategies.
6. Additionally, a pie chart will be displayed to visualize the chances of winning a car for each strategy.



## Authors

- [@AdnanAliMumtaz](https://www.github.com/AdnanAliMumtaz)


