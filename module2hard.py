def numbers(answer):
    res = []
    for i in range(1,answer):
        for j in range(i+1,answer+1):
            if answer % (i + j) == 0 and (i, j) not in res and (j, i) not in res:
                res.append((i, j))

    return res
res = numbers(int(input('ввеи число от 3 до 20 ')))
print(*res)
