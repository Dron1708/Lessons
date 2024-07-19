my_dict = {'Kolya': 2000, 'Anna': 1999, 'Max': 1993}
print(my_dict)
print(my_dict.get('Max'))
print(my_dict.get('Olya'))
q = my_dict.pop('Kolya')
print(q)
print(my_dict)
my_set = {1, 1, 1, 'klap', True, True, 5, 5}
print(my_set)
my_set.add((1, 2, 3, 4))
my_set.add(1.138)
my_set.remove(1)
print(my_set)