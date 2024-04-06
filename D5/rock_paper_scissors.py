from random import choice

def result(plyr1: int, plyr2: int) -> str:
    if plyr1 == plyr2:
        return "Draw"
    elif plyr1 == 0:  # Rock
        if plyr2 == 1:  # Paper
            return "Computer chose - Rock. You win"
        elif plyr2 == 2: # Scissors
            return "Computer chose - Rock. You lost"
    elif plyr1 == 1:  # Paper
        if plyr2 == 2:  # Scissors
            return "Computer chose - Paper. You win"
        elif plyr2 == 0:  # Rock
            return "Computer chose - paper. You lost"
    elif plyr1 == 2:  # Scissors
        if plyr2 == 0:  # Rock
            return "Computer chose - Scissors. You win"
        elif plyr2 == 1:  # Paper
            return "Computer chose - Scissors. You lost"


def main() -> int:
    # Rock = 0, Paper = 1, Scissors = 2
    comp_choice = choice([0, 1, 2])
    while True:
        try:
            plyr_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors \n"))
            if not plyr_choice in [0, 1, 2]:
                raise ValueError
            break
        except:
            print("Type an integer from 0, 1 or 2 ")
    game_result = result(plyr1=comp_choice, plyr2=plyr_choice)
    print(game_result)

if __name__ == "__main__":
    main()