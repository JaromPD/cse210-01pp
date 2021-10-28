import random

def main():
    menu = True
    play = False
    print("Welcome to the HiLo game!\n-------------------------")
    print("You are given a card, and you must guess if the next card\nwill be higher or lower.\n* You start with 300 points.\n* If you are correct you earn 100 points.\n* If you are wrong you lose 75.")
    while menu == True:
        print("\nWhat would you like to do?\n1. Play the game\n2. View high-score")
        menu_selection = int(input("> "))
        if menu_selection == 1:
            hilo_game()
        elif menu_selection == 2:
            high_score()
    
def hilo_game():
    play = True
    score = 300
    while play == True:
        initial_card = get_card()
        new_card = get_card()
        print(f"\nThe card is: {initial_card}")
        guess = input("Higher or lower? [h/l]: ")
        if initial_card < new_card:
            if guess.lower == "h":
                score += 100
            else:
                score -= 75
        elif initial_card > new_card:
            if guess.lower() == "l":
                score += 100
            else:
                score -= 75
        else:
            print("Tie")
        print(f"Next card was: {new_card}")
        print(f"Your score is: {score}")
        play_again = input("Keep playing? [y/n]: ")
        if play_again.lower == "y":
            play = True
        elif play_again.lower == "n":
            play = False

def get_card():
    card = random.randint(1,13)
    return card

def high_score():
    print("Score!")

if __name__ == "__main__":
    main()