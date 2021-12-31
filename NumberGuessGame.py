# The number of guesses should be limited, 9 times.
# Print the number of guesses left.
# Print the number of guesses he took to win the game.
# “Game Over” message should display if the number of guesses becomes equal to 0.


name=input("Enter your name :")
print("Good luck!")
n=18
guess=1
print("No of guess is limited to 9")
while guess<9:
    number=int(input("Guess the number"))
    if number<18:
        print("you guessed less no")
    elif number>18:
        print("you Guessed greater number")
    else:
        print("You Won!")
        print("You took ",guess,"attempt")
        break
    print(9-guess,"no of guess left")
    guess=guess+1
if guess>9:
    print("Game over")
