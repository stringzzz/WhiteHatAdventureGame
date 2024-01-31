#   WHAG, White Hat Adventure Game, a hacking simulation (FULL Version)
#   Copyright (C) 2024 stringzzz, Ghostwarez Co.
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

#WHAG (White Hat Adventure Game) FULL Version
#By stringzzz, Ghostwarez Co.
#Date complete: 01-28-2024
#Mistake found: 01-30-2024 (One cat name left out in level 5, fixed)

#Note: Some kind of password cracker that can work with md5 hashes is needed for this game.
# You may use any you like, though I would reccomend hashcat.
# If using hashcat, it can be used like this: hashcat -m 0 -a 0 hashfile wordlistfile
# Also, a python script called "GWEN0p03.py" will be provided with this game to help in creating wordlists

#It is a game to practice social engineering and password cracking legally
#The passwords and chatbots become more complex as you move up in levels
#In many cases, earning the target's trust is key to getting them to reveal more of their information
#Use all the information you gather to build wordlists, and crack their password
#While you can output the password hash to the command line while in the chat, it is easier
# to just use the appropriate hash '.txt' file with a password cracker

#If using '//hint', "W's" stands for "Words", while "#'s" of course stands for numbers
#This shows the pattern for the current password

#I decided it would be really annoying to have to start the whole game over if you lose the trust of the
# target, so instead if that happens, you can just '//quit' the chat then re-enter it and the trust
# will reset. On that note, if you keep repeating the same message multiple times in a row, the
# target's trust will go down. This is to encourage it being more realistic.

#If you want to reset the game from the beginning, simply clear out the 'userfile.txt' file
#Note: A new password is generated for each target the FIRST time you enter the level.
#If you exit the game, that password will remain the same. But, if you reset the whole game by 
# clearing the userfile, it will generate new passwords each level (For the challenge and replay value)

#NOTE: I realize that you could just easily edit the script to output the password every time
# If you actually want to play this game for it's intended challenge, why do this?
# At that point, you may as well erase the whole script and replace it with:
# print("You won the whole game!") :P 


import hashlib
import random
import re

def updateUserFile():
	user_file = open("userfile.txt", "w")
	user_file.write(user + "\n" + str(onLevel) + "\n" + str(hashLevel) + "\n" + str(hintCount))
	user_file.close()

user = ""
onLevel = 0
hashLevel = 0
hintCount = 0

#Create new user if 'userfile.txt' is empty
#Setup password hash for game
user_file = open("userfile.txt", "r")
if (user_file.readline() == ""): 
	user = input("Enter your username: ")
	updateUserFile()
	targetpass = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

	targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
	hash_file = open("iamroothash.txt", "w")
	hash_file.write(targethash)
	hash_file.close()
	print("Welcome, " + user + "!\nEnter '//help' at any time to see your options.\nYou are trying to get the hash file of the target, crack the password, and log in as that user.\nYou may crack the password in any way you like!\nTalk to the user by logging in and entering '//chat' for password clues!\nGood luck!\n")
else:
	user_file = open("userfile.txt", "r")
	user = user_file.readline().strip()
	onLevel = int(user_file.readline().strip())
	hashLevel = int(user_file.readline().strip()) 
	hintCount = int(user_file.readline().strip())
	user_file.close()

