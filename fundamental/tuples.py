#introductory practices on tuple
#show that values of tuple can't be changed but tuple can be redeclared

buffet=("Crabs","Sushi","Meatballs","Cakes","Soup")
buffet=("Meat","Ice cream","Meatballs","Cakes","Soup")
for meal in buffet:
    print(meal)


buffet[0] = "Ice Cream"