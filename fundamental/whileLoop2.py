#Repetition using while statements


sandwich_orders=["vegetarian","pastrami","smoked bacon","pastrami","cheesy","BBQ","pastrami"]
print("The Deli has run out of pastramo :( ")


finished_sandwiches=[]

while "pastrami" in sandwich_orders:
   sandwich_orders.remove("pastrami")

while sandwich_orders:
    made=sandwich_orders.pop()
    print("We are making ",made," sandwich.")
    finished_sandwiches.append(made)
