from random import choice
from os import system


def display(lives:int, select_word: str) -> None:
    stages : list[str]= ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
    if lives>0:
        print(stages[lives], "\n", f"You have {lives} lives remaining", "\n", select_word)
    else:
        print(stages[lives], "\n", f"You have {lives} lives remaining", "\n", "You lose")


def select_word() -> str:
    words = choice(['xylophone', 
             'juxtaposition', 
             'quixotic', 
             'zygote', 
             'mnemonic', 
             'phlegmatic', 
             'syzygy', 
             'mnemonics', 
             'cryptic', 
             'oxyphenbutazone', 
             'quixotically', 
             'zephyr', 
             'jacuzzi', 
             'xylophonist', 
             'phlegm', 
             'jazz', 
             'zombie', 
             'vex', 
             'quartz', 
             'buzz'])
    return words


def hints(quiz_word:str, guess_word: str) -> str:
    display = ""
    for letter in quiz_word:
        if letter in guess_word:
            display += letter
        else:
            display += "_"
    return display


def main():
    plyr_life : int = 6
    guesses : list = []
    quiz = select_word()
    word = hints(quiz_word=quiz, guess_word="".join(guesses))
    print(word)
    while not plyr_life == 0:
        guess : str = input("Guess a word: ")
        system("clear")
        if guess in quiz:
            if not guess in guesses:
                guesses.append(guess)
            else:
                print("You have already guessed the word")
            word = hints(quiz_word=quiz, guess_word="".join(guesses))
            display(lives=plyr_life, select_word=word)
            if "_" not in word:
                    print("Congratulations! You guessed the word correctly!")
                    break
        else:
            word = hints(quiz_word=quiz, guess_word=guesses)
            plyr_life -= 1
            display(lives=plyr_life, select_word=word)
            
    

if __name__ == "__main__":
    print("""    __  __                                      
   / / / /___  ____  ____  ____ ___  ____  ____ 
  / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ |
 / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /
/_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/ 
                  /____/                        """)
    print("Welcome to the game, Hangman")
    main()