def nombres_premier (num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num > 1
for i in range(2, 1001):
    if nombres_premier(i):
        print(i)
