# --------------------------------------------------------------------------------
# : imports
from random import randint

# --------------------------------------------------------------------------------
# : color code
RED = '\033[91m'
GRE = '\033[92m'
YEL = '\033[93m'
BLU = '\033[94m'
MAG = '\033[95m'
CYA = '\033[96m'
RES = '\033[0m'
BOL = '\033[1m'
UND = '\033[4m'

# --------------------------------------------------------------------------------
# : main
ans = randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.\nGood luck!\n")
idx = 1
while True:
	print(
		f"{BLU}{BOL}{UND}[Guess]{RES}",
		f"{YEL}{BOL}[Guess!]{RES} ",
		f"What's your guess between 1 and 99?\n",
		f"                 : {CYA}",
		end=""
	)
	guess = input()
	print(
		f"{RES}",
		end=""
	)

	if guess == 'exit':
		print(
			f"{BLU}{BOL}{UND}[Guess]{RES}",
			f"{GRE}{BOL}[The End]{RES}",
			f"Good Bye!"
		)
		break
	if not guess.isnumeric():
		print(
			f"{BLU}{BOL}{UND}[Guess]{RES}",
			f"{RED}{BOL}[Failure]{RES}",
			f"Hmm, That seems non-integer value. Try again."
		)
	else:
		if int(guess) == ans:
			if idx == 1:
				print(
					f"{BLU}{BOL}{UND}[Guess]{RES}",
					f"{GRE}{BOL}[Success]{RES}",
					f"{UND}The answer to the ultimate question of life, the universe and everything is {MAG}{BOL}{ans}{RES}",
					f"\n",
					f"               ",
					f"{CYA}{BOL}Congratulations!{RES} You got it on your first try!"
				)
				break
			else:
				print(
					f"{BLU}{BOL}{UND}[Guess]{RES}",
					f"{GRE}{BOL}[Success]{RES}",
					f"{CYA}{BOL}Congratulations!{RES} You've got it in {idx} tries!"
				)
				break
		elif int(guess) < ans:
			print(
				f"{BLU}{BOL}{UND}[Guess]{RES}",
				f"{RED}{BOL}[Failure]{RES}",
				f"That too low."
			)
		elif int(guess) > ans:
			print(
				f"{BLU}{BOL}{UND}[Guess]{RES}",
				f"{RED}{BOL}[Failure]{RES}",
				f"That too high."
			)
	idx += 1
