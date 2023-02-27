x = int(input("введите номер"))
if (x % 2 == True) and (x < 5 ):
    print("верхнее купе")
if (x % 2 == False) and (x < 5):
        print("нижнее купе")
if (x % 2 == True) and (x > 4):
    print ("верхнее боковое")
if (x % 2 == False) and (x > 4):
    print ("нижнее боковое")
