import random
import time

def main():
	global count
	global word
	global display
	global length
	global already_guessed
	count = 0
	words_to_guess = ['january', 'border', 'image', 'film', 'promise', 'kids', 'lungs', 'doll', 'rhyme', 'damage', 'plants']
	word = random.choice(words_to_guess)
	length = len(word)
	display = '_' * length
	already_guessed = []

def play_loop():
	play_game = input("Do you want to play again? y= yes, n = no\n")
	while play_game not in ['y', 'n', 'Y', 'N']:
		play_loop()
	if play_game in ["y", "Y"]:
		main()
	elif play_game in ["n", "N"]:
		print("Thanks for playing!")
		exit()

def hangman():
	global count
	global word
	global display
	global length
	global already_guessed
	limit = 5
	guess = input("The hangman word:" + display + "Enter your guess: \n").strip()
	if len(guess) == 0 or len(guess) >= 2 or not(guess.isalpha()):
		print('invalid input, try a letter\n')
		hangman()
	elif guess in word:
		already_guessed.append(guess)
		index = word.find(guess)
		word = word[:index] + '_' + word[index + 1:]
		display = display[:index] + guess + display[index + 1:]
		print(display + "\n")
	elif guess in already_guessed:
		print("Try another letter.\n")
	else:
		count += 1
		if count == 1:
			time.sleep(1)
			print("   _____ \n"
			      "  |      \n"
			      "  |      \n"
			      "  |      \n"
			      "  |      \n"
			      "  |      \n"
			      "  |      \n"
			      "__|__\n")
			print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
		elif count == 2:
			time.sleep(1)
			print("   _____ \n"
		      	"  |     | \n"
		      	"  |     |\n"
		      	"  |      \n"
		      	"  |      \n"
		      	"  |      \n"
		      	"  |      \n"
		      	"__|__\n")
			print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
		elif count == 3:
			time.sleep(1)
			print("   _____ \n"
			      "  |     | \n"
			      "  |     |\n"
			      "  |     | \n"
			      "  |      \n"
			      "  |      \n"
			      "  |      \n"
			      "__|__\n")
			print("Wrong guess. " + str(limit - count) + " guesses remaining\n")			
		elif count == 4:
			time.sleep(1)
			print("   _____ \n"
			      "  |     | \n"
			      "  |     |\n"
			      "  |     | \n"
			      "  |     O \n"
			      "  |      \n"
			      "  |      \n"
			      "__|__\n")	
			print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
		elif count == 5:
			time.sleep(1)
			print("   _____ \n"
			      "  |     | \n"
			      "  |     |\n"
			      "  |     | \n"
			      "  |     O \n"
			      "  |    /|\ \n"
			      "  |    / \ \n"
			      "__|__\n")
			print("Wrong guess. You are hanged!!!\n")
			print("The word was:", already_guessed, word)
			play_loop()
	if word == "_" *length:
		print("congrats! you have guessed the word correctly")
		play_loop()
	elif count != limit:
		hangman()

print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

main()
hangman()
