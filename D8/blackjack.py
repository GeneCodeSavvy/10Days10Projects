from random import choices

def cards(num_cards:int) -> list[int]:
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choices(cards, k=num_cards)

def results(cards1, cards2):
    threshold = 21
    if sum(cards1) == sum(cards2):
        return []
    elif sum(cards1) > 21 or sum(cards2) > sum(cards1):
        return cards2
    elif sum(cards2) > 21 or sum(cards1) > sum(cards2):
        return cards1

def main():
    comp_cards = cards(2)
    plyr_cards = cards(2)

    print(choices(comp_cards, k=1))
    print(plyr_cards)
    play_further : str = input("Do you want a card? Type 'y' for yes")
    if play_further == "y":
        plyr_cards.append(cards(num_cards=1))
    else:
        winner = results(comp_cards, plyr_cards)
        if winner == plyr_cards:
            print(f"player with {plyr_cards} wins")
        elif winner == comp_cards:
            print(f"computer with {comp_cards} wins")
        else: 
            print(f"player has {plyr_cards}, computer has {comp_cards}. Thereforem this is a draw")

if __name__ == "__main__":
    print("Welcome to BlackJack!")
    # Input Validation
    while True:
        try:
            task: str = input("Do you want to play this game? Type 'y' for yes and 'n' for no\n")
            if task not in ["y", "n"]:
                raise ValueError
            break
        except:
            print("Clear instructions\n")
    
    if task == "y":
        main()