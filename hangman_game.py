import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'developer', 'programming']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts_remaining = 6
    guessed_word = False

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while attempts_remaining > 0 and not guessed_word:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_remaining -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts_remaining} attempts left.")

        current_word = display_word(word, guessed_letters)
        print(current_word)

        if '_' not in current_word:
            guessed_word = True

    if guessed_word:
        print("Congratulations! You've guessed the word correctly.")
    else:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
