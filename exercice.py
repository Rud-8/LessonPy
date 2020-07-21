def maximum(x , y):
    if x < y:
        resul = y
    elif y < x:
        resul = x
    else:
        resul = y
    return resul

print (maximum(12, 23))


def maximumabsolu(x, y):
    if (abs(x) < abs(y)):
        resul = abs(y)
    elif (abs(y) < abs(x)):
        resul = abs(x)
    else:
        resul = abs(x)
    return resul
print (maximumabsolu(-20, 51))


def jodete(nombre):
    annee = nombre %4
    param = (1916, 1920, 1944)

    if nombre < 1896:
        resul = False
    elif annee == 0:
        resul = True
    elif nombre in param:
        resul = False
    else:
        resul = False
    return resul

print (jodete(1896))


def jeuxdhiver(nombre):
    annee = nombre % 2
    param = (1916, 1940, 1944)
    if nombre < 1896:
        res = False
    elif annee == 0:
        res = True
    elif nombre in param:
        res = False
    else:
        res = False
    return res

print(jeuxdhiver(1994))


def yajeux(year):
    if year == jeuxdhiver(year) or jodete(year):
        res = "Y'a jeux"
    else:
        res = "Y'a pas jeux"
    return res

print(yajeux(1845))



def est_perimee(a,b,c,d,e,f):
    liste = a, b, c, d, e, f
    if liste [0:3] <= liste [4:6]:
        res = True
    else:
        res = False
    return res


print(est_perimee(10,10,2020, 10,10,2019))


def fibo(nombre):
    a = (nombre -1 + nombre -2)
    b = ()
    for i in range(a):
        print(i)
    return 0
fibo(3)





