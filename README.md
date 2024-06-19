# Monty Hall Problem Simulation
This Python script simulates the Monty Hall problem, a probability puzzle based on a game show scenario.

The Monty Hall problem is as follows:
- There are 3 doors; behind one door is a car (a prize) and behind the other two are goats.
- The player selects one door.
- The host, who knows what's behind each door, opens another door revealing a goat (if possible).
- The player then has the option to stay with their initial choice or switch to the remaining unopened door.

This script runs simulations of the game show scenario to determine the probabilities of winning a car based on the player's strategy (stay or switch).

## How It Works
The script:
1. Initialises variables to count the number of wins for both strategies (`stay_door` and `switch_door`).
2. Iterates through 1000 simulations of the game:
   - Randomly assigns a car and two goats behind the three doors.
   - Randomly selects a door for the host to reveal a goat.
   - Allows the player to either stay with their initial choice or switch to the remaining door.
3. Calculates and prints the number and percentage of wins for both strategies.
4. Displays a pie chart using matplotlib to visualise the chances of winning a car with each strategy.

## Requirements
- Python 3.x
- matplotlib library (for visualising the results)

## Usage
1. Clone the repository or download the `MontyHallGame.py` file.
2. Ensure you have Python installed on your machine.
3. Install matplotlib if not already installed: `pip install matplotlib`
4. Run the script: `python MontyHallGame.py`

## Output
Upon running the script, you will see:
- A summary of the number and percentage of wins for staying and switching strategies.
- A pie chart displaying the percentage chances of winning a car for both strategies.

## Example
<div align="center">
<img width="600" alt="Screenshot 2024-06-19 at 7 09 47 PM" src="https://github.com/AdnanAliMumtaz/Monty-Hall-Game/assets/81415901/548231dd-1fa7-42e5-a8ee-fd1381d8e23c">
</div>
This chart visually represents the probabilities of winning a car with either staying or switching strategies.
