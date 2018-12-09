from data import dataset


#    Створити пакет validators та написати функції, що валідують усі дані. Імпорутвати дані функції.

from validators.lib import getNameauto
from validators.lib import getraceName
from validators.lib import getball


from task1 import addUserAuto


#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник.
#   Усі дані вводить користувач. Використати валідатори. Викликати функцію
def addUserAutoValidator():
    user_auto =getNameauto ()

    while not user_auto:
        print("Error in auto. Try again")
        user_email = getNameauto()




    name_race = getraceName()

    while not name_race:
        print("Error in auto. Try again")
        name_race = getraceName()


    ball = getball()

    while not ball:
        print("Error in ball. Try again")
        ball = getball()
        ball = str(ball)

        addUserAuto(user_auto, name_race, ball)



print("Task 1")
addUserAutoValidator()
print(dataset)


print("\n\n")