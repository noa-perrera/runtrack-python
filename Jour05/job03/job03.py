def diagonale(n):
    for i in range(n + 1):
        print('#' * (n - i) + '/' + '#' * i)
diagonale(5)