def statement_generator(statement, decoration):

    sides = decoration * 3

    statement =  "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# main routine goes here
statement_generator("Welcome to my quiz,Enjoy", "*")
print()
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
    print("Answer questions correctly and enjoy the quiz")
    print()
    return ""


# Main routine goes here...
played_before = yes_no("Have you played the game before")


if played_before == "no":
    instructions()

print("Program continues")

