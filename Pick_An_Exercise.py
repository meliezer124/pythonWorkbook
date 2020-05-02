## Picks a random exercise based on random number, by category
import random as rand

intro_to_programming = 1
if_statements = 2
loops =3
functions = 4
lists = 5
dictionaries = 6
files_and_exceptions = 7
recursions = 8

def exercise_number(beg, end):
    result = rand.randint(beg, end)
    print("Do exercise number {}".format(result))


selection = int(input("Please pick one of the following categories: \n"
                      "1: Intro to Programming\n"
                      "2: If Statements\n"
                      "3: Loops\n"
                      "4: Functions\n"
                      "5: Lists\n"
                      "6: Dictionaries\n"
                      "7: Files and Exceptions\n"
                      "8: Recursions\n\n"))
if selection == intro_to_programming:
    exercise_number(1,33)
elif selection == if_statements:
    exercise_number(34, 60)
elif selection == loops:
    exercise_number(61, 80)
elif selection == functions:
    exercise_number(81, 103)
elif selection == lists:
    exercise_number(104, 127)
elif selection == dictionaries:
    exercise_number(128, 140)
elif selection == files_and_exceptions:
    exercise_number(141,163)
else:
    exercise_number(164,174)

