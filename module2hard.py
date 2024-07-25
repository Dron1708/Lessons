def numbers(answer):
    res = []
    for i in range(1,20):
        for j in range(1,20):
            if answer % (i + j) == 0 and (i, j) not in res and (j, i) not in res and i != j:
                res.append((i, j))

    return res
res = numbers(int(input('ввеи число от 3 до 20 ')))
print(res)
