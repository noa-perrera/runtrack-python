def type_de_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Pas un triangle"
    elif a == b == c:
        return "Triangle équilatéral"
    elif a == b or a == c or b == c:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "Triangle rectangle isocèle"
        else:
            return "Triangle isocèle"
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return "Triangle rectangle"
    else:
        return "Triangle quelconque"
    
resultat = type_de_triangle(3, 4, 5)
print(resultat)
resultat1 = type_de_triangle(20, 15, 16)
print(resultat1)
resultat2 =  type_de_triangle( 5, 5, 5 )
print(resultat2)
resultat3 = type_de_triangle(7, 1, 30)
print(resultat3)