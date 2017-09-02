print("Game Paper, Rock, Scissors, made by Dimitris Zafiris")
import time
loose = ("Computer wins :( ")
win = ("You Win :) ")
lives = 3
score = 0
drew = 0
computer_lives = 5
password_list = []
while True:
	print("Please fill in your username and password.")
	username = input("Please enter your username:  ")
	password = input("Please enter your password:  ")
	searchfile = open("accounts.txt","r")
	for line in searchfile:
		password_list.append(line.strip())
		if username and password in password_list:
				print("Welcome ",username)
				time.sleep(0.5)
				print("Loading...")
				time.sleep(1.5)
				print("Loading...")
				time.sleep(0.5)
				start_menu = """
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Let's have a quick look at game's rules.
You start with 3 lives.
If you win you get a extra live.
If you loose you loose a live.
If you draw the lives stay the same.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
To see a list of rules type "Rules".
You could see you "Lives, "Score and "Drew".
At any point type "Exit" to leave the game.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Computer start with 5 lives.
Computer choice is random.
Can you beat the computer?
Good Luck!!
Let's start playing!
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
				print(start_menu)
				while True:
					print ("Your choice:")
					rps = input("Rock, Paper, Scissors? ")
					print ("\n")
					rps = rps.title()
					import random
					computer = ("rock", "paper", "scissors")
					computer = random.choice(computer)
					#rock if statments
					if rps == "Rock" and computer == "paper":
						print("The computer choose",computer)
						print("")
						print(loose)
						print("")
						print("")
						lives-=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					elif rps == "Rock" and computer == "scissors":
						print("The computer choose",computer)
						print("")
						print(win)
						print("")
						print("")
						score+=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
				  #paper if statements
					elif rps == "Paper" and computer == "rock":
						print("The computer choose",computer)
						print("")
						print(win)
						computer_lives -= 1
						print("")
						print("")
						score+=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					elif rps == "Paper" and computer == "scissors":
						print("The computer choose",computer)
						print("")
						print(loose)
						print("")
						print("")
						lives-=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					#scissor if statements
					elif rps == "Scissors" and computer == "paper":
						print("The computer choose",computer)
						print("")
						print(win)
						computer_lives -= 1
						print("")
						print("")
						score+=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					elif rps == "Scissors" and computer == "rock":
						print("The computer choose",computer)
						print("")
						print(loose)
						print("")
						print("")
						lives-=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					#duplicates
					elif rps == "Rock" and computer == "rock":
						print("The computer choose",computer)
						print("")
						print("You Drew")
						print("")
						print("")
						drew+=1  
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					elif rps == "Paper" and computer == "paper":
						print("The computer choose",computer)
						print("")
						print("You Drew")
						print("")
						print("")
						drew+=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					elif rps == "Scissors" and computer == "scissors":
						print("The computer choose",computer)
						print("")
						print("You Drew")
						print("")
						print("")
						drew+=1
						print ("You have",lives,"lives")
						print ("Computer has",computer_lives,"lives")
						print ("Your score is",score,".","\n")
					#system
					elif rps == "Rules":
						print("**********************************************")
						print("Rules")
						print("**********************************************")
						print("-Rock looses against Paper")
						print("-Rock beats Scissors")
						print("-Paper beats Rock")
						print("-Paper looses against Scissors")
						print("-Scissors beats Paper")
						print("-Scissors looses against Rock")
						print("**********************************************")
					elif rps == "Lives":
						print(lives)
					elif rps == "Score":
						print(score)
					elif rps == "Drew":
						print(drew)
					#exit
					elif rps == "Exit":
						exit()
					else:
						print ("This is not a valid option, please try again.","\n")
					#lives
					if lives == 0:
						print("Thanks for playing.")
						print("You have run out of lives")
						print("You got",score,"correct")
						print("You drew",drew,"times")
						stop = input("Press enter to exit.")
						exit()
					if computer_lives == 0:
						print("Thanks for playing.")
						print("The computer lost all it's lives. You Win.")
						print("You got",score,"correct")
						print("You drew",drew,"times")
						stop = input("Press enter to exit.")
						exit()

		if password in line and password != line:
			print("Your username or password is incorrect. Please try again.")
			print("---------------------------------------")
