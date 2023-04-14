def fruits():
    x = ["pomme","cerise","orange"]
    return(','.join(x))
    

print (fruits() + ',' + ','.join(["melon"]))
print (fruits())