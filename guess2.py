from random import randint

player_name = raw_input("Hello there! What's your name? ")

print "Let's play a game, %s. I am thinking of a number between 0 and 100. Guess my number." % player_name

answer = randint(0,101)

print answer
tries = 0

max_tries = 5

while tries < max_tries:
    guess = int(raw_input("What is your guess? "))
    tries += 1
    if answer > guess:
        print "Your number is too small. Try again!"
    elif answer < guess:
        print "Your answer is too big. Try again!"
    else:
        print "You did it! You win!"
        break

if guess == answer and tries == 1:
    print "You found the number in %d try!" % tries
elif guess == answer:
    print "You found the number in %d tries!" %tries 
else:
    print "You had %d tries and you didn't find the number. You lose. Loser" % max_tries