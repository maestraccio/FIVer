#!/usr/bin/python3
import os, pathlib
import random
from datetime import *
from os.path import expanduser
from time import sleep

#   Written by Maestraccio
#
#     /7/7/7
#    __|_|_|_o-
#   / /! | |
#   \ L'/! |
#    \  L' |
#     \___/

versie = "2.00"
datum = "20230909"
plaats = "Pedara"
print(versie,datum,plaats)

ResetAll               = "\033[0m"
Bold                   = "\033[1m"
Dim                    = "\033[2m"
Underlined             = "\033[4m"
Blink                  = "\033[5m"
Reverse                = "\033[7m"
Hidden                 = "\033[8m"
ResetBold              = "\033[21m"
ResetDim               = "\033[22m"
ResetUnderlined        = "\033[24m"
ResetBlink             = "\033[25m"
ResetReverse           = "\033[27m"
ResetHidden            = "\033[28m"
Default                = "\033[39m"
Black                  = "\033[30m"
Red                    = "\033[31m"
Green                  = "\033[32m"
Yellow                 = "\033[33m"
Blue                   = "\033[34m"
Magenta                = "\033[35m"
Cyan                   = "\033[36m"
LightGray              = "\033[37m"
DarkGray               = "\033[90m"
LightRed               = "\033[91m"
LightGreen             = "\033[92m"
LightYellow            = "\033[93m"
LightBlue              = "\033[94m"
LightMagenta           = "\033[95m"
LightCyan              = "\033[96m"
White                  = "\033[97m"
BackgroundDefault      = "\033[49m"
BackgroundBlack        = "\033[40m"
BackgroundRed          = "\033[41m"
BackgroundGreen        = "\033[42m"
BackgroundYellow       = "\033[43m"
BackgroundBlue         = "\033[44m"
BackgroundMagenta      = "\033[45m"
BackgroundCyan         = "\033[46m"
BackgroundLightGray    = "\033[47m"
BackgroundDarkGray     = "\033[100m"
BackgroundLightRed     = "\033[101m"
BackgroundLightGreen   = "\033[102m"
BackgroundLightYellow  = "\033[103m"
BackgroundLightBlue    = "\033[104m"
BackgroundLightMagenta = "\033[105m"
BackgroundLightCyan    = "\033[106m"
BackgroundWhite        = "\033[107m"
Kies                   = LightBlue
Ronde                  = Green
Bevestiging            = LightCyan
Gefeliciteerd          = LightMagenta
Goed                   = LightGreen
Tabel                  = Yellow
Resultaat              = LightYellow
Slecht                 = LightRed
Tekst                  = Reverse
Terug                  = DarkGray
Wit                    = White
forr2 = "{:>2}".format
forc3 = "{:^3}".format
inputindent = "  : "
afsluitlijst=["X","Q"]


def nicklijst(init):
    if init == "A":
        nicks = [" the Awesome"," the Admirable", " the Amazing", " the Annihilator"]
    elif init == "B":
        nicks = [" the Bright"," the Brave", " the Bold", " the Bulldozer", " "]
    elif init == "C":
        nicks = [" the Cool", " the Competent", " the Capable", " the Crusher"]
    elif init == "D":
        nicks = [" the Daring", " the Decisive", " the Dutiful", " the Doom"]
    elif init == "E":
        nicks = [" the Earnest", " the Eager", " the Efficient", " the Evil"]
    elif init == "F":
        nicks = [" the Fabulous", " the Fair", " the Ferocious", " the Feared"]
    elif init == "G":
        nicks = [" the Good", " the Gifted", " the Great", " the Grinder"]
    elif init == "H":
        nicks = [" the Honorable", " the Hearty", " the Heroic", " the Hard"]
    elif init == "I":
        nicks = [" the Incredible", " the Impressive", " the Impredictible", " the Invincible"]
    elif init == "J":
        nicks = [" the Jovial", " the Joker", " the Just", " the Jinxed"]
    elif init == "K":
        nicks = [" the Knowledgeable", " the Kind", " the Keen", " the Knocker"]
    elif init == "L":
        nicks = [" the Lucky", " the Lean", " the Loveable", " the Leavealoser"]
    elif init == "M":
        nicks = [" the Mighty", " the Majestic", " the Mean", " the Monster"]
    elif init == "N":
        nicks = [" the Noble", " the Neat", " the Natural", " the Notorious"]
    elif init == "O":
        nicks = [" the Ominous", " the Outrageous", " the Overwhelming", " the Obstinate"]
    elif init == "P":
        nicks = [" the Powerful", " the Polite", " the Peaceful", " the Piranha"]
    elif init == "Q":
        nicks = [" the Quick", " the Quizzical", " the Qualified", " the Quaint"]
    elif init == "R":
        nicks = [" the Righteous", " the Rebellious", " the Radiant", " the Ravishing"]
    elif init == "S":
        nicks = [" the Strong", " the Supreme", " the Skilful", " the Shocking"]
    elif init == "T":
        nicks = [" the Talented", " the Tactful", " the Thoughtful", " the Torturer"]
    elif init == "U":
        nicks = [" the Unbeatable", " the Unexpected", " the Unequalled", " the Unbendable"]
    elif init == "V":
        nicks = [" the Victorious", " the Versatile", " the Virtuoso", " the Vicious"]
    elif init == "W":
        nicks = [" the Wise", " the Warm", " the Wonderful", " the Wrecker"]
    elif init == "X":
        nicks = [" the Xpert", " the Xtraordinary", " the Xcellent", " the Xtruder"]
    elif init == "Y":
        nicks = [" the Yedi", " the Yoda", " the Younghearted", " the Yahtzee"]
    elif init == "Z":
        nicks = [" the Zealous", " the Zodiac", " the Zoroaster", " the Zapper"]
    else:
        nicks = [""]
    nick = random.choice(nicks)
    return nick

