def check_type_and_season(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("rien.")

check_type_and_season("fruits", "hiver")
check_type_and_season("fruits", "ete")
check_type_and_season("legume", "hiver")
check_type_and_season("legume", "ete")
check_type_and_season("sport", "ete")