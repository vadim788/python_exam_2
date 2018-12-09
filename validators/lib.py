
"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getNameauto():

    user_input = input("Enter name auto ")

    if (re.match(r"^[A-Z]{1,2}\-[1-9]{1,4}$", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
"""

def getraceName():

    user_input = input("Enter race name ")

    if (re.match(r"^[a-z]+\.[a-z]+$", user_input)):
        return user_input
    else:
        return False



"""
    Написати валідатор ....
    Правило валідації
"""


def getball():
    user_input = input("Enter ball ")
    if (re.match(r"^[1-9]+\.[1-9]{1,2}$",user_input)):
        return user_input
    else:
        return False
