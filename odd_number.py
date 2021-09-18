def odd_numbers(n):
    return [x for x in range(n+1) if x % 3 == 0]


print(odd_numbers(10))