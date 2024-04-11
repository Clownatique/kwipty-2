from logique.logique import Point, Vecteur, Plan
import json

def generer_donnes_exo():
    xml = []
    c = Point(name = 'C')
    n = Vecteur(nom_vecteur = 'n', randomVecteur=True)
    p = Plan('p', Point1 = c, VecteurNormale = n)
    question1 = f'''On considère le plan P qui passe par le point C{(c.x, c.y, c.z)} et dont le vecteur n{(n.x, n.y, n.z)} est un vecteur normal. Déterminer une equation cartésienne de ce plan.'''
    xml.append(question1)
    correction1 = f'''D’après le cours, n{(n.x, n.y, n.z)} est un vecteur normal, donc P admet une equation cartésienne de la forme ax+by+cz+d, ou d est un réel.
De plus C{(c.x, c.y, c.z)} appartient à P, donc les coordonnées du point C vérifient l’´equation ci-dessus.
Donc, une équation cartésienne de P est {p.calculer_equation_cartesienne(n,c)}'''
    xml.append(correction1)
    return xml[]

print(generer_donnes_exo())
