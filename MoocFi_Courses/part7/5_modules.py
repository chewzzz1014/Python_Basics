from string import ascii_letters, digits

def change_case(orig_string: str):
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    half = len(orig_string)//2
    return (orig_string[:half],orig_string[half:])

def remove_special_characters(orig_string: str):
    return "".join([x for x in orig_string if x in ascii_letters or x in digits or x == ' '])
