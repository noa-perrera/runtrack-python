def my_long_word(n, phrase):
    mots = phrase.split()
    mots_long = []
    for mot in mots:
        if len(mot) > n:
            mots_long.append(mot)
    return ' '.join(mots_long)

phrase = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
resultat = my_long_word(3, phrase)
print(resultat)