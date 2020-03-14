cost=eval(input("Enter the cost (in Rand):\n"))
deposite=eval(input("Deposit a coin or note (in Rand):\n"))
while cost>deposite:
    d=eval(input("Deposit a coin or note (in Rand):\n"))
    deposite+=d

change=deposite-cost
print("Your change is:")
if change>=50:
    x=int(change/50)
    print(x ,"x R50")
    change= change-(x*50)

if change>=20:
    x=int(change/20)
    print(x ,"x R20")
    change= change-(x*20)

if change>=10:
    x=int(change/10)
    print(x ,"x R20")
    change= change-(x*10)

if change>=5:
    x=int(change/5)
    print(x ,"x R5")
    change= change-(x*5)

if change>=2:
    x=int(change/2)
    print(x ,"x R2")
    change= change-(x*2)

if change>=1:
    x=int(change/1)
    print(x ,"x R1")
    change= change-(x*1)
    


              