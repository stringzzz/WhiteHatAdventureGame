#This is a demo for WHAG (White Hat Adventure Game)
#By stringzzz, Ghostwarez Co.
#Date complete: 01-18-2024

#Note: Some kind of password cracker that can work with md5 hashes is needed for this game.
# You may use any you like, though I would reccomend hashcat.

#It is a game to practice social engineering and password cracking legally
#The demo is highly simplified, the full version will have much more to it, including more intelligent and realistic chatbots,
# along with more difficult passwords that need custom wordlists to crack, based off of the information you gather from
# the chats. Building trust with the chatbot target will be crucial to getting more information related to their passwords.
#The full version might be a ways away for now, but stay tuned!


import hashlib
import random

user = ""
#Create new user if 'userfile.txt' is empty
#Setup password hash for game
user_file = open("userfile.txt", "r")
if (user_file.readline() == ""): 
	user = input("Enter your username: ")
	user_file = open("userfile.txt", "w")
	user_file.write(user + "\n0")
	user_file.close()
	targetpass = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
	targethash = hashlib.md5(targetpass.encode('utf-8')).hexdigest()
	hash_file = open("iamroothash.txt", "w")
	hash_file.write(targethash)
	hash_file.close()
	print("Welcome, " + user + "!\nEnter '//help' at any time to see your options.\nYou are trying to get the hash file of the target, crack the password, and log in as that user.\nYou may crack the password in any way you like!\nTalk to the user by logging in and entering '//chat' for password clues!\nGood luck!\n")
elif (user_file.readline() == "1"):
	print("You already completed the demo.\nErase the contents of 'userfile.txt' if you wish to play again.\n")
	exit()
else:
	user_file = open("userfile.txt", "r")
	user = user_file.readline().strip()
	user_file.close()

#Main prompt loop	
user_input = "none"
while(user_input != "//quit"):
	user_input = input("'//login': Login as a user\n'//quit': exit the game\n'//help': Repeat this prompt\n")
	if (user_input == "//login"):
		username = input("Username: ")
		if (username == "iamroot"):
			password = input("Password: ")
			passwordhash = hashlib.md5(password.encode('utf-8')).hexdigest()
			hash_file = open("iamroothash.txt", "r")
			testhash = hash_file.readline()
			if (passwordhash == testhash):
				print("\nCongratulations, you won the demo!\n")
				user_file = open("userfile.txt", "w")
				user_file.write(user + "\n1")
				user_file.close()
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
					print("\nEntered the chat with 'iamroot'")
					user_input = "none"
					trust = True
					while (user_input != "//quit"):
						user_input = input(user + ": ").lower()
						if (user_input == "//quit"):
							print("Exiting the chat...\n")
							break
						elif (user_input == "//stealhash"):
							hash_file = open("iamroothash.txt", "r")
							print("iamroot hash: " + hash_file.readline())
							hash_file.close()
							continue
						elif (user_input == "//help"):
							print("'//quit': Quit the chat\n'//stealhash': Steal 'iamroot's hash (Displays it)\n'//help': Repeat this prompt\n")
							continue
						else:
							#This part is a real crude chatbot, it will be better in the full version
							if (trust):
								if (user_input == "hello" or user_input == "hi" or user_input == "sup" or user_input == "yo"):
									print("iamroot: HI TH3R3!")
								elif (user_input == "what is your password?" or user_input == "what is your password" or user_input == "what'ss your password?" or user_input == "tell me your password" or user_input == "tell me your password!" or user_input == "your password?" or user_input == "give me your password?" or user_input == "give me your password!" or user_input == "give me your password" or user_input == "give me your password please" or user_input == "please give me your password" or user_input == "please give me your password!" or user_input == "give me your password, please"):
									print("iamroot: N0, N3V3R!")
									trust = False
								elif (user_input == "what do you like?" or user_input == "what do you like" or user_input == "what do you enjoy" or user_input == "what do you enjoy?" or user_input == "what are your hobbies?" or user_input == "what are your hobbies" or user_input == "what is your favorite topic?" or user_input == "what do you do for fun?"):
									print("iamroot: I L1K3 NUMB3R5!!!")
								elif (user_input == "do you have any pets?" or user_input == "do you have any pets" or user_input == "do you have pets?" or user_input == "do you have pets" or user_input == "what are your pet's names?" or user_input == "what is the name of your pet?" or user_input == "what are the names of your pets?"):
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
	elif (user_input == "//quit"):
		print("Good bye, " + user + "!")
		break
	elif (user_input == "//help"):
		continue
	else:
		print("Invalid command!\n")
