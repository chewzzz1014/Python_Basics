#nested dictionary

pets={"lih":{"species":"snake","owner":"chewzzz"},
      "jacky":{"species":"dog","owner":"lynn"}}
print("About pets...\n")


class Default(dict):
    def __missing(self,key):
         return key

for pet in pets:
    print("{name} is here!".format_map(Default(name=pet)))
    print("Species: ",pets[pet]["species"])
    print("Owner: ",pets[pet]["owner"])
    print("")


class Foo(dict): # inheriting the dict class
    def __missing__(self,key):
        return key
print('({x},{y})'.format_map(Foo(x='2')))  # missing key y
print('({x},{y})'.format_map(Foo(y='3')))  # missing key x