if (onLevel == 0):
	#Main prompt loop Level 0	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 0 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "iamroot"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("iamroothash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 0!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'iamroot'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with iamroot loop
						print("\nEntered the chat with 'iamroot'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = True
						while (user_input != "//quit"):
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust):
									print("Trust level: Yes")
								else:
									print("Trust level: No")
							elif (user_input == "//stealhash"):
								hash_file = open("iamroothash.txt", "r")
								print("iamroot hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'iamroot's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#This part is a real crude chatbot for level 0, I promise they get better
								if (trust):
									if (user_input == "hello" or user_input == "hi" or user_input == "sup" or user_input == "yo"):
										print("iamroot: HI TH3R3!")
									elif (user_input == "what is your password" or user_input == "tell me your password" or user_input == "give me your password!" or user_input == "give me your password" or user_input == "give me your password please" or user_input == "please give me your password" or user_input == "give me your password, please"):
										print("iamroot: N0, N3V3R!")
										trust = False
									elif (user_input == "what do you like" or user_input == "what do you enjoy" or user_input == "what are your hobbies" or user_input == "what is your favorite topic" or user_input == "what do you do for fun"):
										print("iamroot: I L1K3 NUMB3R5!!!")
									elif (user_input == "do you have any pets" or user_input == "do you have pets" or user_input == "what are your pet's names" or user_input == "what is the name of your pet?" or user_input == "what are the names of your pets"):
										print("iamroot: I L1K3 C0UNT1NG MY P3T5!!")
									else:
										print("iamroot: NUMB3R5 4R3 TH3 B35T35T!!")
								else:
									print("iamroot: I D0N'T W4NT T0 T4LK T0 Y0U 4NYM0R3!")  
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 6#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 1):
	interests = ["Spongebob Squarepants", "Fairly Oddparents", "My Little Pony", "Adventure Time", "Animaniacs"]
	if (hashLevel == 0):
		targetpass = "".join(interests[2].split(" ")).lower() + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		
		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("brony55hash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		hashLevel += 1
		updateUserFile()

	#Main prompt loop Level 1	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 1 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "brony55"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("brony55hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 1!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'brony55'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with brony55 loop
						print("\nEntered the chat with 'brony55'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust >= 4):
									print("Trust level: High")
								elif (trust > 0):
									print("Trust level: Normal")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("brony55hash.txt", "r")
								print("brony55 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'brony55's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#Slightly better chatbot than iamroot
								if (trust <= 0):
									print("brony55: Go away, weirdo!")
								elif (previous_input == user_input):
									print("brony55: You said that already...")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										print("brony55: Hi, I'm just watching some cartoons!")
									elif (re.search(r"(what|what's|which) is (your favorite cartoon)", user_input) or re.search(r"(which|what|what's) (cartoon )?(do you like the most|is the best|is your favorite)", user_input)):
										if (trust >= 4):
											print("brony55: I love My Little Pony the most! :3")
										else:
											print("brony55: That's a secret...")
									elif re.search(r"what (do you like|interests you)", user_input):
										print("brony55: I like cartoons!") 
									elif re.search(r"what do you (like to do|do for fun|enjoy doing|like doing)", user_input):
										print("brony55: I like to spend time watching cartoons!") 
									elif re.search(r"(what|which) (cartoons do you like|is a good cartoon|cartoon is good)", user_input):
										trust += 1
										print("brony55: I like " + random.choice(interests) + "!")
									elif re.search(r"i like (.*)", user_input):
										m1 = re.match(r"i like (.*)", user_input)
										word = m1.group(1)
										interestMatch = False
										for interest in interests:
											if (interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("brony55: I like " + word + " too! :D")
											trust += 1
										else:
											print("brony55: That's nice...")	
									elif (re.search(r"(do you )?have (any )?pets", user_input) or re.search(r"what (is |are )(your pet's names|the name(s)? of your pet(s)?)", user_input)):
										if re.match(r"(do you )?have (any )?pets", user_input):
											print("brony55: No, but if I did I would have a pony named Sparklez! :3") 
										elif re.match(r"what (is |are )(your pet's names|the name(s)? of your pet(s)?)", user_input):
											print("brony55: I don't have any, but if I did I would have a pony named Sparklez! :3") 			
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("brony55: No, WTH?! :O")
										trust -= 1
									else:
										n = random.randint(0, 3)
										if (n == 0):
											print("brony55: I'm not sure what you mean? :O")		  
										elif (n == 1):
											print("brony55: I don't know what you are talking about... :S")
										elif (n == 2):
											print("brony55: Say what?")
										else:
											print("brony55: Huh?")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 3W's3#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 2):
	interests = ["Pokemon", "The Godfather", "James Bond", "Crosswords", "Legos"]
	interestAct = ["playing", "watching", "watching", "solving", "building"]
	if (hashLevel == 1):
		targetpass = "".join((random.choice(interests).lower().split(" "))) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		
		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("thechief506hash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		hashLevel += 1
		updateUserFile()

	#Main prompt loop Level 2	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 2 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "thechief506"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("thechief506hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 2!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'thechief506'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with thechief506 loop
						print("\nEntered the chat with 'thechief506'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust > 0):
									print("Trust level: Good")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("thechief506hash.txt", "r")
								print("thechief506 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'thechief506's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#Slightly better chatbot than brony55
								if (trust <= 0):
									print("thechief506: I don't trust you one bit")
								elif (previous_input == user_input):
									print("thechief506: You said that already...")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										print("thechief506: Not much, same old same old")
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										print("thechief506: Maybe... The Godfather trilogy or any James Bond movie")							
									elif re.search(r"what (do you like|interests you)", user_input):
										print("thechief506: I like " + random.choice(interests) + ", sometimes") 
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										rnum = random.randint(0, 4)
										print("thechief506: I like " + interestAct[rnum] + " " + interests[rnum] + " from time to time") 
									elif re.search(r"i (like|love|enjoy) (.*)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (.*)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in interests:
											if (interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("thechief506: Agreed, " + word + " is cool")
											trust += 1
										else:
											print("thechief506: Cool, cool")	
									elif re.search(r"do you have (any )?pets", user_input):
										print("thechief506: I have a cat named Muffins. Muffins is a chill cat")			
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("thechief506: Hah, not cool, man")
										trust -= 1
									else:
										n = random.randint(0, 3)
										if (n == 0):
											print("thechief506: Not sure about that one")		  
										elif (n == 1):
											print("thechief506: I don't know about that")
										elif (n == 2):
											print("thechief506: I don't even know what to say")
										else:
											print("thechief506: Huh?")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 1-2W2#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 3):
	interests = ["Budweiser", "Captain Morgan", "Jack Daniels", "Grey Goose", "Corona", "Tequila", "Moonshine"]
	drunkInterests = ["buuuudwizer", "Capin moregon", "Javk danyuls", "gray gus", "cornona", "tekeela", "Moanshinw"]
	if (hashLevel == 2):
		targetpass = "".join((random.choice(interests).lower().split(" "))) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		
		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("drunk4lifehash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		hashLevel += 1
		updateUserFile()

	#Main prompt loop Level 3	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 3 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "drunk4life"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("drunk4lifehash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 3!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'drunk4life'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with drunk4life loop
						print("\nEntered the chat with 'drunk4life'\nEnter '//help' to see options\n")
						user_input = "none"
						while (user_input != "//quit"):
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								print("Trust level: Drunk")
							elif (user_input == "//stealhash"):
								hash_file = open("drunk4lifehash.txt", "r")
								print("drunk4life hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'drunk4life's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#Drunken chatbot ;D
								if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
									print("drunk4life: oh, whassup mann!?")
								elif re.search(r"(what is|what's) your favorite movie", user_input):
									print("drunk4life: animal hows! lol")							
								elif re.search(r"what (do you like|interests you)", user_input):
									print("drunk4life: oh yea i lovw " + random.choice(drunkInterests) + ", hell yah!!!!") 
								elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
									rnum = random.randint(0, 4)
									print("drunk4life: for sure, i rely leik " + random.choice(drunkInterests) + " ya know lolol") 
								elif re.search(r"i (like|love|enjoy) (.*)", user_input):
									m1 = re.match(r"i (like|love|enjoy) (.*)", user_input)
									word = m1.group(2)
									interestMatch = False
									for interest in interests:
										if (interest.lower() == word):
											interestMatch = True
									if (interestMatch):
										print("drunk4life: heel ya man, " + word + " is it!!!!")
									else:
										for interest in drunkInterests:
											if (interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("drunk4life: hahah, for sure, " + word + " is evertythin!!!!")
										else:
											print("drunk4life: alrihhgt man")	
								elif re.search(r"do you have (any )?pets", user_input):
									print("drunk4life: ysh, I hav a pet named al... Alcohol, lololol")			
								elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
									print("drunk4life: Shure, i think its... i dont remember, lol!")
								else:
									n = random.randint(0, 3)
									if (n == 0):
										print("drunk4life: loolol, never herd that 1 bfore")		  
									elif (n == 1):
										print("drunk4life: yo mamaa, lol hah")
									elif (n == 2):
										print("drunk4life: im so lost noww, lol")
									else:
										print("drunk4life: who said wut? hahahsr")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 1-2W2#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 4):
	interestChoices = ["NFL", "football", "sports", "hockey", "basketball", "baseball", "dogs", "MMA", "working out", "superbowl"]
	interestDict = {"nfl": "following the", "football": "watching", "sports": "playing and watching", "hockey": "watching", "basketball": "playing", "baseball": "watching", "dogs": "playing with my", "mma": "seeing live", "working out": "at the gym", "superbowl": "booking tickets for"}
	favoriteDict = {"football team": "Raiders", "hockey team": "Mighty Ducks", "baseball team": "Dodgers", "mma fighter": "The Iceman", "gym": "Planet Fitness"}
	favoriteTeams = ["raiders", "mighty ducks", "ducks", "dodgers", "iceman", "planet fitness"]
	openInterests = []
	privateInterests = []
	if (hashLevel == 3):
	
		interest_file = open("interests_Raiders557.txt", "w")
		for word in range(0, 5):
			rnum = random.randint(0, len(interestChoices) - 1)
			openInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		openInterests.append("Raiders")
		for word in range(0, 3):
			rnum = random.randint(0, len(interestChoices) - 1)
			privateInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		interest_file.close()
		
		targetpass = openInterests[len(openInterests) - 1].lower() + "".join((random.choice(privateInterests).lower().split(" "))) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		
		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("Raiders557hash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		hashLevel += 1
		updateUserFile()
	else:
		#Restore previously generated lists of interests
		interest_file = open("interests_Raiders557.txt", "r")
		tempInterests = interest_file.readline().split("&&&&")
		interest_file.close()
		if (tempInterests[len(tempInterests) - 1] == ""):
			del tempInterests[len(tempInterests) - 1]
		for n in range(0, len(tempInterests)):
			if (n >= 5):
				privateInterests.append(tempInterests[n])
			else:
				openInterests.append(tempInterests[n])
		openInterests.append("Raiders")
		
	#Main prompt loop Level 4	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 4 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "Raiders557"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("Raiders557hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 4!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'Raiders557'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with Raiders557 loop
						print("\nEntered the chat with 'Raiders557'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust >= 5):
									print("Trust level: High")
								elif (trust > 0):
									print("Trust level: Normal")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("Raiders557hash.txt", "r")
								print("Raiders557 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'Raiders557's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#Slightly better chatbot than thechief506
								if (trust <= 0):
									print("Raiders557: I couldn't trust you any less")
								elif (previous_input == user_input):
									print("Raiders557: You said that already...")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										print("Raiders557: Just watching some sports")
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										print("Raiders557: I'm not really into movies")							
									elif re.search(r"what (do you like|interests you)", user_input):
										if (trust >= 5):
											print("Raiders557: I really love " + random.choice(privateInterests) + "!")
										else:	
											print("Raiders557: Gotta love " + random.choice(openInterests) + ", definitely") 
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										if (trust >= 5):
											rnum = random.randint(0, 2)
											print("Raiders557: I really like " + interestDict[privateInterests[rnum].lower()] + " " + privateInterests[rnum] + " all the time")
										else: 
											rnum = random.randint(0, 5)
											print("Raiders557: I like " + interestDict[openInterests[rnum].lower()] + " " + openInterests[rnum] + " sometimes")
											trust += 1 
									elif re.search(r"i (like|love|enjoy) (the )?(.*)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (the )?(.*)", user_input)
										word = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("Raiders557: Most true, " + word + " is great")
											trust += 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												print("Raiders557: I know, right?")
												trust += 1
											else:
												for interest in favoriteTeams:
													if (interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													print("Raiders557: That's what I'm talking about!")
													trust += 1
												else:
													print("Raiders557: I guess that's cool")
									elif re.search(r"i (hate|don't like|dislike) (the )?(.*)", user_input):
										m1 = re.match(r"i (hate|don't like|dislike) (the )?(.*)", user_input)
										word = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("Raiders557: Hold up, " + word + " is so good!")
											trust -= 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												print("Raiders557: You must be crazy!")
												trust -= 1
											else:
												for interest in favoriteTeams:
													if (interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													print("Raiders557: Get out, you don't know what you are talking about!")
													trust -= 1
												else:
													print("Raiders557: lol, yep")
									elif re.search(r"(what is|what's|which is) (your )?favorite (.*)", user_input):
										m1 = re.match(r"(what is|what's|which is) (your )?favorite (.*)", user_input)
										word = m1.group(3)
										try:
											favoriteDict[word]
											print("Raiders557: My favorite would be, " + favoriteDict[word] + ", of course")
											trust += 1
										except(KeyError):
											print("Raiders557: I'm not sure")					 
									elif re.search(r"do you have (any )?pets", user_input):
										print("Raiders557: I have a dog named Patchy, like eye patch")			
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("Raiders557: Sus...")
										trust -= 1
									else:
										n = random.randint(0, 3)
										if (n == 0):
											print("Raiders557: Hold up, the game is back on")		  
										elif (n == 1):
											print("Raiders557: I'm not sure what you mean")
										elif (n == 2):
											print("Raiders557: You lost me")
										else:
											print("Raiders557: sure, sure")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 2-3W's2#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 5):
	cats = ["Fluffy", "Tigger", "Garfield", "Bob", "Tom", "Dmitri", "Buttercup", "Lilith", "Oreo", "Olga"]
	catActions = ["playing with", "holding", "cuddling with", "grooming", "feeding", "cooking for", "hanging out with", "petting", "talking to"]
	catTypes = {"Fluffy": "is so hairy!", "Tigger": "is so bouncy!", "Garfield": "is so lazy", "Bob": "is so laid back", "Tom": "is such a hunter", "Dmitri": "is so cuddly", "Buttercup": "is so cute", "Lilith": "is so full of attitude", "Oreo": "is such big eater", "Olga": "is so grouchy"}
	currentCats = []
	pastCats = []
	
	if (hashLevel == 4):
		catsForPass = cats[:]
		interest_file = open("interests_CrazyCatLady853.txt", "w")
		for word in range(0, 8):
			rnum = random.randint(0, len(cats) - 1)
			currentCats.append(cats[rnum])
			interest_file.write(cats[rnum] + "&&&&")
			del cats[rnum]

		for word in range(0, 2):
			rnum = random.randint(0, len(cats) - 1)
			pastCats.append(cats[rnum])
			interest_file.write(cats[rnum] + "&&&&")
			del cats[rnum]
		for name in pastCats:
			catTypes[name] = catTypes[name].replace("is", "was")
		interest_file.close()
		
		targetpass = ""
		for name in range(0, 10):
			rnum = random.randint(0, len(catsForPass) - 1)
			targetpass += catsForPass[rnum]
			del catsForPass[rnum]
		
		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("CrazyCatLady853hash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		hashLevel += 1
		updateUserFile()
	else:
		#Restore previously generated lists of interests
		interest_file = open("interests_CrazyCatLady853.txt", "r")
		tempInterests = interest_file.readline().split("&&&&")
		interest_file.close()
		if (tempInterests[len(tempInterests) - 1] == ""):
			del tempInterests[len(tempInterests) - 1]
		for n in range(0, len(tempInterests)):
			if (n >= 8):
				pastCats.append(tempInterests[n])
			else:
				currentCats.append(tempInterests[n])

	#Main prompt loop Level 5	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 5 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "CrazyCatLady853"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("CrazyCatLady853hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 5!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'CrazyCatLady853'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with CrazyCatLady853 loop
						print("\nEntered the chat with 'CrazyCatLady853'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust >= 7):
									print("Trust level: High")
								elif (trust > 0):
									print("Trust level: Normal")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("CrazyCatLady853hash.txt", "r")
								print("CrazyCatLady853 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'CrazyCatLady853's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:							
								if (trust <= 0):
									print("CrazyCatLady853: You should go away!")
								elif (previous_input == user_input):
									print("CrazyCatLady853: You said that already...")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										print("CrazyCatLady853: Just hanging out with my cats")
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										print("CrazyCatLady853: Puss in Boots")							
									elif re.search(r"what (do you like|interests you)$", user_input):
										print("CrazyCatLady853: I really love my cat " + random.choice(currentCats) + "!")
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										rnum = random.randint(0, len(currentCats) - 1)
										rnum2 = random.randint(0, len(catActions) - 1)
										print("CrazyCatLady853: I love " + catActions[rnum2] + " " + currentCats[rnum] + " daily :3")
										trust += 1 
									elif re.search(r"i (like|love|enjoy) (.*) (cats|kittens)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (.*) (cats|kittens)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in catActions:
											if (interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("CrazyCatLady853: Me too!")
											trust += 1
										else:
											print("CrazyCatLady853: Okay...")
											trust -= 1
									elif re.search(r"i (hate|don't like|dislike) (.*) (cats|kittens)", user_input):
										m1 = re.match(r"i (hate|don't like|dislike) (.*) (cats|kittens)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in catActions:
											if (interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("CrazyCatLady853: What's wrong with you?!")
											trust -= 1
										else:
											print("CrazyCatLady853: I understand")
									elif re.search(r"(what is|what's|which is) (your )?favorite cat", user_input):
											rnum1 = random.randint(0, len(currentCats) - 1)
											rnum2 = rnum1
											while(rnum2 == rnum1):
												rnum2 = random.randint(0, len(currentCats) - 1)
											print("CrazyCatLady853: My favorite would be... " + currentCats[rnum1] + "! No, wait..." + currentCats[rnum2] + "! Oh, I just can't pick a favorite, I love them all!")
											trust += 1
									elif re.search(r"what (is |are )(your (pet's|cat's) names|the name(s)? of your (pet(s)?|cat(s)?))", user_input):
										rnum1 = random.randint(0, len(currentCats) - 1)
										rnum2 = rnum1
										while(rnum2 == rnum1):
											rnum2 = random.randint(0, len(currentCats) - 1)
										print("CrazyCatLady853: Well, there's... " + currentCats[rnum1] + "! And... " + currentCats[rnum2] + "! Oh, that's not all of them, lol...")
										trust += 1					 
									elif re.search(r"do you have (any )?pets", user_input):
										print("CrazyCatLady853: That's an understatement! I have 10... Actually no, I'm sorry, I have 8 now... :(")			
									elif re.search(r"what do you (like|love|enjoy|) about (.*)", user_input):
										m1 = re.match(r"what do you (like|love|enjoy|) about (.*)", user_input)							
										word = m1.group(2)
										nameMatch = False
										name2 = ""
										for name in currentCats:
											if (name.lower() == word):
												nameMatch = True
												name2 = name
										if (nameMatch):
											print("CrazyCatLady853: " + name2 + " " + catTypes[name2] + " I love them!")
											trust += 1
										else:
											for name in pastCats:
												if (name.lower() == word):
													nameMatch = True
													name2 = name
												if (nameMatch):
													if (trust >= 7):
														print("CrazyCatLady853: " + name2 + " " + catTypes[name2] + ", I miss them :'(")
													else:
														print("CrazyCatLady853: I don't want to talk about them right now...")
												else:
													print("CrazyCatLady853: Not sure...")
									elif re.search(r"(what other cats did you have|(what|which) cats passed away|what are the names of your (past|previous|passed away) cats|(which|what) cats are gone (now)?|what are your past pet's names)", user_input):
										if (trust >= 7):
											print("CrazyCatLady853: " + pastCats[0] + " and " + pastCats[1] + ", they lived a long life, a happy life. I still miss them, though... :'(")
										else:
											print("CrazyCatLady853: I don't want to share about them with you...")
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("CrazyCatLady853: No way, creep!")
										trust -= 1
									else:
										n = random.randint(0, 5)
										if (n == 0):
											print("CrazyCatLady853: lol, I'm " + random.choice(catActions) + " " + random.choice(currentCats) + "! :3")		  
										elif (n == 1):
											rnum1 = random.randint(0, len(currentCats) - 1)
											rnum2 = rnum1
											while(rnum2 == rnum1):
												rnum2 = random.randint(0, len(currentCats) - 1)
											print("CrazyCatLady853: Hah, " + currentCats[rnum1] + " and " + currentCats[rnum2] + " are playing together! :3")
										elif (n == 2):
											print("CrazyCatLady853: Not sure about that")
										elif (n == 3):
											print("CrazyCatLady853: do you like cats?")
										elif (n == 4):
											print("CrazyCatLady853: Okay?")
										else:
											rnum1 = random.randint(0, len(currentCats) - 1)
											print("CrazyCatLady853: Awww..." + currentCats[rnum1] + " " + catTypes[currentCats[rnum1]] + " :3")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 10W's\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 6):
	interestChoices = ["bowling", "golf", "YouTube", "skateboarding", "chess", "animation", "clay sculpting", "painting", "video games", "recipes", "horror movies", "short stories", "science fiction", "poetry", "jokes"]
	interestDict = {"bowling": "going", "golf": "watching and playing", "youtube": "watching", "skateboarding": "going", "chess": "playing", "animation": "creating", "clay sculpting": "doing", "painting": "graffiti", "video games": "playing", "recipes": "trying new", "horror movies": "watching", "short stories": "writing", "science fiction": "reading", "poetry": "writing", "jokes": "telling"}
	openInterests = []
	privateInterests = []
	
	if (hashLevel == 5):
	
		interest_file = open("interests_monkeystinks52.txt", "w")
		for word in range(0, 5):
			rnum = random.randint(0, len(interestChoices) - 1)
			openInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		for word in range(0, 5):
			rnum = random.randint(0, len(interestChoices) - 1)
			privateInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		interest_file.close()
	
		targetpass = "".join((random.choice(openInterests).lower().split(" "))) + "".join((random.choice(privateInterests).lower().split(" "))) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		
		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("monkeystinks52hash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		hashLevel += 1
		updateUserFile()
	else:
		#Restore the previously generated lists of interests
		interest_file = open("interests_monkeystinks52.txt", "r")
		tempInterests = interest_file.readline().split("&&&&")
		interest_file.close()
		if (tempInterests[len(tempInterests) - 1] == ""):
			del tempInterests[len(tempInterests) - 1]
		for n in range(0, len(tempInterests)):
			if (n >= 5):
				privateInterests.append(tempInterests[n])
			else:
				openInterests.append(tempInterests[n])

	#Main prompt loop Level 6	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 6 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "monkeystinks52"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("monkeystinks52hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 6!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'monkeystinks52'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with monkeystinks52 loop
						print("\nEntered the chat with 'monkeystinks52'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust >= 6):
									print("Trust level: High")
								elif (trust > 0):
									print("Trust level: Normal")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("monkeystinks52hash.txt", "r")
								print("monkeystinks52 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'monkeystinks52's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#monkeystinks52 chat
								if (trust <= 0):
									print("monkeystinks52: I'm done talking to you")
								elif (previous_input == user_input):
									print("monkeystinks52: Again with that? What's your deal?")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										rnum1 = random.randint(0, len(openInterests) - 1)
										print("monkeystinks52: Not much, just thinking about " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1])
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										print("monkeystinks52: Either Avatar or Transformers")							
									elif re.search(r"what (do you like|interests you)$", user_input):
										if (trust >= 6):
											rnum1 = random.randint(0, len(privateInterests) - 1)
											print("monkeystinks52: I really love " + interestDict[privateInterests[rnum1].lower()] + " " + privateInterests[rnum1] + "!")
										else:	
											print("monkeystinks52: Gotta love " + random.choice(openInterests) + ", definitely") 
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										if (trust >= 6):
											print("monkeystinks52: I really like " + random.choice(privateInterests) + ", it's fun!")
										else: 
											rnum = random.randint(0, len(privateInterests) - 1)
											print("monkeystinks52: I like " + interestDict[openInterests[rnum].lower()] + " " + openInterests[rnum] + " somewhat")
											trust += 1 
									elif re.search(r"i (like|love|enjoy) (.*)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (.*)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("monkeystinks52: Hah, yeah, " + word + " is cool")
											trust += 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												print("monkeystinks52: Totally agree, " + word + " is awesome!")
												trust += 1
											else:
												print("monkeystinks52: That's good, I guess")
									elif re.search(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input):
										m1 = re.match(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input)
										word = m1.group(1)
										isare = m1.group(2)
										description = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("monkeystinks52: Yes, " + word + " " + isare + description)
											trust += 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												print("monkeystinks52: For sure, " + word + " is " + description + "!")
												trust += 1
											else:
												print("monkeystinks52: That's good, I guess")
									elif re.search(r"i (hate|don't like|dislike) (the )?(.*)", user_input):
										m1 = re.match(r"i (hate|don't like|dislike) (the )?(.*)", user_input)
										word = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("monkeystinks52: WTF, " + word + " is cool?")
											trust -= 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												print("monkeystinks52: No way, " + word + " is so awesome!")
												trust -= 1
											else:
												print("monkeystinks52: Hah, okay")					 
									elif re.search(r"do you have (any )?pets", user_input):
										print("monkeystinks52: Just 2 turtles, Koopa and Bowser")			
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("monkeystinks52: Wow, is that your L4M3 idea of hacking, just ask for the password? :/")
										trust -= 1
									else:
										n = random.randint(0, 4)
										if (n == 0):
											rnum1 = random.randint(0, len(openInterests) - 1)
											print("monkeystinks52: I'm thinking of " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1] + ", soon")		  
										elif (n == 1):
											print("monkeystinks52: Sorry, I'm lost, lol")
										elif (n == 2):
											print("monkeystinks52: Not too sure what you are talking about")
										elif (n == 3):
											print("monkeystinks52: Ok")
										else:
											print("monkeystinks52: Well, then...")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 2-4W's4#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 7):
	interestChoices = ["Pokemon cards", "TikToks", "YouTube", "clubbing", "music", "game shows", "cartoons", "anime", "manga", "jokes"]
	interestChoices2 = interestChoices[:]
	interestDict = {"pokemon cards": "collecting", "tiktoks": "creating", "youtube": "watching", "clubbing": "going", "music": "listening to", "game shows": "watching", "cartoons": "drawing", "anime": "watching", "manga": "reading", "jokes": "making"}
	openInterests_jb = []
	openInterests_ff = []
	
	if (hashLevel == 6):
	
		interest_file = open("interests_johnnyboy082.txt", "w")
		for word in range(0, 6):
			rnum = random.randint(0, len(interestChoices) - 1)
			openInterests_jb.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		interest_file.close()
	
		rnum1 = random.randint(0, len(openInterests_jb) - 1)
		rnum2 = random.randint(0, len(openInterests_jb) - 1)
		targetpass_jb = "".join(openInterests_jb[rnum1].lower().split(" ")) + "".join(openInterests_jb[rnum2].lower().split(" ")) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		
		targethash_jb = hashlib.md5(targetpass_jb.encode('utf-8')).hexdigest()
		hash_file = open("johnnyboy082hash.txt", "w")
		hash_file.write(targethash_jb)
		hash_file.close()
		jb = "Johnny"
		
		interest_file = open("interests_friendsforever28.txt", "w")
		for word in range(0, 5):
			rnum = random.randint(0, len(interestChoices2) - 1)
			openInterests_ff.append(interestChoices2[rnum])
			interest_file.write(interestChoices2[rnum] + "&&&&")
			del interestChoices2[rnum]
		interest_file.close()
	
		targetpass_ff = jb.lower() + "".join((random.choice(openInterests_ff).lower().split(" "))) + str(random.randint(0, 9)) + str(random.randint(0, 9))
		
		targethash_ff = hashlib.md5(targetpass_ff.encode('utf-8')).hexdigest()
		hash_file = open("friendsforever28hash.txt", "w")
		hash_file.write(targethash_ff)
		hash_file.close()
		
		hashLevel += 1
		updateUserFile()
	else:
		#Restore the previously generated lists of interests
		interest_file = open("interests_johnnyboy082.txt", "r")
		tempInterests_jb = interest_file.readline().split("&&&&")
		interest_file.close()
		if (tempInterests_jb[len(tempInterests_jb) - 1] == ""):
			del tempInterests_jb[len(tempInterests_jb) - 1]
		for n in range(0, len(tempInterests_jb)):
			openInterests_jb.append(tempInterests_jb[n])
			
		interest_file = open("interests_friendsforever28.txt", "r")
		tempInterests_ff = interest_file.readline().split("&&&&")
		interest_file.close()
		if (tempInterests_ff[len(tempInterests_ff) - 1] == ""):
			del tempInterests_ff[len(tempInterests_ff) - 1]
		for n in range(0, len(tempInterests_ff)):
			openInterests_ff.append(tempInterests_ff[n])

	#Main prompt loop Level 7	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 7 #####\n'//login': Login as a user\n'//hint johnnyboy082': See a hint for the johnnyboy082 password\n'//hint friendsforever28': See a hint for the friendsforever28 password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "johnnyboy082"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("johnnyboy082hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 7!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif ((username == user) or (username == "friendsforever28")):
				if (username == "friendsforever28"):
					password = input("Password: ")
					passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
					hash_file = open("friendsforever28hash.txt", "r")
					testhash = hash_file.readline()
					if (passwordhash == testhash):
						print("\nLogged in as friendsforever28\n")
					else:
						print("Login failed!\n")
						continue
					
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat johnnyboy082': Enter the chat with 'johnnyboy082'\n'//chat friendsforever28': Enter the chat with 'friendsforever28'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat johnnyboy082"):
					
						#Chat with johnnyboy082 loop
						print("\nEntered the chat with 'johnnyboy082'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 0
						if (username == "friendsforever28"):
							trust = 5
						else:
							trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(username + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (username == "friendsforever28"):
									if (trust > 0):
										print("Trust level: High")
									else:
										print("Trust level: None")
								else:
									if (trust > 0):
										print("Trust level: Almost none")
									else:
										print("Trust level: Absolutely none")
							elif (user_input == "//stealhash"):
								hash_file = open("johnnyboy082hash.txt", "r")
								print("johnnyboy082 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'johnnyboy082's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#johnnyboy082 chat
								if (trust <= 0):
									if (username == "friendsforever28"):
										print("johnnyboy082: What happened with you?")
									else:
										print("johnnyboy082: Go away, I don't even know you.")
								elif (previous_input == user_input):
									print("johnnyboy082: Again with that? What's your deal?")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										if (username == "friendsforever28"):
											rnum1 = random.randint(0, len(openInterests_jb) - 1)
											print("johnnyboy082: Just thinking about " + interestDict[openInterests_jb[rnum1].lower()] + " " + openInterests_jb[rnum1] + ", the usual")
										else:
											print("johnnyboy082: Nothing that concerns you...")
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										if (username == "friendsforever28"):
											print("johnnyboy082: Don't you remember the movie Soul? We both saw it together and it became our favorite, are you okay?")
											trust -= 1
										else:
											print("johnnyboy082: Nunya. Nunya business...")							
									elif re.search(r"what (do you like|interests you)$", user_input):
										if (username == "friendsforever28"):
											rnum1 = random.randint(0, len(openInterests_jb) - 1)
											print("johnnyboy082: I really love " + interestDict[openInterests_jb[rnum1].lower()] + " " + openInterests_jb[rnum1] + ", but you already know that lol")
										else:
											print("johnnyboy082: As if you need to know that")
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										if (username == "friendsforever28"):
											print("johnnyboy082: I really like " + random.choice(openInterests_jb) + ", and I know you do to!")
											trust += 1
										else: 
											print("johnnyboy082: I like people I know, as in not you")
									elif re.search(r"i (like|love|enjoy) (.*)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (.*)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in openInterests_jb:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											if (username == "friendsforever28"):
												print("johnnyboy082: Of course " + word + " is cool, I already know you like that")
												trust += 1
											else:
												print("johnnyboy082: Yeah... That's nice")
										else:
											if (username == "friendsforever28"):
												print("johnnyboy082: I didn't know that about you!")
											else:
												print("johnnyboy082: Good for you")
									elif re.search(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input):
										m1 = re.match(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input)
										word = m1.group(1)
										isare = m1.group(2)
										description = m1.group(3)
										interestMatch = False
										for interest in openInterests_jb:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											if (username == "friendsforever28"):
												print("johnnyboy082: Hah " + word + " " + isare + "definitely " + description)
												trust += 1
											else:
												print("johnnyboy082: Sure")
										else:
											if (username == "friendsforever28"):
												print("johnnyboy082: Sure is, hah")
											else:
												print("johnnyboy082: Great, good for you")
									elif re.search(r"i (hate|don't like|dislike) (the )?(.*)", user_input):
										m1 = re.match(r"i (hate|don't like|dislike) (the )?(.*)", user_input)
										word = m1.group(3)
										interestMatch = False
										for interest in openInterests_jb:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											if (username == "friendsforever28"):
												print("johnnyboy082: Huh? Since when?")
												trust -= 1
											else:
												print("johnnyboy082: I don't really care...")
										else:
											if (username == "friendsforever28"):
												print("johnnyboy082: lol, true that")
											else:
												print("johnnyboy082: Oh, okay")					 
									elif re.search(r"do you have (any )?pets", user_input):
										if (username == "friendsforever28"):
											print("johnnyboy082: Are you okay? How do you not remember my cat Poof?")
											trust -= 1
										else:
											print("johnnyboy082: Why do you care?")			
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										if (username == "friendsforever28"):
											print("johnnyboy082: Okay, something is not right here...")
											trust -= 3
										else:
											print("johnnyboy082: I didn't trust you to begin with, but now I really don't.")
											trust -= 2
									else:
										if (username == "friendsforever28"):
											n = random.randint(0, 4)
											if (n == 0):
												rnum1 = random.randint(0, len(openInterests_jb) - 1)
												print("johnnyboy082: I think I'm gonna " + interestDict[openInterests_jb[rnum1].lower()] + " " + openInterests_jb[rnum1] + " in a bit, maybe?")		  
											elif (n == 1):
												print("johnnyboy082: lol, wut?")
											elif (n == 2):
												print("johnnyboy082: You're weird, but that's why you're my friend, lol")
											elif (n == 3):
												print("johnnyboy082: Hah, good one")
											else:
												print("johnnyboy082: I'm a bit confused, here :S")
										else:
											print("johnnyboy082: I have no desire to talk to you...")	
					elif (user_input == "//chat friendsforever28"):
						#Chat with friendsforever28 loop
						print("\nEntered the chat with 'friendsforever28'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(username + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (username == "friendsforever28"):
									print("Trust level: LOL, wait, what are you even doing?")
								elif (trust > 0):
									print("Trust level: Good")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("friendsforever28hash.txt", "r")
								print("friendsforever28 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'friendsforever28's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#friendsforever28 chat
								if (username == "friendsforever28"):
									print("friendsforever28: WTF is going on, seriously?!")
								elif (trust <= 0):
									print("friendsforever28: I don't want to talk to you now")
								elif (previous_input == user_input):
									print("friendsforever28: Why do you keep repeating? Are you a robot?")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										if (random.randint(0, 2) == 1):
											print("friendsforever28: I think I'll call my best friend Johnny soon")
										else:
											rnum1 = random.randint(0, len(openInterests_ff) - 1)
											print("friendsforever28: Hmmm... " + interestDict[openInterests_ff[rnum1].lower()] + " " + openInterests_ff[rnum1] + " is probably what I'll be doing soon")
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										print("friendsforever28: The movie Soul, for sure")							
									elif re.search(r"what (do you like|interests you)$", user_input):
										if (random.randint(0, 2) == 1):
											print("friendsforever28: I really love hanging out with my friend Johnny!")
										else:
											rnum1 = random.randint(0, len(openInterests_ff) - 1)
											print("friendsforever28: I really love " + interestDict[openInterests_ff[rnum1].lower()] + " " + openInterests_ff[rnum1] + ", what about you?")
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										if (random.randint(0, 2) == 1):
											print("friendsforever28: I like to hang out with my friend Johnny all day!")
										else:
											print("friendsforever28: I really like " + random.choice(openInterests_ff) + ", do you?")
											trust += 1
									elif re.search(r"i (like|love|enjoy) (.*)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (.*)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in openInterests_ff:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("friendsforever28: Yep, " + word + " is cool!")
											trust += 1
										else:
											print("friendsforever28: That's pretty cool")
									elif re.search(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input):
										m1 = re.match(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input)
										word = m1.group(1)
										isare = m1.group(2)
										description = m1.group(3)
										interestMatch = False
										for interest in openInterests_ff:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("friendsforever28: I know, " + word + " " + isare + "definitely " + description + ", right? :)")
											trust += 1
										else:
											print("friendsforever28: That is interesting, I haven't ever done anything with that")
									elif re.search(r"i (hate|don't like|dislike) (the )?(.*)", user_input):
										m1 = re.match(r"i (hate|don't like|dislike) (the )?(.*)", user_input)
										word = m1.group(3)
										interestMatch = False
										for interest in openInterests_ff:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("friendsforever28: Well, agree to disagree, I guess")
											trust -= 1
										else:
											print("friendsforever28: Hah, nice")					 
									elif re.search(r"do you have (any )?pets", user_input):
											print("friendsforever28: Yeah, my cat Foop. He is my friend's cat's brother :3")			
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("friendsforever28: Umm... how about... no?")
										trust -= 1
									else:
										n = random.randint(0, 4)
										if (n == 0):
											rnum1 = random.randint(0, len(openInterests_ff) - 1)
											print("friendsforever28: I think I'll be " + interestDict[openInterests_ff[rnum1].lower()] + " " + openInterests_ff[rnum1] + " in a while, maybe?")		  
										elif (n == 1):
											print("friendsforever28: lol, huh?")
										elif (n == 2):
											print("friendsforever28: You're weird, lol!")
										elif (n == 3):
											print("friendsforever28: Hah, nice one")
										else:
											print("friendsforever28: I think we're on different pages right now, lol")
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint johnnyboy082"):
			hintCount += 1
			updateUserFile()
			print("Hint: 2-4W's3#'s\n")
		elif (user_input == "//hint friendsforever28"):
			hintCount += 1
			updateUserFile()
			print("Hint: 1-2W's2#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 8):
	interestChoices = ["Pokemon", "vodka", "action movies", "comedy movies", "comics", "math problems", "experiments", "camping", "poems", "martial arts", "yoga", "swimming", "cakes", "basketball", "skateboarding", "models", "YouTube", "clay", "freestyle raps", "photos"]
	interestDict = {"pokemon": "playing", "vodka": "drinking", "action movies": "watching", "comedy movies": "watching", "comics": "drawing", "math problems": "solving", "experiments": "doing", "camping": "going", "poems": "writing", "martial arts": "practicing", "yoga": "practicing", "swimming": "going", "cakes": "baking", "basketball": "watching and playing", "skateboarding": "going", "models": "building", "youtube": "watching", "clay": "sculpting", "freestyle raps": "doing", "photos": "taking"}
	interestWhys = {"pokemon": "competitive battling of", "playing pokemon": "competitive battling of", "vodka": "the taste and buzz of", "drinking vodka": "the taste and buzz of", "action movies of": "the suspense of", "watching action movies": "the suspense of", "comedy movies": "the humor of", "watching comedy movies": "the humor of", "comics": "the creativity of", "drawing comics": "the creativity of", "math problems": "the challenge of", "solving math problems": "the challenge of", "experiments": "the science of", "doing experiments": "the science of", "camping": "the adventure of", "going camping": "the adventure of", "poems": "the creativity of", "writing poems": "the creativity of", "martial arts": "the peace of", "practicing martial arts": "the peace of", "yoga": "the zen of", "practicing yoga": "the zen of", "swimming": "the freedom of", "going swimming": "the freedom of", "cakes": "the satisfaction of", "baking cakes": "the satisfaction of", "basketball": "the excitement of", "watching basketball": "the excitement of", "playing basketball": "the excitement of", "skateboarding": "the freedom of", "going skateboarding": "the freedom of", "models": "the satisfaction of", "building models": "the satisfaction of", "youtube": "the variety of content of", "watching youtube": "the variety of content of", "clay": "the creativity of", "sculpting clay": "the creativity of", "freestyle raps": "the entertainment of", "doing freestyle raps": "the entertainment of", "photos": "the art of", "taking photos": "the art of"}
	openInterests = []
	privateInterests = []
	secretInterests = []
	
	if (hashLevel == 7):
	
		interest_file = open("interests_redeye36.txt", "w")
		for word in range(0, 6):
			rnum = random.randint(0, len(interestChoices) - 1)
			openInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		for word in range(0, 5):
			rnum = random.randint(0, len(interestChoices) - 1)
			privateInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		for word in range(0, 3):
			rnum = random.randint(0, len(interestChoices) - 1)
			secretInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		interest_file.close()
		
		targetpass = "".join((random.choice(openInterests).lower().split(" "))) + "".join((random.choice(privateInterests).lower().split(" "))) + "".join((random.choice(secretInterests).lower().split(" "))) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("redeye36hash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		hashLevel += 1
		updateUserFile()
	else:
		#Restore the previously generated lists of interests	
		interest_file = open("interests_redeye36.txt", "r")
		tempInterests = interest_file.readline().split("&&&&")
		interest_file.close()
		if (tempInterests[len(tempInterests) - 1] == ""):
			del tempInterests[len(tempInterests) - 1]
		for n in range(0, len(tempInterests)):
			if (n >= 11):
				secretInterests.append(tempInterests[n])
			elif (n >= 6 and n < 11):
				privateInterests.append(tempInterests[n])
			else:
				openInterests.append(tempInterests[n])

	#Main prompt loop Level 8	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 8 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "redeye36"):
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("redeye36hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed level 8!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("Login failed!\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'redeye36'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with redeye36 loop
						print("\nEntered the chat with 'redeye36'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust >= 9):
									print("Trust level: Highest")
								elif (trust >= 5):
									print("Trust level: Mid")
								elif (trust > 0):
									print("Trust level: Slight")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("redeye36hash.txt", "r")
								print("redeye36 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'redeye36's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#redeye36 chat
								if (trust <= 0):
									print("redeye36: You can leave now")
								elif (previous_input == user_input):
									print("redeye36: Is there an echo in here?")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										rnum1 = random.randint(0, len(openInterests) - 1)
										print("redeye36: " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1] + " is on my mind right now")
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										print("redeye36: The Bourne movies, or Ms. Doubtfire for the lulz")							
									elif re.search(r"what (do you (like|love|enjoy)|interests you)$", user_input):
										if (trust >= 9):
											rnum1 = random.randint(0, len(secretInterests) - 1)
											print("redeye36: I absolutely love " + interestDict[secretInterests[rnum1].lower()] + " " + secretInterests[rnum1] + ", it's excellent!")
										elif (trust >= 5 and trust < 9):
											rnum1 = random.randint(0, len(privateInterests) - 1)
											print("redeye36: I really like " + interestDict[privateInterests[rnum1].lower()] + " " + privateInterests[rnum1] + ", it's great")
										else:	
											print("redeye36: Sometimes " + random.choice(openInterests) + ", is cool") 
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										if (trust >= 9):
											print("redeye36: " + random.choice(secretInterests) + " is the absolute best!")
										elif (trust >= 5 and trust < 9):
											rnum1 = random.randint(0, len(privateInterests) - 1)
											print("redeye36: I like to often " + interestDict[privateInterests[rnum1].lower()] + " " + privateInterests[rnum1] + ", good times")
											trust += 1
										else: 
											rnum = random.randint(0, len(privateInterests) - 1)
											print("redeye36: I like " + interestDict[openInterests[rnum].lower()] + " " + openInterests[rnum] + " here and there")
											trust += 1 
									elif re.search(r"i (like|love|enjoy) (.*)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (.*)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("redeye36: Yeah, " + word + " is pretty cool")
											trust += 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												if (trust >= 5):
													print("redeye36: For sure, " + word + " is great!")
													trust += 1
												else:
													print("redeye36: I get you.")
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													if (trust >= 9):
														print("redeye36: Hell yeah, " + word + " is the best!")
														trust += 1
													else:
														print("redeye36: Yeah, cool")
												else:
													print("redeye36: I don't know about that, but cool")
									elif re.search(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input):
										m1 = re.match(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input)
										word = m1.group(1)
										isare = m1.group(2)
										description = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("redeye36: Agreed, " + word + " " + isare + "sometimes " + description)
											trust += 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												if (trust >= 5):
													print("redeye36: For sure, " + word + " is " + description + "!")
													trust += 1
												else:
													print("redeye36: Maybe...")
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													if (trust >= 9):
														print("redeye36: For sure, " + word + " is " + description + "!")
														trust += 1
													else:
														print("redeye36: I will neither confirm nor deny...")
												else:
													print("redeye36: Cool, I don't know much about it though")
									elif re.search(r"i (hate|don't like|dislike) (the )?(.*)", user_input):
										m1 = re.match(r"i (hate|don't like|dislike) (the )?(.*)", user_input)
										word = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("redeye36: Serious? " + word + " seems cool to me")
											trust -= 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												print("redeye36: What? " + word + " is great?!")
												trust -= 1
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													print("redeye36: I'm not sure we can talk anymore, " + word + " is my life!")
													trust -= 1
												else:
													if (trust < 16):
														print("redeye36: lol, I don't know what else to say.")	
													else:
														print("redeye36: hah, you know I almost feel like a crappy chatbot created by some weird coder named stringzzz, isn't that crazy? (@_@)") 				 
									elif re.search(r"what do you (really )?(like|enjoy|love) about (.*)", user_input):
										m1 = re.match(r"what do you (really )?(like|enjoy|love) about (.*)", user_input)
										word = m1.group(3)
										description = m1.group(2)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("redeye36: I " + description + " " + interestWhys[word] + " " + word)
											trust += 2
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												if (trust >= 5):
													print("redeye36: I really " + description + " " + interestWhys[word] + " " + word + ", for sure")
													trust += 2
												else:
													print("redeye36: How did you know about that?")
													trust -= 1
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													if (trust >= 9):
														print("redeye36: I absolutely " + description + " " + interestWhys[word] + " " + word + ", oh yeah!")
														trust += 2
													else:
														print("redeye36: Okay, this is weird, I know I never told you about that?")
														trust -= 1
												else:
													print("redeye36: I actually don't really like or dislike that, I guess?")
									elif re.search(r"do you have (any )?pets", user_input):
										print("redeye36: Not yet, but I would like either a cat or a dog. Maybe both?")			
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("redeye36: You're at level 8 and you're still trying this? XD")
										trust -= 1
									else:
										n = random.randint(0, 7)
										if (n == 0):
											rnum1 = random.randint(0, len(openInterests) - 1)
											print("redeye36: I think I will be " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1] + ", in a while")		  
										elif (n == 1):
											print("redeye36: IDK, IDK")
										elif (n == 2):
											print("redeye36: Hah, huh? HAHUH? :S")
										elif (n == 3):
											print("redeye36: I don't think I've ever heard that one, lol")
										elif (n == 4):
											rnum1 = random.randint(0, len(openInterests) - 1)
											print("redeye36: Maybe I'll be " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1] + ", I'll chat for a while, though")	
										elif (n == 5):
											print("redeye36: I'm speechless, lulz")
										elif (n == 6):
											print("redeye36: If I had a nickel for every time I heard that one, I would have... 5 cents :P")
										else:
											print("redeye36: That is quite strange...")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 3-6W's3#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 9):
	interestChoices = ["drama movies", "chess", "go", "anime", "arts and crafts", "cars", "cats", "characters", "jokes", "meat", "music", "dances", "TikToks", "games", "graphic design", "coffee", "recipes", "mystery books", "model cars", "model planes", "Warhammer", "Pokemon cards", "MTG", "Star Wars", "Star Trek", "code", "computers", "photographs", "scotch", "coins"]
	interestDict = {"drama movies": "watching", "chess": "playing", "go": "playing", "anime": "watching", "arts and crafts": "making", "cars": "working on", "cats": "playing with", "characters": "drawing", "jokes": "cracking", "meat": "barbecuing", "music": "listening to", "dances": "doing", "tiktoks": "watching", "games": "playing", "graphic design": "doing", "coffee": "drinking", "recipes": "creating", "mystery books": "reading", "model cars": "building", "model planes": "building", "warhammer": "playing", "pokemon cards": "collecting", "mtg": "playing", "star wars": "watching", "star trek": "watching", "code": "writing", "computers": "using", "photographs": "taking", "scotch": "drinking", "coins": "collecting"}
	interestWhys = {"drama movies": "the cliffhangers of", "watching drama movies": "the cliffhangers of","chess": "the strategy of", "playing chess": "the strategy of", "go": "the strategy of", "playing go": "the strategy of", "anime": "the humor and action of", "watching anime": "the humor and action of", "arts and crafts": "the creativity of", "making arts and crafts": "the creativity of", "cars": "the joy of", "working on cars": "the joy of", "cats": "the cuteness of", "playing with cats": "the cuteness of", "characters": "the fun of", "drawing characters": "the fun of", "jokes": "the entertainment of", "cracking jokes": "the entertainment of", "meat": "the satisfaction of", "barbecuing meat": "the satisfaction of", "music": "the emotions of", "listening to music": "the emotions of", "dances": "the excitement of", "doing dances": "the excitement of", "tiktoks": "the variety of", "watching tiktoks": "the variety of", "games": "the strategy of", "playing games": "the strategy of", "graphic design": "the creativity of", "doing graphic design": "the creativity of", "coffee": "the buzz of", "drinking coffee": "the buzz of", "recipes": "the satisfaction of", "creating recipes": "the satisfaction of", "mystery books": "the thrill of", "reading mystery books": "the thrill of", "model cars": "the process of", "building model cars": "the process of", "model planes": "the process of", "building model planes": "the process of", "warhammer": "the strategy of", "playing warhammer": "the strategy of", "pokemon cards": "the art of", "collecting pokemon cards": "the art of", "mtg": "the strategy of", "playing mtg": "the strategy of", "star wars": "the excitement of", "watching star wars": "the excitement of", "star trek": "the intelligence of", "watching star trek": "the intelligence of", "code": "the challenge of", "writing code": "the challenge of", "computers": "the power of", "using computers": "the power of", "photographs": "the beauty of", "taking photographs": "the beauty of", "scotch": "the taste of", "drinking scotch": "the taste of", "coins": "the completeness of", "collecting coins": "the completeness of" }
	cats = ["Snowball", "Mittens", "Tom", "Bubbles", "Anna", "Smithy", "Patches", "Waffles", "Sam", "Iris"]
	names = ["Jennifer", "Gwen", "Marta", "Anya", "Jane", "Sophia", "Emma", "Samantha", "Jolene", "Gina"]
	cars = ["Chevy Cobra", "Toyota Camry", "Ford Mustang", "Nissan Ultima", "Mitsubishi Eclipse"]
	openInterests = []
	privateInterests = []
	secretInterests = []
	a1 = ""
	a2 = ""
	a3 = ""
	a4 = ""
	a5 = ""
	a6 = ""
	
	if (hashLevel == 8):
	
		interest_file = open("interests_TheBoss0.txt", "w")
		for word in range(0, 8):
			rnum = random.randint(0, len(interestChoices) - 1)
			openInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		rnum = random.randint(0, len(cats) - 1)
		a1 = cats[rnum]
		interest_file.write(cats[rnum] + "&&&&")
		del cats[rnum]
		rnum = random.randint(0, len(cats) - 1)
		a2 = cats[rnum]
		interest_file.write(cats[rnum] + "&&&&")
		del cats[rnum]
		rnum = random.randint(0, len(cats) - 1)
		a3 = cats[rnum]
		interest_file.write(cats[rnum] + "&&&&")
		for word in range(0, 6):
			rnum = random.randint(0, len(interestChoices) - 1)
			privateInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		rnum = random.randint(0, len(names) - 1)
		a4 = names[rnum]
		interest_file.write(names[rnum] + "&&&&")
		rnum = random.randint(0, len(cars) - 1)
		a5 = cars[rnum]
		interest_file.write(cars[rnum] + "&&&&")
		del cars[rnum]
		rnum = random.randint(0, len(cars) - 1)
		a6 = cars[rnum]
		interest_file.write(cars[rnum] + "&&&&")
		for word in range(0, 4):
			rnum = random.randint(0, len(interestChoices) - 1)
			secretInterests.append(interestChoices[rnum])
			interest_file.write(interestChoices[rnum] + "&&&&")
			del interestChoices[rnum]
		interest_file.close()
	
		targetpass = "".join((random.choice(openInterests).lower().split(" "))) + "".join((random.choice(privateInterests).lower().split(" "))) + "".join((random.choice(secretInterests).lower().split(" "))) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))

		targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
		hash_file = open("TheBoss0hash.txt", "w")
		hash_file.write(targethash)
		hash_file.close()
		sec_file = open("TheBoss0SecHashes.txt", "w")
		sec_file.write(hashlib.md5(a2.encode('utf-8')).hexdigest() + "\n")
		sec_file.write(hashlib.md5(a4.encode('utf-8')).hexdigest() + "\n")
		sec_file.write(hashlib.md5(a6.encode('utf-8')).hexdigest() + "\n")
		sec_file.close()
		hashLevel += 1
		updateUserFile()
	else:
		#Restore the previously generated lists of interests
		interest_file = open("interests_TheBoss0.txt", "r")
		tempInterests = interest_file.readline().split("&&&&")
		interest_file.close()
		if (tempInterests[len(tempInterests) - 1] == ""):
			del tempInterests[len(tempInterests) - 1]
		for n in range(0, 24):
			if (n < 8):
				openInterests.append(tempInterests[n])
			elif (n == 8):
				a1 = tempInterests[n]
			elif (n == 9):
				a2 = tempInterests[n]
			elif (n == 10):
				a3 = tempInterests[n]
			elif (n > 10 and n < 17):
				privateInterests.append(tempInterests[n])
			elif (n == 17):
				a4 = tempInterests[n]
			elif (n == 18):
				a5 = tempInterests[n]
			elif (n == 19):
				a6 = tempInterests[n]
			elif (n > 19 and n < 24):
				secretInterests.append(tempInterests[n])

	#Main prompt loop Level 8	
	user_input = "none"
	while(user_input != "//quit"):
		user_input = input("\n##### LEVEL 9 #####\n'//login': Login as a user\n'//hint': See a hint for the current password\n'//quit': Exit the game\n'//help': Repeat this prompt\n")
		if (user_input == "//login"):
			username = input("Username: ")
			if (username == "TheBoss0"):
				sec_file = open("TheBoss0SecHashes.txt", "r")
				sec_hashes = sec_file.readlines()
				sec_file.close()
				sec_answer1 = input("You're logging in on a new device, please answer your security questions to continue\nWhat was the name of your first pet?: ")
				
				if (hashlib.md5(sec_answer1.encode('utf-8')).hexdigest() == sec_hashes[0].strip()):
					sec_answer2 = input("What was the name of your first partner?: ")
					if (hashlib.md5(sec_answer2.encode('utf-8')).hexdigest() == sec_hashes[1].strip()):
						sec_answer3 = input("What was the make and model of your first car?: ")
						if (hashlib.md5(sec_answer3.encode('utf-8')).hexdigest() == sec_hashes[2].strip()):
							print("Security check passed, enter your password to continue logging in")
						else:
							print("ACCESS DENIED\n")
							continue
					else:
						print("ACCESS DENIED\n")
						continue
				else:
					print("ACCESS DENIED\n")
					continue
				password = input("Password: ")
				passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
				hash_file = open("TheBoss0hash.txt", "r")
				testhash = hash_file.readline()
				if (passwordhash == testhash):
					print("\nCongratulations, you completed the entire game!\n")
					onLevel += 1
					updateUserFile()
					break
				else:
					print("ACCESS DENIED\n")
					continue
			elif (username == user):
			
				#Logged in prompt loop
				user_input = "none"
				while(user_input != "//logout"):
					user_input = input("\n'//logout': Logout\n'//chat': Enter the chat with 'TheBoss0'\n'//help': Repeat this prompt\n")
					if (user_input == "//logout"):
						break
					elif (user_input == "//chat"):
						#Chat with TheBoss0 loop
						print("\nEntered the chat with 'TheBoss0'\nEnter '//help' to see options\n")
						user_input = "none"
						trust = 1
						while (user_input != "//quit"):
							previous_input = user_input
							user_input = input(user + ": ").lower()
							user_input = re.sub(r"(\.|\?|!)", "", user_input)
							if (user_input == "//quit"):
								print("Exiting the chat...\n")
								break
							elif (user_input == "//trustlevel"):
								if (trust >= 16):
									print("Trust level: Highest")
								elif (trust >= 13):
									print("Trust level: High")
								elif (trust >= 7):
									print("Trust level: Mid")
								elif (trust > 0):
									print("Trust level: Slight")
								else:
									print("Trust level: None")
							elif (user_input == "//stealhash"):
								hash_file = open("TheBoss0hash.txt", "r")
								print("TheBoss0 hash: " + hash_file.readline())
								hash_file.close()
								continue
							elif (user_input == "//help"):
								print("'//quit': Quit the chat\n'//trustlevel': View current trust level of target\n'//stealhash': Steal 'TheBoss0's hash (Displays it)\n'//help': Repeat this prompt\n")
								continue
							else:
								#TheBoss0 chat
								if (trust <= 0):
									print("TheBoss0: Get lost, you!")
								elif (previous_input == user_input):
									print("TheBoss0: Are you glitching out?")
									trust -= 1
								else:
									if re.search(r"(hello|hi|what is up|(what is|what's) up|sup|(what is|what's) cracking|(what is|what's) going on)$", user_input):
										rnum1 = random.randint(0, len(openInterests) - 1)
										print("TheBoss0: Hi, " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1] + " is going through my head")
									elif re.search(r"(what is|what's) your favorite movie", user_input):
										print("TheBoss0: Back To The Future, all 3")							
									elif re.search(r"what (do you (like|love|enjoy)|interests you)$", user_input):
										if (trust >= 16):
											print("TheBoss0: I like hanging out with my wife, " + a4)
										elif (trust >= 13 and trust < 16):
											if (random.randint(0, 2) == 1):
												print("TheBoss0: I love hanging out with my wife.")
											else:
												rnum1 = random.randint(0, len(secretInterests) - 1)
												print("TheBoss0: I totally love " + interestDict[secretInterests[rnum1].lower()] + " " + secretInterests[rnum1] + ", it's the best!")
										elif (trust >= 7 and trust < 13):
											rnum1 = random.randint(0, len(privateInterests) - 1)
											print("TheBoss0: I like " + interestDict[privateInterests[rnum1].lower()] + " " + privateInterests[rnum1] + " a lot")
										else:	
											print("TheBoss0: From time to time, " + random.choice(openInterests) + ", is good") 
									elif re.search(r"what do you (like to do|do for fun|enjoy doing)", user_input):
										if (trust >= 16):
											print("I enjoy working on my good, old " + a6)
										elif (trust >= 13 and trust < 16):
											print("TheBoss0: " + random.choice(secretInterests) + " is the greatest, aside from my wife, of course!")
										elif (trust >= 7 and trust < 13):
											rnum1 = random.randint(0, len(privateInterests) - 1)
											print("TheBoss0: I sometimes like to " + interestDict[privateInterests[rnum1].lower()] + " " + privateInterests[rnum1] + ", it's pretty cool")
											trust += 1
										else: 
											rnum = random.randint(0, len(privateInterests) - 1)
											print("TheBoss0: Every once in a while " + interestDict[openInterests[rnum].lower()] + " " + openInterests[rnum] + " is rewarding")
											trust += 1 
									elif re.search(r"i (like|love|enjoy) (.*)", user_input):
										m1 = re.match(r"i (like|love|enjoy) (.*)", user_input)
										word = m1.group(2)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("TheBoss0: Yep, I hear you, " + word + " is okay")
											trust += 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												if (trust >= 7):
													print("TheBoss0: Indeed, " + word + " is pretty cool")
													trust += 1
												else:
													print("TheBoss0: I get you, I think.")
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													if (trust >= 13):
														print("TheBoss0: Yes, totally, " + word + " is fire")
														trust += 1
													else:
														print("TheBoss0: Yeah, alright")
												else:
													print("TheBoss0: I don't even know what that is, but more power to you")
									elif re.search(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input):
										m1 = re.match(r"(.*) (is |are )(cool|fun|awesome|great|good|nice)", user_input)
										word = m1.group(1)
										isare = m1.group(2)
										description = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("TheBoss0: True, " + word + " " + isare + description + " sometimes")
											trust += 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												if (trust >= 7):
													print("TheBoss0: Agreed in full, " + word + " is " + description + "!")
													trust += 1
												else:
													print("TheBoss0: Oh, alright")
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													if (trust >= 13):
														print("TheBoss0: Hah, I like you, " + word + " is definitely " + description + "!")
														trust += 1
													else:
														print("TheBoss0: Nice")
												else:
													print("TheBoss0: That's good, I guess")
									elif re.search(r"i (hate|don't like|dislike) (the )?(.*)", user_input):
										m1 = re.match(r"i (hate|don't like|dislike) (the )?(.*)", user_input)
										word = m1.group(3)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("TheBoss0: What? " + word + " is good, you're missing out")
											trust -= 1
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												print("TheBoss0: Serious? " + word + " is great!")
												trust -= 1
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													print("TheBoss0: Wow, " + word + " is one of the points of existing!")
													trust -= 1
												else:
													print("TheBoss0: haha, nice") 				 
									elif re.search(r"what do you (really )?(like|enjoy|love) about (.*)", user_input):
										m1 = re.match(r"what do you (really )?(like|enjoy|love) about (.*)", user_input)
										word = m1.group(3)
										description = m1.group(2)
										interestMatch = False
										for interest in openInterests:
											if (interest.lower() == word):
												interestMatch = True
											elif (interestDict[interest.lower()] + " " + interest.lower() == word):
												interestMatch = True
										if (interestMatch):
											print("TheBoss0: I " + description + " " + interestWhys[word] + " " + word)
											trust += 2
										else:
											for interest in privateInterests:
												if (interest.lower() == word):
													interestMatch = True
												elif (interestDict[interest.lower()] + " " + interest.lower() == word):
													interestMatch = True
											if (interestMatch):
												if (trust >= 13):
													print("TheBoss0: I really " + description + " " + interestWhys[word] + " " + word + ", that's the truth")
													trust += 2
												else:
													print("TheBoss0: That's odd that you're asking me about that...")
													trust -= 1
											else:
												for interest in secretInterests:
													if (interest.lower() == word):
														interestMatch = True
													elif (interestDict[interest.lower()] + " " + interest.lower() == word):
														interestMatch = True
												if (interestMatch):
													if (trust >= 7):
														print("TheBoss0: I absolutely " + description + " " + interestWhys[word] + " " + word + ", it's deep in my life!")
														trust += 2
													else:
														print("TheBoss0: Hold up. How did you know I like that?")
														trust -= 1
												else:
													print("TheBoss0: I'm not real big on that, actually")
									elif re.search(r"(do you have (any )?pets|(what is|what's) the name of your first pet)", user_input):
										if (trust >= 16):
											print("TheBoss0: Ah, I remember my first cat..." + a2 + ", R.I.P :'(")
										else:
											print("TheBoss0: Well, right now I got " + a1 + " and " + a3 + ", but I don't share about my past pets. Too personal, no offense")
									elif re.search(r"((what is|what's) the name of your (first partner|wife))", user_input):
										if (trust >= 16):
											print("TheBoss0: I married my first partner, love at first sight, you know?")
										else:
											print("TheBoss0: That's a bit too personal for me")
									elif re.search(r"((what is|what's|what was) the (make|model|type|make and model) of your (first|original) car)", user_input):
										if (trust >= 16):
											print("TheBoss0: I still have it, working on it regularly. It's a " + a6 + ". Its my baby")
										else:
											print("TheBoss0: I don't feel comfortable sharing that right now")		
									elif re.search(r"(please )?(what is|what's|tell me|give me) your pass(word)?(\,? please)?", user_input):
										print("TheBoss0: GAME OVER\nTheBoss0: JK, but why are you seriously asking me this?")
										trust -= 1
									else:
										n = random.randint(0, 7)
										if (n == 0):
											rnum1 = random.randint(0, len(openInterests) - 1)
											print("TheBoss0: I'm thinking of " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1] + ", at some point later on")		  
										elif (n == 1):
											print("TheBoss0: Hah, okay")
										elif (n == 2):
											print("TheBoss0: Strange")
										elif (n == 3):
											print("TheBoss0: Much weird, you are")
										elif (n == 4):
											rnum1 = random.randint(0, len(openInterests) - 1)
											print("TheBoss0: " + interestDict[openInterests[rnum1].lower()] + " " + openInterests[rnum1] + ", sounds fun right now")	
										elif (n == 5):
											print("TheBoss0: Words can't describe")
										elif (n == 6):
											print("TheBoss0: lmao, cool")
										else:
											print("TheBoss0: I think you're losing it...")	
					elif (user_input == "//help"):
						continue
					else:
						print("Invalid command!\n")
						continue
			else:
				print("Invalid username!")
				continue
		elif (user_input == "//hint"):
			hintCount += 1
			updateUserFile()
			print("Hint: 3-7W's4#'s\n")		
		elif (user_input == "//quit"):
			print("Good bye, " + user + "!\n")
			break
		elif (user_input == "//help"):
			continue
		else:
			print("Invalid command!\n")
if (onLevel == 10):
	print("\nYou have completed the whole game, congratulations!\nYou used a total of " + str(hintCount) + " password hints.\n\nWHAG (White Hat Adventure Game)\nCreated by stringzzz, Ghostwarez Co. 2024\nI really hope you didn't cheat and enjoyed the full challenge of the game, but I won't judge if you cheated a little.\nOf course, you would be more 1337 and not L4M3 if you didn't cheat at all, just saying...\nAnyway...\n\nDo you want to start from the beginning? Just clear out the file 'userfile.txt' to erase all progress.")
