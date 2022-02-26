#perform introductory operations on list part 1
#difference between sort() and sorted()


places=["Finland","New Zealand","Australia","Japan","Korea"]
print("Original list:",places)


#sort the list in ascending order without changing the original list
print("\nsorted() in ascending order:",sorted(places))
print("Orginal list:",places)


#sort the list in descending order without changing the original list
print("\nsorted() in descending order:",sorted(places,reverse=True))
print("Orginal list:",places)


#reverse the list
places.reverse()
print("\nOriginal ist after reverse:",places)
places.reverse()
print("\nOriginal list after reverse:",places)


#sort the list in ascending order
places.sort()
print("\nsort() in ascending order:",places)


#sort the list in ascending order
places.sort(reverse=True)
print("\nsort() in descending order:",places)



print("\n*******************************************************\n")
for place in places:
    print("I'm excited to visit "+place+"!")