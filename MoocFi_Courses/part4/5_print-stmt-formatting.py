def formatted(my_list):
    result = []
    for i in my_list:
        result.append(f'{i:.2f}')
    return result

names =  [ "Steve", "Jean", "Katherine", "Paul" ]
for name in names:
  # right padding and left padding
  print(f"{name:15} centre {name:>15}")
