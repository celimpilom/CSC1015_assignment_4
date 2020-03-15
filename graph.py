import math

f_x_str = input("Enter a function f(x):\n") #function as a string

for y in range(10 , -11 , -1 ): #loop with y

    for x in range(-10, 11):

        f_x = eval(f_x_str)

        if y == int(f_x):
            print("o", end = '')

        elif y == 0 and x == 0 :
            print("+", end = '')

        elif y == 0:
            print("-", end = '')

        elif x == 0:
            print("|", end = '')

        else:
            print(" ", end = '')

    print()