cost=eval(input("Enter the cost (in Rand):\n"))
deposite=eval(input("Deposit a coin or note (in Rand):\n"))
while cost>deposite:
    d=eval(input("Deposit a coin or note (in Rand):\n"))
    deposite+=d

change=deposite-cost

curr = [50, 20, 10, 5, 2, 1]

if (change>0):
    
    print("Your change is :")

    for i in curr:
        dev = change//i
        if dev > 0:
            print(dev, "x", "R"+str(i))
        change = change % i
else:
    print("You have no change")