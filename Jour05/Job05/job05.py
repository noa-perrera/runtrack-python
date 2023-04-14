def distance_parcourue(nbr_marches: int, hauteur_marche: int) -> float:
    distance_jour = 2 * 5 * nbr_marches * hauteur_marche
    distance_jour = distance_jour / 100
    distance_semaine = distance_jour * 7
    return distance_semaine

nbr_marches = 10
hauteur_marche = 20
resultat = distance_parcourue(nbr_marches, hauteur_marche)
print(f"Pour {nbr_marches} marches de {hauteur_marche} cm, le gardien parcours {resultat:.2f} m par semaine.")