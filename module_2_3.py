my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# for number in my_list:
#      if number > 0:
#          print(number)
#      elif number < 0:
#          break

i = 0
while i in range(len(my_list)):
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i += 1



