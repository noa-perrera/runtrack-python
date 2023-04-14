L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

sum = 0
for P in L:
    if P % 2 == 0:
        sum += P

print(sum)