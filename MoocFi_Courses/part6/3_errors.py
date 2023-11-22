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



def new_person(name: str, age: int):
    if name == '' or len(name.split(' '))<2 or len(name)>40 or age<0 or age>150:
        raise ValueError('Something went wrong')
    else:
        return (name, age)


def filter_incorrect():
    with open('lottery_numbers.csv') as rf:
        with open('correct_numbers.csv', 'w') as wf:
            for line in rf:
                try:
                    parsed_line = line.replace('\n', '').split(';')
                    week = parsed_line[0].split(' ')
                    week_num = int(week[1])

                    nums = parsed_line[1].split(',')
                    parsed_nums = []
                    for n in nums:
                        if 1<=int(n)<=39 and int(n) not in parsed_nums:
                            parsed_nums.append(int(n))

                    if week[0]=='week' and len(parsed_nums)==7:
                        wf.write(line)
                except:
                    continue



