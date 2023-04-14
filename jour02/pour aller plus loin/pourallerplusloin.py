a = 2
b = 2 
c = 3 
def check_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return " pas un triangle"
    elif a == b == c:
        return " triangle équillateral"
    elif a == b or a == c or b == c:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "triangle rectangle isolsel"
        else:
            return"triangle isosel"
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return "triangle requtangle"
    else:
        return "triangle quelquonque"
    resultat = type_de_triangle(3, 4, 5)
print(resultat)
    