print()
langsel = input("Choose your langauge | Scegli la tua lingua | Kies uw taal\n >1 : English\n  2 : Italiano\n  3 : Nederlands\n%s" % inputindent)
if langsel.upper() in afsluitlijst:
    exit()
elif langsel == "2":
    lang = "IT"
    scorelijst = ["1","2","3","4","5","6","Subtot Sopra","Bonus 35 se SS >= 63","Totale Sopra","Tre Uguali","Quattro Uguali","Full House","Piccola Scala","Grande Scala","F I V er","Scelta Libera","Totale Sopra","Totale Sotto","TOTALE"]
    allespelers = "Tutti i Giocatori"
    nog = "Avanzamento"
    speelt = "È l'opportunità di "
    ronde = "Turno"
    welkveld = "In %squale campo%s desideri registrare il tuo punteggio?\n%s" % (Kies,ResetAll,inputindent)
    welkewaarde = "Punteggio:\n%s" % (inputindent)
    waardeongeldig = "%sPunteggio invalido%s" % (Slecht,ResetAll)
    veldongeldig = "%sCampo invalido%s" % (Slecht,ResetAll)
    veldbezet = "%sCampo occupato%s" % (Slecht,ResetAll)
    tekort = "Da recuperare: "
    over = "Margine di manovra: "
    totbonus = "Fino al Bonus: "
elif langsel == "3":
    lang = "NL"
    scorelijst = ["1","2","3","4","5","6","Subtot Boven","Bonus 35 als SB >= 63","Totaal Boven","Drie Dezelfde","Vier Dezelfde","Full House","Kleine Straat","Grote Straat","F I V er","Vrije Keus","Totaal Boven","Totaal Onder","TOTAAL"]
    allespelers = "Alle Spelers"
    nog = "Voortgang"
    speelt = "De beurt is aan "
    ronde = "Ronde"
    welkveld = "In %swelk veld%s wil je je score registreren?\n%s" % (Kies,ResetAll,inputindent)
    welkewaarde = "Score:\n%s" % (inputindent)
    waardeongeldig = "%sOngeldige score%s" % (Slecht,ResetAll)
    veldongeldig = "%sOngeldig veld%s" % (Slecht,ResetAll)
    veldbezet = "%sVeld al in gebruik%s" % (Slecht,ResetAll)
    tekort = "In te halen: "
    over = "Speelruimte: "
    totbonus = "Tot aan de Bonus: "
else:
    lang = "EN"
    scorelijst = ["1","2","3","4","5","6","Subtot Upper","Bonus 35 if SU >= 63","Total Upper","Three of a Kind","Four of a Kind","Full House","Small Straight","Large Straight","F I V er","Free Choice","Total Upper","Total Lower","TOTAL"]
    allespelers = "All Players"
    nog = "Progress"
    speelt = "It's the turn of "
    ronde = "Round"
    welkveld = "In %swhich field%s do you want to record your score?\n%s" % (Kies,ResetAll,inputindent)
    welkewaarde = "Score:\n%s" % (inputindent)
    waardeongeldig = "%sInvalid score%s" % (Slecht,ResetAll)
    veldongeldig = "%sInvalid field%s" % (Slecht,ResetAll)
    veldbezet = "%sField already taken%s" % (Slecht,ResetAll)
    tekort = "Short: "
    over = "Leeway: "
    totbonus = "Until the Bonus: "

