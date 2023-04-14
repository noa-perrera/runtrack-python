def tri_selection(L):
    for i in range(len(L)):
        min_index = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
L_triee = tri_selection(L)
print(L_triee)