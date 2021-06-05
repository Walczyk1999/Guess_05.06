def your_choice():
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")

    return result


def guess_number():
    import random
    random_number = random.randint(1, 100)
    choice = your_choice()
    while choice != random_number:
        if choice > random_number:
            print("Too big!")
        else:
            print("Too low!")
        choice = your_choice()
    print("You Win!")


guess_number()
