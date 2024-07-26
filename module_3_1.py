calls = 0
def count_calls(n):
    global calls
    calls += n
def string_info(string):
    lengh = len(string)
    up = string.upper()
    low = string.lower()
    answer = (lengh, up, low)
    count_calls(1)
    return answer
def is_contains(string, list_to_search):
    s = string.lower()
    list_ = []
    for i in list_to_search:
        list_.append(i.lower())
    if s in list_:
        answer2 = True
    else:
        answer2 = False
    count_calls(1)
    return answer2
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



