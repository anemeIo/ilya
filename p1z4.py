x = input("Введите первый цвет")
x1 = input("Введите второй цвет")
z1= "красный"
z2= "синий"
z3= "желтый"
if (x == z1) and (x1 == z2):
    print("фиолетовый")
elif (x == z1) and (x1 == z3):
    print("оранжевый")
elif (x == z2) and (x1 == z3):
    print("зеленый")
elif (x1 == z1) and (x == z2):
    print("фиолетовый")
elif (x1 == z1) and (x == z3):
    print("оранжевый")
elif (x1 == z2) and (x == z3):
    print("зеленый")
else:
    print("ОШИБКА!!!!!!!!!!!!")