import re

def find_words(search_term: str):
    results = []
    search_term = search_term.lower()

    with open('words.txt') as rf:
        for word in rf:
            word = word.replace('\n', '')
            if '.' in search_term:
                pattern = re.compile(search_term)
                if pattern.match(word) and len(search_term) == len(word):
                    results.append(word)
            elif search_term.startswith('*'):
                if word.endswith(search_term.replace('*', '')):
                    results.append(word)
            elif search_term.endswith('*'):
                if word.startswith(search_term.replace('*', '')):
                    results.append(word)
            elif word == search_term:
                results.append(word)
    return results



#################################################################

print('1 - Add word, 2 - Search, 3 - Quit')
action = int(input('Function:'))

with open('dictionary.txt', 'a') as wf:
    with open('dictionary.txt') as rf:
        while action != 3:
            if action == 1:
                finn = input('The word in Finnish:')
                eng = input('The word in English:')
                wf.write(f'{finn} - {eng}\n')
                print('Dictionary entry added')
            elif action == 2:
                search_term = input('Search term:')
                for line in rf:
                    parsed_line = line.replace('\n', '')
                    # print(parsed_line)
                    # print(search_term in parsed_line)
                    if search_term in parsed_line:
                        print(parsed_line)

            print('1 - Add word, 2 - Search, 3 - Quit')
            action = int(input('Function:'))

        print('Bye!')