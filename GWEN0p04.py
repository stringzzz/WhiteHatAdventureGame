#GWEN (Generator of Wordlists for ENdeavors) 0.04
#by stringzzz, Ghostwarez Co.
#Date completed (0.01): 01-19-2024
#Date completed (0.02): 01-19-2024 (Cleaned up the code quite a bit)
#Date completed (0.03): 01-21-2024 (Added prompt for user to continue or not after showing exact size of wordlist)
#Added new wordlist pattern option

#Makes generating wordlists with common patterns easier

import itertools
import math

nogen = False
choice = 'none'
while(choice != 'exit'):
	print("Welcome to GWEN (Generator of Wordlists for ENdeavors) 0.04\nMakes generating wordlists with common patterns easier\n")
	choice = input("All size and length estimates below were from using 15char words, and 10 base words.\nAfter entering the base words, you will be given exact sizes for your list\n\nEnter a # choice\n1) [word][0-6#s][word2] 40MB 1,111,111Lines\n2) (Need base word file) [word][0-5#s or '!@#$%&*'] 302MB 15,085,980Lines\n3) (Need base word file) [0-2#s or '!@#$%&*'][word][0-3#s or '!@#$%&*'] 302MB 15,085,980Lines\n4) (Need base word file) [word1][word2][0-4#s or '!@#$%&*'] 267MB 7,986,690Lines\n5) (Need base word file) [word1][word2][word3][3-4#s] 377MB 7,920,000Lines\n6) (Need base word file) Concat list words, generate every permutation of them 523MB 3,628,800Lines\n7) [All 7 digit phone numbers] 77MB 10,000,000Lines\n'exit': Exit GWEN\n\nChoice: ").strip()
	if (choice == '1'):
		list_name = input("Enter the name for the list: ").strip()
		word = input("Enter the start word (Press ENTER to skip): ").strip()
		end_word = input("Enter the end word (Press ENTER to skip): ").strip()
		
		#Get wordlist size and length
		line_count = math.pow(10, 6) + math.pow(10, 5) + math.pow(10, 4) + math.pow(10, 3) + math.pow(10, 2) + 10 + 1
		line_bytes_count = (len(word) + len(end_word) + 1) * line_count + (math.pow(10, 6)*6 + math.pow(10, 5)*5 + math.pow(10, 4)*4 + math.pow(10, 3)*3 + math.pow(10, 2)*2 + 10)
		yn = input("Will generate " + str(math.ceil(line_bytes_count/1024/1024)) + "MB and " + f'{(int(line_count)):,}' + "Lines of data, continue? (y/n): ").strip().lower()
		if (yn != 'y'):
			nogen = True
			break
		
		print("\nGenerating wordlist...\n")
		
		wordlist_file = open(list_name + "_wordlist01.txt", 'w')
		wordlist_file.write(word + end_word + "\n")
		chars = "0123456789"
		for a in range(0, 10):
			wordlist_file.write(word + chars[a] + end_word + "\n")
		for n in range(2, 7):			
			p = list(itertools.product(chars, repeat=n))
			for line in p:
				wordlist_file.write(word + "".join(line) + end_word + "\n")
		wordlist_file.close()
		print("Wordlist '" + list_name + "_wordlist01.txt' generation complete.")
		break
		
	elif (choice == '2'):
		list_name = input("Enter the name for the list: ").strip()
		word_fn = input("Enter the name of the base word file (>30 base words not recommended): ").strip()
		baseword_file=open(word_fn, "r")
		words = baseword_file.read().splitlines()	
		baseword_file.close()
		if (words[len(words) - 1] == ""):
			words.pop()
			
		#Get wordlist size and length
		lines = math.pow(17, 5) + math.pow(17, 4) + math.pow(17, 3) + math.pow(17, 2) + 17 + 1
		line_count = len(words) * lines
		line_bytes_count = 0
		for word in words:
			line_bytes_count += (len(word) + 1) * lines + (math.pow(17, 5)*5 + math.pow(17, 4)*4 + math.pow(17, 3)*3 + math.pow(17, 2)*2 + 17)
		yn = input("Will generate " + str(math.ceil(line_bytes_count/1024/1024)) + "MB and " + f'{(int(line_count)):,}' + "Lines of data, continue? (y/n): ").strip().lower()
		if (yn != 'y'):
			nogen = True
			break
			
		print("\nGenerating wordlist...\n")
		wordlist_file = open(list_name + "_wordlist02.txt", 'w')

		chars = "0123456789!@#$%&*"
		for word in words:
			wordlist_file.write(word + "\n")
			for a in range(0, 17):
				wordlist_file.write(word + chars[a] + "\n")
			for n in range(2, 6):			
				p = list(itertools.product(chars, repeat=n))
				for line in p:
					wordlist_file.write(word + "".join(line) + "\n")
		wordlist_file.close()
		print("Wordlist '" + list_name + "_wordlist02.txt' generation complete.")
		break
		
	elif (choice == '3'):
		list_name = input("Enter the name for the list: ").strip()
		word_fn = input("Enter the name of the base word file (>30 base words not recommended): ").strip()
		baseword_file=open(word_fn, "r")
		words = baseword_file.read().splitlines()
		baseword_file.close()
		if (words[len(words) - 1] == ""):
			words.pop()
			
		#Get wordlist size and length
		lines = math.pow(17, 5) + math.pow(17, 4) + math.pow(17, 3) + math.pow(17, 2) + 17 + 1
		line_count = len(words) * lines
		line_bytes_count = 0
		for word in words:
			line_bytes_count += (len(word) + 1) * lines + (math.pow(17, 5)*5 + math.pow(17, 4)*4 + math.pow(17, 3)*3 + math.pow(17, 2)*2 + 17)
		yn = input("Will generate " + str(math.ceil(line_bytes_count/1024/1024)) + "MB and " + f'{(int(line_count)):,}' + "Lines of data, continue? (y/n): ").strip().lower()
		if (yn != 'y'):
			nogen = True
			break
			
		print("\nGenerating wordlist...\n")
		wordlist_file = open(list_name + "_wordlist03.txt", 'w')

		chars = "0123456789!@#$%&*"
		for word in words:
			wordlist_file.write(word + "\n")
			for a in range(0, 17):
				wordlist_file.write(chars[a] + word + "\n")
			p2 = list(itertools.product(chars, repeat=2)) 
			for line in p2:
				wordlist_file.write("".join(line) + word + "\n")
			for line in p2:
				for c in range(0, 17):
					wordlist_file.write("".join(line) + word + chars[c] + "\n")			
			for n in range(2, 4):			
				p = list(itertools.product(chars, repeat=n))
				for line2 in p2:	
					for line in p:
						wordlist_file.write("".join(line2) + word + "".join(line) + "\n")
		wordlist_file.close()
		print("Wordlist '" + list_name + "_wordlist03.txt' generation complete.")
		break
		
	elif (choice == '4'):
		list_name = input("Enter the name for the list: ").strip()
		word_fn = input("Enter the name of the base word file (>30 base words not recommended): ").strip()
		baseword_file=open(word_fn, "r")
		words = baseword_file.read().splitlines()
		baseword_file.close()
		if (words[len(words) - 1] == ""):
			words.pop()
		words2 = words[:]
			
		#Get wordlist size and length
		lines = math.pow(17, 4) + math.pow(17, 3) + math.pow(17, 2) + 17 + 1
		combo_count = 0
		for word in words:
			for word2 in words2:
				if (word == word2):
					continue
				combo_count += 1
		line_count = combo_count * lines
		line_bytes_count = 0
		for word in words:
			for word2 in words2:
				if (word == word2):
					continue
				line_bytes_count += (len(word) + len(word2) + 1) * lines + (math.pow(17, 4)*4 + math.pow(17, 3)*3 + math.pow(17, 2)*2 + 17)
		yn = input("Will generate " + str(math.ceil(line_bytes_count/1024/1024)) + "MB and " + f'{(int(line_count)):,}' + "Lines of data, continue? (y/n): ").strip().lower()
		if (yn != 'y'):
			nogen = True
			break
			
		print("\nGenerating wordlist...\n")
		wordlist_file = open(list_name + "_wordlist04.txt", 'w')

		chars = "0123456789!@#$%&*"
		for word in words:
			for word2 in words2:
				if (word == word2):
					continue
				wordlist_file.write(word + word2 + "\n")
				for a in range(0, 17):
					wordlist_file.write(word + word2 + chars[a] + "\n")
				for n in range(2, 5):			
					p = list(itertools.product(chars, repeat=n))
					for line in p:
						wordlist_file.write(word + word2 + "".join(line) + "\n")


		wordlist_file.close()
		print("Wordlist '" + list_name + "_wordlist04.txt' generation complete.")
		break
		
	elif (choice == '5'):
		list_name = input("Enter the name for the list: ").strip()
		word_fn = input("Enter the name of the base word file (>20 base words not recommended): ").strip()
		baseword_file=open(word_fn, "r")
		words = baseword_file.read().splitlines()
		baseword_file.close()
		if (words[len(words) - 1] == ""):
			words.pop()
		words2 = words[:]
		words3 = words2[:]
			
		#Get wordlist size and length
		lines = math.pow(10, 4) + math.pow(10, 3)
		combo_count = 0
		for word in words:
			for word2 in words2:
				if (word == word2):
					continue
				for word3 in words3:
					if (word == word3 or word2 == word3):
						continue
					combo_count += 1
		line_count = combo_count * lines
		line_bytes_count = 0
		for word in words:
			for word2 in words2:
				if (word == word2):
					continue
				for word3 in words3:
					if (word == word3 or word2 == word3):
						continue
					line_bytes_count += (len(word) + len(word2) + len(word3) + 1) * lines + (math.pow(10, 4)*4 + math.pow(10, 3)*3)
		yn = input("Will generate " + str(math.ceil(line_bytes_count/1024/1024)) + "MB and " + f'{(int(line_count)):,}' + "Lines of data, continue? (y/n): ").strip().lower()
		if (yn != 'y'):
			nogen = True
			break
			
		print("\nGenerating wordlist...\n")
		wordlist_file = open(list_name + "_wordlist05.txt", 'w')

		chars = "0123456789"
		for word in words:
			for word2 in words2:
				if (word == word2):
					continue
				for word3 in words3:
					if (word == word3 or word2 == word3):
						continue
					for n in range(3, 5):			
						p = list(itertools.product(chars, repeat=n))
						for line in p:
							wordlist_file.write(word + word2 + word3 + "".join(line) + "\n")


		wordlist_file.close()
		print("Wordlist '" + list_name + "_wordlist05.txt' generation complete.")
		break
			
	elif (choice == '6'):
		list_name = input("Enter the name for the list: ").strip()
		word_fn = input("Enter the name of the base word file (>10 base words not recommended): ").strip()
		baseword_file=open(word_fn, "r")
		words = baseword_file.read().splitlines()
		baseword_file.close()
		if (words[len(words) - 1] == ""):
			words.pop()
			
		#Get wordlist size and length
		permuted_words = list(itertools.permutations(words, len(words)))
		line_count = len(permuted_words)
		permute_size = 0
		for word in words:
			permute_size += len(word)
		line_bytes_count = (permute_size + 1) * line_count
		yn = input("Will generate " + str(math.ceil(line_bytes_count/1024/1024)) + "MB and " + f'{(int(line_count)):,}' + "Lines of data, continue? (y/n): ").strip().lower()
		if (yn != 'y'):
			nogen = True
			break
			
		print("\nGenerating wordlist...\n")		
		wordlist_file = open(list_name + "_wordlist06.txt", 'w')
		for line in permuted_words:
			wordlist_file.write("".join(line) + "\n")
		wordlist_file.close()
		print("Wordlist '" + list_name + "_wordlist06.txt' generation complete.")
		break
			
				
	elif (choice == '7'):
		print("\nGenerating wordlist...\n")
		
		wordlist_file = open("phonenumbers7digits_wordlist.txt", 'w')
		chars = "0123456789"
		p = list(itertools.product(chars, repeat=7))
		for line in p:
			wordlist_file.write("".join(line) + "\n")
		wordlist_file.close()
		print("Wordlist 'phonenumbers7digits_wordlist.txt' generation complete.")
		break
	elif (choice == 'exit'):
		nogen = True
		break
	else:
		print("Invalid choice!\n")

if (not(nogen)):		
	print("\nThank you for working with GWEN, happy cracking! ;3\n")
else:
	print("\nAwww, maybe next time... :C\n")
