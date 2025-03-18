amount = int(input("Enter amount of your bill"))
if amount<=1000:
    print("You are eligible for 10% discount")
    disc = amount - ((10/100)*amount)
    print("Your final bill is",disc)
elif amount>1000 and amount<=5000:
    print("You are eligible for 20% discount")
    disc = amount - ((20/100)*amount)
    print("Your final bill is",disc)
elif amount>5000 and amount<=10000:
    print("You are eligible for 30% discount")
    disc = amount - ((30/100)*amount)
    print("Your final bill is",disc)
else:
    print("You are eligible for 50% discount")
    disc = amount - ((50/100)*amount)
    print("Your final bill is",disc)