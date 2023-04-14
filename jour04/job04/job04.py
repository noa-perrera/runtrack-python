def fruits():
    x = ["pomme", "cerise", "orange"]
    return x

x = fruits()
x.insert(2, "mangue")
print(','.join(x))
print(','.join(fruits()))