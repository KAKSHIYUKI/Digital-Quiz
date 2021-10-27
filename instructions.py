# functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("Answer questions correctly and enjoy the quiz by typing 1,2,3 on your keyboard")
    print()
    return ""


# Main routine goes here...
played_before = yes_no("Have you completed a quiz before?")


if played_before == "no":
    instructions()

print("Program continues (score will be shown at end)")

