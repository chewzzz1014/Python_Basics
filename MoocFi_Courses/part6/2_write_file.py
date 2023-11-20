name = input('Whom should I sign this to: ')
file_name = input('Where shall I save it:')
with open(file_name, 'w') as rf:
    rf.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')

with open('diary.txt', 'a') as rf:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    action = int(input('Function'))

    while action != 0:
        if action == 1:
            diary_entry = input('Diary entry:')
            rf.write(diary_entry + '\n')
            print('Diary saved')
        elif action == 2:
            with open('diary.txt') as rf1:
                for line in rf1:
                    print(line.replace('\n', ''))
        print('1 - add an entry, 2 - read entries, 0 - quit')
        action = int(input('Function'))
print('Bye now!')

def write_to_file(file_name, content):
    with open(file_name, 'a') as rf:
        rf.write(content)
def filter_solutions():
    # clear files first
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()

    with open('solutions.csv') as rf:
        for line in rf:
            parsed_vals = line.replace('\n', '').split(';')
            expression = parsed_vals[1].split('+')
            operation = '+'
            if len(expression) < 2:
                expression = parsed_vals[1].split('-')
                operation = '-'
            print(expression)

            if operation == '+':
                if (int(expression[0]) + int(expression[1])) == int(parsed_vals[2]):
                    write_to_file('correct.csv', line)
                else:
                    write_to_file('incorrect.csv', line)
            elif operation == '+':
                if (int(expression[0]) - int(expression[1])) == int(parsed_vals[2]):
                    write_to_file('correct.csv', line)
                else:
                    write_to_file('incorrect.csv', line)