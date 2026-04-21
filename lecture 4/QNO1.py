import random

# Ask the user how many dice to roll
num_dice = int(input("How many dice do you want to roll? "))

total = 0

# Roll the dice using a for loop
for i in range(num_dice):
    roll = random.randint(1, 6)  # roll one die (1–6)
    total = total + roll

# Print the total sum
print("The total is:", total)