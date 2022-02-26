#Task 1: enter nested loop when encounter key "toppings"
pizza={"crust":"thick","delivery method":"take away","toppings":["mushrooms","extra cheese"]}
print("****************************")
print("Note:")
for requests in pizza:
    if requests=="toppings":
        print("\nContains toppings:")
        for topping in pizza["toppings"]:
            print(topping.title())
    else:
        print("\n"+requests.title()+": "+pizza[requests].title())
print("*******************************************************")
print()

#Task 2: Display everyone's favourite language(s)
fav_languages={"jen":["python","ruby"],
               "sarah":["c"],
               "edward":["ruby","go"],
               "phil":["python","haskell"]}

for name in fav_languages:

    if len(fav_languages[name])>1:
         print(name.title()+"'s favourite languages are",end=" ")
         i=0
         for language in fav_languages[name]:
           if i<(len(fav_languages[name])-1):
                print(language.title(),",",end=" ")
           else:
               print(language.title())
           i+=1

    else:
       print(name.title()+"'s favourite language is",end=" ")
       print(fav_languages[name][0].title())
print("*******************************************************")