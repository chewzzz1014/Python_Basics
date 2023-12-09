from datetime import timedelta


def cheaters():
    exam_data = {}
    cheaters_list = []

    with open('start_times.csv') as rf:
        for line in rf:
            parsed_vals = line.replace('\n', '').split(';')

            name = parsed_vals[0]
            start_time = list(map(int, parsed_vals[1].split(':')))

            exam_data[name] = {
                'start_time': timedelta(hours=start_time[0], minutes=start_time[1])
            }

    with open('submissions.csv') as rf:
        for line in rf:
            parsed_vals = line.replace('\n', '').split(';')

            name = parsed_vals[0]
            task = parsed_vals[1]
            points = parsed_vals[2]
            end_time = list(map(int, parsed_vals[3].split(':')))

            exam_data[name]['task'] = task
            exam_data[name]['points'] = points
            if 'end_time' not in exam_data[name]:
                exam_data[name]['end_time'] = [timedelta(hours=end_time[0], minutes=end_time[1])]
            else:
                exam_data[name]['end_time'].append(timedelta(hours=end_time[0], minutes=end_time[1]))

    for student in exam_data:
        time_spent = max(exam_data[student]['end_time']) - exam_data[student]['start_time']
        if time_spent.total_seconds() / 3600 > 3:
            cheaters_list.append(student)

    return cheaters_list

# print(cheaters())


########################################################################################

from difflib import get_close_matches

with open('wordlist.txt') as rf:
    suggestions = {}
    words_list = list(map(lambda x: x.replace('\n', '').lower(), rf))

    user_word = input('Write text:')
    result = ''
    for w in user_word.split(' '):
        if w.lower() not in words_list:
            result += f'*{w}* '
            if w not in suggestions:
                suggestions[w] = get_close_matches(w, words_list)
        else:
            result += f'{w} '

    print(result)
    print('suggestions: ')
    for k,v in suggestions.items():
        print(f'{k}: {", ".join(v)}')