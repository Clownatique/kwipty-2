from sympy import symbols, Eq
from sympy.vector import CoordSys3D
from random import randrange

# Déclaration des variables symboliques
x, y, z = symbols('x y z')

# Déclaration du système de coordonnées
N = CoordSys3D('N')

# Génération de coefficients aléatoires
a1, b1, c1, d1 = randrange(-5, 5), randrange(-5, 5), randrange(-5, 5), randrange(-5, 5)
a2, b2, c2, d2 = randrange(-5, 5), randrange(-5, 5), randrange(-5, 5), randrange(-5, 5)
a3, b3, c3, d3 = randrange(-5, 5), randrange(-5, 5), randrange(-5, 5), randrange(-5, 5)

# Définition des plans P1, P2 et P3
P1 = Eq(a1 * x + b1 * y + c1 * z + d1, 0)
P2 = Eq(a2 * x + b2 * y + c2 * z + d2, 0)
P3 = Eq(a3 * x + b3 * y + c3 * z + d3, 0)

# Affichage des équations des plans
print(f"P1 : {P1}")
print(f"P2 : {P2}")
print(f"P3 : {P3}")

# 1. Détermination du vecteur normal à chaque plan
n1 = N.i * a1 + N.j * b1 + N.k * c1
n2 = N.i * a2 + N.j * b2 + N.k * c2
n3 = N.i * a3 + N.j * b3 + N.k * c3

# Vecteur w aléatoire avec SymPy
w = N.i * randrange(-5, 5) + N.j * randrange(-5, 5) + N.k * randrange(-5, 5)

# Vérification de la colinéarité de w avec n3
if w.is_colinear(n3):
    print("\n1. Le vecteur w est normal au plan P3.")
else:
    print("\n1. Le vecteur w n'est pas normal au plan P3.")

# 2. Vérification de l'orthogonalité des plans P2 et P3
if n2.dot(n3) == 0:
    print("\n2. Les plans P2 et P3 sont perpendiculaires.")
else:
    print("\n2. Les plans P2 et P3 ne sont pas perpendiculaires.")