maxlinkol = len(max(scorelijst, key = len))
forlinkol = ("{:^%s}" % maxlinkol).format
forllinkol = ("{:<%s}" % maxlinkol).format
forrlinkol = ("{:>%s}" % maxlinkol).format

def verzamelspelers():
    spelerslijst = []
    spelertel = 1
    speler = ""
    while speler.upper() not in afsluitlijst:
        if lang == "IT":
            speler = "Giocatore_%s" % spelertel
            geefnaam = "Inserisci il nome del %s:\n%s" % (speler,inputindent)
        elif lang == "NL":
            speler = "Speler_%s" % spelertel
            geefnaam = "Geef de naam van %s:\n%s" % (speler,inputindent)
        else:
            speler = "Player_%s" % spelertel
            geefnaam = "Enter the name of %s:\n%s" % (speler,inputindent)
        spelersnaam = input(geefnaam)
        if spelersnaam.upper() in afsluitlijst:
            spelersnaam = speler
            spelerslijst.append(spelersnaam)
            break
        elif spelersnaam == "":
            spelersnaam = speler
            spelertel += 1
        else:
            init = spelersnaam[0].upper()
            nick = nicklijst(init)
            spelersnaam = spelersnaam + nick
            print(inputindent+Ronde+spelersnaam+ResetAll)
            spelertel += 1
        spelerslijst.append(spelersnaam)
    return spelerslijst
spelerslijst = verzamelspelers()        
maxspeler = len(max(spelerslijst, key = len))
if maxspeler < 3:
    maxspeler = 3
forspeler = ("{:^%s}" % maxspeler).format

def maakscoretabel():
    scoretabel = []
    for i in spelerslijst:
        i = []
        for j in scorelijst:
            i.append("")
        scoretabel.append(i)
    return scoretabel
scoretabel = maakscoretabel()

def bouwtabel():
    print(Tabel, end = "")
    pluslijn = "+"+"-"*maxlinkol+("+"+"-"*maxspeler)*len(spelerslijst)+"+"
    print(pluslijn)
    print("|"+forlinkol(allespelers),end = "")
    for i in spelerslijst:
            print("|"+forspeler(i), end = "")
    print("|")
    print(pluslijn)
    print("|"+forlinkol(scorelijst[0]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][0]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[1]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][1]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[2]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][2]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[3]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][3]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[4]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][4]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[5]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][5]),end = "")
    print("|")
    print(pluslijn)
    print("|"+forllinkol(scorelijst[6]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][6]),end = "")
    print("|")
    print("|"+forllinkol(scorelijst[7]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][7]),end = "")
    print("|")
    print("|"+forllinkol(scorelijst[8]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][8]),end = "")
    print("|")
    print(pluslijn)
    print("|"+forlinkol(scorelijst[9]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][9]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[10]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][10]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[11]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][11]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[12]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][12]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[13]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][13]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[14]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][14]),end = "")
    print("|")
    print("|"+forlinkol(scorelijst[15]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][15]),end = "")
    print("|")
    print(pluslijn)
    print("|"+forllinkol(scorelijst[16]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][16]),end = "")
    print("|")
    print("|"+forllinkol(scorelijst[17]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][17]),end = "")
    print("|")
    print("|"+forrlinkol(scorelijst[18]), end = "")
    for i in range(len(spelerslijst)):
        print("|"+forspeler(scoretabel[i-1][18]),end = "")
    print("|")
    print(pluslijn)
    print(ResetAll, end = "")
bouwtabel()

