immutable_var = (1, False, 'qwe')
print(immutable_var)
#immutable_var [0] = 2
print(immutable_var)
print(type(immutable_var [0]))
#Тип int не изменяеммый в кортеже
mutable_list = [1, 2, 3, True, 'qwe']
mutable_list [-2] = False
print(mutable_list)