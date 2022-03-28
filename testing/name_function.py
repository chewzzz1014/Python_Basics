# tested in test1.py


def formatted_name(first, last, middle=""):
    if middle:
        return (first+" "+middle+" "+last).title()
    else:
        return (first+" "+last).title()

def print_formatted_name(name):
    print("Hello,", name,"!")

if __name__ == "__main__":
    print("Accessing formatted_name from name_function.py")
    print_formatted_name ( formatted_name( input("Enter first name: "), input("Enter last name: ")) )
