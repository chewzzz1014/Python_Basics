#introductory operations of selection statements part 2


available_toppings=["mushroom","olives","green peppers",
                    "pepperoni","pineapple","extra cheese"]

requested_toppings=["mushroom","french fries","extra cheese"]

for requested in requested_toppings:
    if requested in available_toppings:
        print("Adding "+requested+".")
    else:
        print("Sorry, we don't have "+requested+".")

print("\nFinished making your pizza!")