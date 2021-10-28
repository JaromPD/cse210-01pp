import random
import json

def main():
    menu = True
    play = False
    print("Welcome to the HiLo game!\n-------------------------")
    print("You are given a card, and you must guess if the next card\nwill be higher or lower.\n* You start with 300 points.\n* If you are correct you earn 100 points.\n* If you are wrong you lose 75.")
    while menu == True:
        print("\nWhat would you like to do?\n1. Play the game\n2. View high-score\n3. Quit")
        menu_selection = int(input("> "))
        if menu_selection == 1:
            hilo_game(high_score())
        elif menu_selection == 2:
            print(f"\n{high_score()[0]} with a score of {high_score()[1]}")
        else:
            menu = False
    
def hilo_game(high_score_data):
    play = True
    score = 300
    while play == True:

        initial_card = get_card()
        new_card = get_card()
        print(f"\nThe card is: {initial_card}")
        guess = input("Higher or lower? [h/l]: ")
        if initial_card < new_card:
            if guess.lower() == "h":
                score += 100
            else:
                score -= 75
        elif initial_card > new_card:
            if guess.lower() == "l":
                score += 100
            else:
                score -= 75
        else:
            new_card = f"{new_card} - Tie!"
        print(f"Next card was: {new_card}")
        print(f"Your score is: {score}")

        if score <= 0:
            print("GAME OVER! Score too low")
            break

        play_again = input("Keep playing? [y/n]: ")
        if play_again.lower() == "y":
            play = True
        elif play_again.lower() == "n":
            if score > high_score_data [1]:
                print(f"You beat {high_score_data[0]}'s score of: {high_score_data[1]}!")
                add_high_score(score)

            play = False

def get_card():
    card = random.randint(1,13)
    return card

def high_score():
    file = open("highscore.json", "r")
    data = json.load(file)
    high_score_data = data["high-score"]
    high_name = high_score_data[0]
    high_score = high_score_data[1]
    
    return(high_name, high_score)

def add_high_score(score):
    file = open("highscore.json", "r")
    high_score_data = json.load(file)
    file.close()
    file = open("highscore.json", "w")
    name = input("Enter name here: ")
    print(f"Congratulations on your highscore {name}!")
    high_score_data["high-score"] = [name, score]
    json.dump(high_score_data, file)


if __name__ == "__main__":
    main()