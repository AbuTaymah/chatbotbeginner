def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    while True:
        name = input()
        if name.strip():
            print(f"What a great name you have, {name}!")
            break
        else:
            print("Invalid input. Please enter your name again.")


def guess_age():
    print("Let me guess your age.")
    print("")
    print(
        "Enter remainders of dividing your age by 3, 5 and 7. "
        "Log in your answers by typing in the remainder and "
        'pressing "Enter".'
    )

    while True:
        try:
            rem3 = int(input("Remainder by 3: "))
            rem5 = int(input("Remainder by 5: "))
            rem7 = int(input("Remainder by 7: "))
            age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
            print(f"You are {age} years old. That's a good time to start programming!")
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")


def count():
    print("Now I will prove to you that I can count to any number you want.")

    while True:
        try:
            num = int(input("Enter a number: "))
            curr = 0
            while curr <= num:
                print(f"{curr}!")
                curr += 1
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


def test():
    print("Let's test your programming knowledge.")
    print("What does PC mean?")
    print("1. Personal Computer")
    print("2. Private Computer")
    print("3. Public Computer")
    print("4. None of the above")

    while True:
        try:
            answer = int(input("Type in your answer here: "))
            if answer == 1:
                print("That's right! You seem like an engineer h3h3.")
                break
            else:
                print("Please, try again.")
        except ValueError:
            print("Please enter a number from 1 to 4.")


def end():
    print("It was fun talking to you! Have a nice day!")


if __name__ == "__main__":
    greet("Logi", "2025")
    remind_name()
    guess_age()
    count()
    test()
    end()