numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_primes = []
for i in range(2, len(numbers) + 1):
    for j in Primes:
            if i % j == 0:
                Not_primes.append(i)
                break
    else:
       Primes.append(i)
print(Primes)
print(Not_primes)
