#WHAG (White Hat Adventure Game)
#By stringzzz, Ghostwarez Co.
#Date complete: 01-27-2024 (BETA Version)

#BETA Version not deeply tested. After working out all the test cases, a FULL version will be released soon

#Note: Some kind of password cracker that can work with md5 hashes is needed for this game.
# You may use any you like, though I would reccomend hashcat.
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