def spelertabel(speler):
    pluslijn = "+"+"-"*maxlinkol+"+"+"-"*maxspeler+"+"
    doel = 63
    verschil = 0
    print(pluslijn)
    print("|"+forlinkol(nog)+"|"+forspeler(speler),end = "")
    print("|")
    print(pluslijn)
    if scoretabel[spelerslijst.index(speler)-1][0] != "" and scoretabel[spelerslijst.index(speler)-1][0] < 3*1:
        verschil += scoretabel[spelerslijst.index(speler)-1][0]-(3*1)
        doel -= scoretabel[spelerslijst.index(speler)-1][0]
        print("|"+forlinkol(scorelijst[0]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*1)-scoretabel[spelerslijst.index(speler)-1][0]))+ResetAll,end = "")
        print("|")
        #print("1 = %s%s%s" % (Slecht,"-"+str((3*1)-scoretabel[spelerslijst.index(speler)-1][0]),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][0] != "" and scoretabel[spelerslijst.index(speler)-1][0] > 3*1:
        verschil += scoretabel[spelerslijst.index(speler)-1][0]-(3*1)
        doel -= scoretabel[spelerslijst.index(speler)-1][0]
        print("|"+forlinkol(scorelijst[0]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][0]-(3*1)))+ResetAll,end = "")
        print("|")
        #print("1 = %s%s%s" % (Goed,"+"+str(scoretabel[spelerslijst.index(speler)-1][0]-(3*1)),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][0] != "" and scoretabel[spelerslijst.index(speler)-1][0] == 3*1:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][0]
        print("|"+forlinkol(scorelijst[0]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
        #print("1 = OK")
    if scoretabel[spelerslijst.index(speler)-1][1] != "" and scoretabel[spelerslijst.index(speler)-1][1] < 3*2:
        verschil += scoretabel[spelerslijst.index(speler)-1][1]-(3*2)
        doel -= scoretabel[spelerslijst.index(speler)-1][1]
        print("|"+forlinkol(scorelijst[1]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*2)-scoretabel[spelerslijst.index(speler)-1][1]))+ResetAll,end = "")
        print("|")
        #print("2 = %s%s%s" % (Slecht,"-"+str((3*2)-scoretabel[spelerslijst.index(speler)-1][1]),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][1] != "" and scoretabel[spelerslijst.index(speler)-1][1] > 3*2:
        verschil += scoretabel[spelerslijst.index(speler)-1][1]-(3*2)
        doel -= scoretabel[spelerslijst.index(speler)-1][1]
        print("|"+forlinkol(scorelijst[1]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][1]-(3*2)))+ResetAll,end = "")
        print("|")
        #print("2 = %s%s%s" % (Goed,"+"+str(scoretabel[spelerslijst.index(speler)-1][1]-(3*2)),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][1] != "" and scoretabel[spelerslijst.index(speler)-1][1] == 3*2:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][1]
        print("|"+forlinkol(scorelijst[1]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
        #print("2 = OK")
    if scoretabel[spelerslijst.index(speler)-1][2] != "" and scoretabel[spelerslijst.index(speler)-1][2] < 3*3:
        verschil += scoretabel[spelerslijst.index(speler)-1][2]-(3*3)
        doel -= scoretabel[spelerslijst.index(speler)-1][2]
        print("|"+forlinkol(scorelijst[2]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*3)-scoretabel[spelerslijst.index(speler)-1][2]))+ResetAll,end = "")
        print("|")
        #print("3 = %s%s%s" % (Slecht,"-"+str((3*3)-scoretabel[spelerslijst.index(speler)-1][2]),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][2] != "" and scoretabel[spelerslijst.index(speler)-1][2] > 3*3:
        verschil += scoretabel[spelerslijst.index(speler)-1][2]-(3*3)
        doel -= scoretabel[spelerslijst.index(speler)-1][2]
        print("|"+forlinkol(scorelijst[2]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][2]-(3*3)))+ResetAll,end = "")
        print("|")
        #print("3 = %s%s%s" % (Goed,"+"+str(scoretabel[spelerslijst.index(speler)-1][2]-(3*3)),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][2] != "" and scoretabel[spelerslijst.index(speler)-1][2] == 3*3:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][2]
        print("|"+forlinkol(scorelijst[2]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
        #print("3 = OK")
    if scoretabel[spelerslijst.index(speler)-1][3] != "" and scoretabel[spelerslijst.index(speler)-1][3] < 3*4:
        verschil += scoretabel[spelerslijst.index(speler)-1][3]-(3*4)
        doel -= scoretabel[spelerslijst.index(speler)-1][3]
        print("|"+forlinkol(scorelijst[3]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*4)-scoretabel[spelerslijst.index(speler)-1][3]))+ResetAll,end = "")
        print("|")
        #print("4 = %s%s%s" % (Slecht,"-"+str((3*4)-scoretabel[spelerslijst.index(speler)-1][3]),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][3] != "" and scoretabel[spelerslijst.index(speler)-1][3] > 3*4:
        verschil += scoretabel[spelerslijst.index(speler)-1][3]-(3*4)
        doel -= scoretabel[spelerslijst.index(speler)-1][3]
        print("|"+forlinkol(scorelijst[3]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][3]-(3*4)))+ResetAll,end = "")
        print("|")
        #print("4 = %s%s%s" % (Goed,"+"+str(scoretabel[spelerslijst.index(speler)-1][3]-(3*4)),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][3] != "" and scoretabel[spelerslijst.index(speler)-1][3] == 3*4:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][3]
        print("|"+forlinkol(scorelijst[3]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
        #print("4 = OK")
    if scoretabel[spelerslijst.index(speler)-1][4] != "" and scoretabel[spelerslijst.index(speler)-1][4] < 3*5:
        verschil += scoretabel[spelerslijst.index(speler)-1][4]-(3*5)
        doel -= scoretabel[spelerslijst.index(speler)-1][4]
        print("|"+forlinkol(scorelijst[4]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*5)-scoretabel[spelerslijst.index(speler)-1][4]))+ResetAll,end = "")
        print("|")
        #print("5 = %s%s%s" % (Slecht,"-"+str((3*5)-scoretabel[spelerslijst.index(speler)-1][4]),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][4] != "" and scoretabel[spelerslijst.index(speler)-1][4] > 3*5:
        verschil += scoretabel[spelerslijst.index(speler)-1][4]-(3*5)
        doel -= scoretabel[spelerslijst.index(speler)-1][4]
        print("|"+forlinkol(scorelijst[4]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][4]-(3*5)))+ResetAll,end = "")
        print("|")
        #print("5 = %s%s%s" % (Goed,"+"+str(scoretabel[spelerslijst.index(speler)-1][4]-(3*5)),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][4] != "" and scoretabel[spelerslijst.index(speler)-1][4] == 3*5:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][4]
        print("|"+forlinkol(scorelijst[4]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
        #print("5 = OK")
    if scoretabel[spelerslijst.index(speler)-1][5] != "" and scoretabel[spelerslijst.index(speler)-1][5] < 3*6:
        verschil += scoretabel[spelerslijst.index(speler)-1][5]-(3*6)
        doel -= scoretabel[spelerslijst.index(speler)-1][5]
        print("|"+forlinkol(scorelijst[5]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*6)-scoretabel[spelerslijst.index(speler)-1][5]))+ResetAll,end = "")
        print("|")
        #print("6 = %s%s%s" % (Slecht,"-"+str((3*6)-scoretabel[spelerslijst.index(speler)-1][5]),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][5] != "" and scoretabel[spelerslijst.index(speler)-1][5] > 3*6:
        verschil += scoretabel[spelerslijst.index(speler)-1][5]-(3*6)
        doel -= scoretabel[spelerslijst.index(speler)-1][5]
        print("|"+forlinkol(scorelijst[5]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][5]-(3*6)))+ResetAll,end = "")
        print("|")
        #print("6 = %s%s%s" % (Goed,"+"+str(scoretabel[spelerslijst.index(speler)-1][5]-(3*6)),ResetAll))
    if scoretabel[spelerslijst.index(speler)-1][5] != "" and scoretabel[spelerslijst.index(speler)-1][5] == 3*6:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][5]
        print("|"+forlinkol(scorelijst[5]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
        #print("6 = OK")
    if verschil < 0:
        print("|"+Slecht+forlinkol(tekort)+ResetAll, end = "")
        print("|"+Slecht+forspeler(verschil)+ResetAll,end = "")
        print("|")
    else:
        print("|"+Goed+forlinkol(over)+ResetAll, end = "")
        print("|"+Goed+forspeler(verschil)+ResetAll,end = "")
        print("|")
    if doel > 0:
        print("|"+forlinkol(totbonus), end = "")
        print("|"+forspeler(doel),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][0] == "":
        print("|"+forlinkol(scorelijst[0]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][0]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][1] == "":
        print("|"+forlinkol(scorelijst[1]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][1]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][2] == "":
        print("|"+forlinkol(scorelijst[2]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][2]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][3] == "":
        print("|"+forlinkol(scorelijst[3]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][3]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][4] == "":
        print("|"+forlinkol(scorelijst[4]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][4]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][5] == "":
        print("|"+forlinkol(scorelijst[5]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][5]),end = "")
        print("|")
    print(pluslijn)
    if scoretabel[spelerslijst.index(speler)-1][9] == "":
        print("|"+forlinkol(scorelijst[9]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][9]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][10] == "":
        print("|"+forlinkol(scorelijst[10]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][10]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][11] == "":
        print("|"+forlinkol(scorelijst[11]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][11]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][12] == "":
        print("|"+forlinkol(scorelijst[12]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][12]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][13] == "":
        print("|"+forlinkol(scorelijst[13]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][13]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][14] == "":
        print("|"+forlinkol(scorelijst[14]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][14]),end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][15] == "":
        print("|"+forlinkol(scorelijst[15]), end = "")
        print("|"+forspeler(scoretabel[spelerslijst.index(speler)-1][15]),end = "")
        print("|")
    print(pluslijn)
    

