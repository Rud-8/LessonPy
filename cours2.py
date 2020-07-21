

def aucarre (nombre):
    return nombre * nombre

a = aucarre (2)
print (a)


def aucube (nombre):
    return aucarre(nombre) *nombre

r = aucube (2)
print (r)


def puissance4 (nombre):
    return aucarre(nombre) *4

res = puissance4(2)
print (res)

def puissance8 (nombre):
    return puissance4(nombre) *4

resu = puissance8(2)
print (resu)

def puissance32 (nombre):
    return puissance8(nombre) * 8

resul = puissance32(2)

print (resul)