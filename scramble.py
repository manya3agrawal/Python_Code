import random

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

def play_round(words):
    word = random.choice(words)
    scrambled = scramble_word(word)
    attempts = 3

    print("\nScrambled word:", scrambled)

    while attempts > 0:
        guess = input("Your guess: ").lower()

        if guess == word:
            print("Correct!")
            return 1  # score for correct guess
        else:
            attempts -= 1
            if attempts > 0:
                print("Wrong guess. Attempts left:", attempts)
            else:
                print("No attempts left. The correct word was:", word)
                return 0

def main():
    words = [
        "python", "computer", "program", "keyboard", "laptop",
        "internet", "science", "variable", "function", "syntax"
    ]

    score = 0
    print("Welcome to the Word Scramble Game!")

    while True:
        score += play_round(words)
        print("Current score:", score)

        again = input("Play again? (yes/no): ").lower()
        if again not in ("yes", "y"):
            break

    print("Final score:", score)
    print("Thanks for playing!")

if __name__ == "__main__":
    main()