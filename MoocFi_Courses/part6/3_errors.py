def read_input(prompt, min, max):
    while True:
        try:
            val = int(input(prompt))
            if min<=val<=max:
                print(f'You typed in: {val}')
                return val
            else:
                print(f'You must type in an integer between {min} and {max}')
        except ValueError:
            print(f'You must type in an integer between {min} and {max}')

