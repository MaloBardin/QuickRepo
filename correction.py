def multiplyv2(a:int,b:int)->int:
    """
        :param a:entier n°1
        :param b:entier n°2
        :return: produit de a par b
    """

    if b<0: #gérer le signe de a et de b
        return -multiplyv2(a,-b)
    if a<0:
        return -multiplyv2(-a,b)

    if b>a: #inversion du b et du a pour multiplier par le plus petit (était-ce la mini opti ?)
        a,b =b,a

    pairespower2=[]#stockage de tuple
    k=1
    tempo=a

    while k<=b: #tant que la puissance de 2k ne dépasse pas b
        pairespower2.append((k,tempo))
        k,tempo=k+k,tempo+tempo

    resultat=0
    while len(pairespower2)!=0: #tant qu'il reste un couple dans ma liste de tuple
        k,tempo = pairespower2.pop() #recuperer le plus important a chaque fois
        if k<=b:
            resultat,b=resultat+tempo,b -k

    return resultat

print(multiplyv2(0, 5))
print(multiplyv2(-9, 0))
print(multiplyv2(0, 0))
print(multiplyv2(-9, -5))
print(multiplyv2(9, 5))
print(multiplyv2(-9, 5))
print(multiplyv2(900, -500))


#utilisation des opérations binaires donc pas autorisé mais toujours intéréssant je trouve
def multiple_logrecursif(a:int,b:int)->int:
    """
    :param a: entier n°1
    :param b: entier n°2
    :return: produit de a par b
    """
    if abs(a)<abs(b):#réduire le nombre d'étape inversion de a et b
        return multiple_logrecursif(b,a)

    if b<0:#gestion du négatif
        return -multiple_logrecursif(a,-b)
    if b==0:#condition d'arret
        return 0
    if b&1:# cas impair
        return a+multiple_logrecursif(a+a,b>>1)

    return multiple_logrecursif(a+a,b>>1)

print("Résultats pour la multiplication récursive o(log(n))")
print(multiple_logrecursif(-9, -3)) #27
print(multiple_logrecursif(9, 3)) #27
print(multiple_logrecursif(9, -3)) #-27
print(multiple_logrecursif(-9, 3))