spel = 1
while spel <= 13:
    print(Ronde+ronde+ResetAll,spel)
    for i in range(len(spelerslijst)):
        speler = spelerslijst[i]
        print(speelt+Ronde+spelerslijst[i]+ResetAll)
        spelertabel(speler)
        for j in range(len(scorelijst)):
            if j not in [6,7,8,16,17,18]:
                print(Kies+forr2(j+1)+ResetAll+": "+forllinkol(scorelijst[j]),end = "")
            if j in [2,5,11,14]:
                print()
        print()
        score = False
        while score == False:
            veld = input(welkveld+Kies)
            print(ResetAll,end = "")
            if veld.upper() in afsluitlijst:
                exit()
            try:
                print(inputindent+Kies+veld+ResetAll+": "+scorelijst[int(veld)-1])
            except:
                print(veldongeldig)
                veld = "veldongeldig"
            if veld != "veldongeldig":
                waarde = input(welkewaarde)
                if waarde.upper() in afsluitlijst:
                    exit()
                if veld == "1":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if waarde % 1 == 0 and waarde <= 5 * 1:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "2":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if waarde % 2 == 0 and waarde <= 5 * 2:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "3":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if waarde % 3 == 0 and waarde <= 5 * 3:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "4":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if waarde % 4 == 0 and waarde <= 5 * 4:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "5":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if waarde % 5 == 0 and waarde <= 5 * 5:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "6":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if waarde % 6 == 0 and waarde <= 5 * 6:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "10":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if 5 <= waarde <= 5 * 6:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "11":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if 5 <= waarde <= 5 * 6:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)
                if veld == "12":
                    if scoretabel[i-1][int(veld)-1] == "":
                        waarde = 25
                        scoretabel[i-1][int(veld)-1] = waarde
                        score = True
                    else:
                        print(veldbezet)
                if veld == "13":
                    if scoretabel[i-1][int(veld)-1] == "":
                        waarde = 30
                        scoretabel[i-1][int(veld)-1] = waarde
                        score = True
                    else:
                        print(veldbezet)
                if veld == "14":
                    if scoretabel[i-1][int(veld)-1] == "":
                        waarde = 40
                        scoretabel[i-1][int(veld)-1] = waarde
                        score = True
                    else:
                        print(veldbezet)
                if veld == "15":
                    if scoretabel[i-1][int(veld)-1] == "":
                        waarde = 50
                        scoretabel[i-1][int(veld)-1] = waarde
                        score = True
                    else:
                        print(veldbezet)
                if veld == "16":
                    if scoretabel[i-1][int(veld)-1] == "":
                        try:
                            waarde = eval(waarde)
                            if 5 <= waarde <= 5 * 6:
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(waardeongeldig)
                        except(Exception) as f:
                            print(waardeongeldig)
                    else:
                        print(veldbezet)

                subtotboven = 0
                for j in scoretabel[i-1][:6]:
                    if j == "":
                        j = 0
                    subtotboven += j
                scoretabel[i-1][6] = subtotboven
                if scoretabel[i-1][6] >= 63:
                    scoretabel[i-1][7] = 35
                    scoretabel[i-1][8] = subtotboven+35
                    scoretabel[i-1][16] = subtotboven+35
                else:
                    scoretabel[i-1][8] = subtotboven+0
                    scoretabel[i-1][16] = subtotboven+0
                subtotonder = 0
                for j in scoretabel[i-1][9:16]:
                    if j == "":
                        j = 0
                    subtotonder += j
                scoretabel[i-1][17] = subtotonder
                scoretabel[i-1][18] = scoretabel[i-1][16]+scoretabel[i-1][17]
        bouwtabel()
    spel += 1 
