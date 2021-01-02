#In order to use this just press the green run button in the top middle part of the screen, from there just follow the instructions on the terminal on the right


import random

ans = input("Would you like to determine your class?\n(Press enter after you type something, answer yes or no)\n")

if ans == "yes":
	print("Choosing your class \'randomly\'.")
	
	choice = random.randint(1,4)

	if choice == 1:
			print("Your class is mage.")
			print("Goodbye.")
	elif choice == 2:
			print("Your class is melee.")
			print("Goodbye.")
	elif choice == 3:
			print("Your class is ranged.")
			print("Goodbye.")
	elif choice == 4:
			print("Your class is summoner.")
			print("Goodbye.")
if ans!= "yes":
	print("Goodbye.")