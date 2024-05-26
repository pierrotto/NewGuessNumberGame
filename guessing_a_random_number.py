import random

rand_number = random.randint(1, 100)
print("If you want to stop, press 'Q'!")
try_count = 0

while True:
    player_guess = input("You are given 7 try to guess an integer number from 1 to 100: ")
    try_count += 1

    if player_guess == 'q':
        break
    if not player_guess.isdigit():
        print("Invalid input. Try again...")
        continue
    if try_count == 7:
        print("Too many tries!")
        restart = input("Do you want to play again 'yes'/'no'? ")
        if restart == 'yes':
            continue
        elif restart == 'no':
            break
    if int(player_guess) == rand_number:
        print(f"Congratulations! You entered the right number after {try_count} tries!")
        break
    else:
        if int(player_guess) > rand_number:
            print("This number is too high. Guess again!")
        elif int(player_guess) < rand_number:
            print("This number is too low. Guess again!")

