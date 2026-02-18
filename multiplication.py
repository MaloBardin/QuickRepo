def multiple_fullrecursif(a:int,b:int,s:int=0)->int:
    """
    :param a: entier n°1
    :param b: entier n°2
    :param s: somme temporaire
    :return: produit de a par b
    """
    if b<0:
        return -multiple_fullrecursif(a,-b,s)
    if b==0:
        return s
    return multiple_fullrecursif(a,b-1,s+a)

print("Résultats pour la multiplication récursive o(n)")
print(multiple_fullrecursif(-9, -3)) #27
print(multiple_fullrecursif(9, 3)) #27
print(multiple_fullrecursif(9, -3)) #-27
print(multiple_fullrecursif(-9, 3)) #-27

def multiple_logrecursif(a:int,b:int,s:int=0)->int:
    """
    :param a: entier n°1
    :param b: entier n°2
    :param s: somme temporaire
    :return: produit de a par b
    """
    if b<0:
        return -multiple_logrecursif(a,-b, s)
    if b ==0:
        return s
    if b%2== 1: #gérer le cas impair
        s+=a
    return multiple_logrecursif(a+a,b//2,s)

print("Résultats pour la multiplication récursive o(log(n))")
print(multiple_logrecursif(-9, -3)) #27
print(multiple_logrecursif(9, 3)) #27
print(multiple_logrecursif(9, -3)) #-27
print(multiple_logrecursif(-9, 3))

def division_basique(a:int)->float:
    """
    :param a: un entier classique
    :return: le flotant résultant de la division par 2 de a
    """
    return a*0.5

def division_shift(a:int)->int:
    """
    :param a: un entier classique
    :return: la division de a par 2 arrondi a l'entier inférieur
    """
    return a>>1

print("Division multiplication inverse et décalage shift :")
print(division_basique(10))
print(division_shift(10))
print(division_basique(-10))
print(division_shift(-10))
print(division_basique(3))
print(division_shift(3))
print(division_basique(-3))
print(division_shift(-3))
