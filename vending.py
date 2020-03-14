cost=eval(input("Enter the cost (in Rand):\n"))
deposite=eval(input("Deposit a coin or note (in Rand):\n"))
while cost>deposite:
    d=eval(input("Deposit a coin or note (in Rand):\n"))
    deposite+=d
change=deposite-cost
print("Your change is:\n")
if not change==50 and change==20 and change==5 and change==2 and change==1:
    
    
else:
    print("Your change is:\n",change)
    


              