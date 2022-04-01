############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    return random.choice(cards)


# Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Inside calculate_score() check for a blackjack (sum =21) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().


def calculate_score(c):
    if sum(c) == 21:
        return 0
    elif sum(c) > 21:
        if 11 in c:
            c.remove(11)
            c.append(1)
    return sum(c)


#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(score_comp, score_user):
    if score_comp == score_user:
        print("It's a draw.")
    elif score_comp == 0 or score_user > 21:
        print("You lose:(")
    elif score_user == 0 or score_comp > 21:
        print("You win!")
    else:
        if score_comp > score_user:
            print("You lose:(")
        else:
            print("You win!")


wanna_restart = True
print(logo)
flag = 0
while wanna_restart:
    draw_another = True
    #Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    while draw_another:
        score_user = calculate_score(user_cards)
        score_comp = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {score_user}")
        print(f"Computer's first card: {computer_cards[0]}")
        if score_comp == 0 or score_user > 21:
            print("You lose:(")
            flag = 1
            break
        elif score_user == 0:
            print("You win!")
            flag = 1
            break

        #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

        inp_user = input("Type 'yes' to draw another card else 'no': ")
        if inp_user == 'no':
            draw_another = False
        else:
            user_cards.append(deal_card())

        # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    if (flag == 0):
        while (score_comp < 17 and score_comp != 0):
            computer_cards.append(deal_card())
            score_comp = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, score: {score_user}")
        print(f"Computer's final hand: {computer_cards}, score: {score_comp}")
        compare(score_comp, score_user)

    #Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    inp_user1 = input("Type 'yes' to play again else 'no' to exit: ")
    if inp_user1 == 'no':
        wanna_restart = False
    else:
        os.system('clear')
        print(logo)
