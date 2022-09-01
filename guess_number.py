class Guessed_Big(Exception):
    pass


class Guessed_Small(Exception):
    pass


right_number = 47
while True:
    try:
        guessed = int(input("Enter guessed number: "))
        if guessed > right_number:
            raise Guessed_Big
        elif guessed < right_number:
            raise Guessed_Small
        break

    except Guessed_Big:
        print("Your guessed number is too big.")
    except Guessed_Small:
        print("Your guessed number is too small.")

print("You guesses the right number. Good guess.")
