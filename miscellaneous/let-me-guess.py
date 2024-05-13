print("\n" + "-" * 30 + "\n")

# introduction to the game
print("\nThink of a number between 1 to 100")
print("I will keep giving guesses")
print("If you want me to go lower, say 'lower' or 'l'")
print("If you want me to go higher, say 'higher' or 'h'")
print("If I got the number, say 'yes' or 'y'\n")

print("Shall we begin?")
input("> ")

# variables
min = 1
max = 100
num_of_tries = 0

# game loop
while min < max:
    # increment number of tries
    num_of_tries += 1

    # calculate guess
    guess = (min + max) // 2

    # take user's input on the guess (should we go higher or lower or did we get the number)
    print(f"\n\nI guess {guess}")
    user_input = input("> ")

    # depending on user's input, do the appropriate action
    if user_input in ["h", "higher"]:
        min = guess + 1
    elif user_input in ["l", "lower"]:
        max = guess - 1
    elif user_input in ["yes", "y"]:
        break

print("\n" + "-" * 30)
print(f"Your number was {guess}!")
print(f"It only took me {num_of_tries} tries to get it!")
print("If I didnt get your number, please try playing again")

