
#def nombremax (x, y):
#    x = abs(x)
#    y = abs(y)
#   if (x > y):
#        c = abs(x)
#    elif (x < y):
#        c = abs(y)
#    else:
#       c = y
###    return c
#print (nombremax(-26, -32))

def nombremax(x, y):
    if (x > y):
        c = x
    elif (x < y):
        c = y
    else:
        c = y
    return c

print(nombremax(92, 89))




def nombreabsolu (nbb, nba):
    nbb = abs(nbb)
    nba = abs (nba)
    if nba > nbb:
        resu = nba
    elif nba < nbb:
        resu = nbb
    else:
        resu = nbb
    return resu

print (nombreabsolu(-29, -51))


#def yajeuxdete (x):
#    if
#        jo = true

#def yajeuxdete (x):
 #   J0 = x +4
  #  if x == (1916, 1940, 1944):
   #     resul = False
   # return resul

#print (yajeuxdete(1968))




def yajeuxdete (t):
    annee = t % 4
    param = (1916, 1940, 1944)
    if t < 1896:
        res = False
    elif annee == 0:
        res = True
    elif t in param:
        res = False
    else:
        res = False
    return res

print (yajeuxdete(1892))



def jeuxdhiver(x):
    annee = x % 2
    param = (1916, 1940, 1944)
    if x < 1896:
        res = False
    elif annee == 0:
        res = True
    elif x in param:
        res = False
    else:
        res = False
    return res

print (jeuxdhiver(1994))

def yajeux(r):
    if yajeuxdete(t) or jeuxdhiver(x):
        res = True
    else:
        res = False
    return res

print (yajeuxdete(2002))









        































