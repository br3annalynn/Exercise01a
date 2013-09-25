from random import randint
from sys import exit

player_name = raw_input("Hello there! What's your name? ")

print "Let's play a game, %s. I am thinking of a number between 0 and 100. Guess my number." % player_name

def play_game():
    answer = randint(0,100)

    print answer
    tries = 0

    max_tries = 5

    while tries < max_tries:
        print "You have %d tries remaining." % (max_tries - tries)
        guess = int(raw_input("What is your guess? "))
        tries += 1
        if answer > guess:
            print "Your number is too small. Try again!",
        elif answer < guess:
            print "Your answer is too big. Try again!",
        else:
            print "You did it! You win!",
            break

    if guess == answer and tries == 1:
        print "You found the number in %d try!" % tries
    elif guess == answer:
        print "You found the number in %d tries!" %tries 
    else:
        print "You had %d tries and you didn't find the number. You lose. Loser" % max_tries

play_game()
playing = "y"

while playing == "y":
    print "Would you like to play again?"
    print "1. yes"
    print "2. no"
    play_again = raw_input("> ")
    if play_again == "yes" or play_again == "1":
        play_game()
        playing = "y"
    elif play_again =="no" or play_again =="2":
        exit(0)
    else: 
        print "I didn't understand your response."
        playing = "y"