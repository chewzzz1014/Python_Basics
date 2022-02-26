#introductory declaration and operations of dictionary

#dict 1
favs={"food":"noodles","song":"My Time","sliblings":["Alex","Zaid","Lynn"]}

#access to elements in dict 1
print(favs["food"])
print(favs["sliblings"][2])
fav_food=favs["food"]
print("Do you like "+fav_food+" ?")

#update values
favs["place"]="Finland"
favs["languages"]="Python"
print(favs)
print("********************************************************")

#dict 2
bioinfo_1={"first_name":"Zi Qing","last_name":"Chew","city":"Kuala Lumpur"}

#access values in dict 2
print("\tAbout me\n"+"First name: "+bioinfo_1["first_name"]+"\n"+
      "Last name: "+bioinfo_1["last_name"]+"\n"+"City: "+bioinfo_1["city"]+"\n\n")
print("********************************************************")

#dict 3
fav_num={"Zeke":34,"Stanley":12,"Ivan":45,"Stephanie":45}

#print dict 3 values in ascending order
for num in sorted(fav_num.values()):
    print("Do you like "+str(num)+".")
print("********************************************************")