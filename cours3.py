

def sortie (cas, malade, gueris):
    j = 0
    g = 0
    while (cas >=0):
        cas = cas+ malade - gueris
        j = j+1
        c = c + malades
        g = g + gueris
    annees = j//365
    mois = (j%365)//30
    jours = (j%365)%30

    return (c, g, annees, mois, jours)

print ("il faudra, sortie(10000, 20, 30)[2], "annees, ", sortie(10000 , 20 , 30)