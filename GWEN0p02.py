#GWEN (Generator of Wordlists for ENdeavors) 0.02
#by stringzzz, Ghostwarez Co.
#Date completed (0.01): 01-19-2024
#Date completed (0.02): 01-19-2024 (Cleaned up the code quite a bit)

#Makes generating wordlists with common patterns easier

import itertools

choice = 'none'
while(choice != 'exit'):
	print("Welcome to GWEN (Generator of Wordlists for ENdeavors) 0.01\nMakes generating wordlists with common patterns easier\n")
	choice = input("Enter a # choice (all size and length estimates were from using 15char words, and 10 base words)\n1) [word][0-6#][word2] 40MB 1,111,111Lines\n2) (Need base word file) [word][0-5# or '!@#$%&*'] 302MB 15,085,980Lines\n3) (Need base word file) [0-2# or '!@#$%&*'][word][0-3digits or '!@#$%&*'chars] 302MB 15,085,980Lines\n4) (Need base word file) [word1][word2][0-3digits or '!@#$%&*'chars] 267MB 7,986,690Lines\n5) (Need base word file) Concat list words, generate every permutation of them 523MB 3,628,800Lines\n6) [All 7 digit phone numbers] 77MB 10,000,000Lines\n'exit': Exit GWEN\nChoice: ").strip()
	if (choice == '1'):
		list_name = input("Enter the name for the list: ").strip()
		word = input("Enter the start word (Press ENTER to skip): ").strip()
		end_word = input("Enter the end word (Press ENTER to skip): ").strip()
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
		word_fn = input("Enter the name of the base word file (>10 base words not recommended): ").strip()
		baseword_file=open(word_fn, "r")
		words = baseword_file.read().splitlines()
		baseword_file.close()
		if (words[len(words) - 1] == ""):
			words.pop()
			
		print("\nGenerating wordlist...\n")
		
		permuted_words = list(itertools.permutations(words, len(words)))		
		wordlist_file = open(list_name + "_wordlist05.txt", 'w')
		for line in permuted_words:
			wordlist_file.write("".join(line) + "\n")
		wordlist_file.close()
		print("Wordlist '" + list_name + "_wordlist05.txt' generation complete.")
		break
			
				
	elif (choice == '6'):
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
		break
	else:
		print("Invalid choice!\n")
		
print("Thank you for working with GWEN, happy cracking! ;3\n")
