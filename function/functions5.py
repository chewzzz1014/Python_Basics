#introductory operations of functions part 5
#To show that function will not excute without been called


def make_pizza (size, *toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)