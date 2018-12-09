
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по атомобілях та спискам їх перегонів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
def recursionByRace(user_auto, name_race, ball= 0):
    if name_race == []:
        return ball

    current_product_list = dataset[user_auto][name_race[0]]

    ball = sum(current_product_list)

    return recursionByRace(user_auto, name_race[1:], ball)

def recursionByauto(user_auto = list(dataset.keys()), result_dict = dict()):
    if user_auto == []:
        return result_dict

    user_auto = user_auto[0]

    product_list = list(dataset[user_auto].keys())

    money = recursionByRace(user_auto, product_list)

    result_dict[user_auto] = money

    return recursionByauto (user_auto[1:], result_dict)


print("Task 3")

result = recursionByauto()
print(result)

print("\n\n")



