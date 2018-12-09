from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserAuto(name_auto, name_race, ball):
    if name_auto in dataset:
        if name_race in dataset[name_auto]:
            new_auto = dataset[name_auto][name_race]
            new_auto.append(ball)
        else:
            dataset[name_auto][name_race]=[ball]
    else:
        dataset[name_auto]={name_race:[ball]}




print("Task 1")

#Додати нового користувача та нову покупку
addUserAuto("BB-1111","race",45.5)

#Додати існуючому користувачу нову покупку нового продукту
addUserAuto("AA-4444","racing",32.1)

#Додати існуючому користувачу нову покупку існуючого продукту
addUserAuto("AA-4444","race_win",23)
addUserAuto("AA","race_win",24)

print(dataset)


print("\n\n")