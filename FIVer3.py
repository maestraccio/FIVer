#!/usr/bin/python3
import random,textwrap
from time import sleep

#   Written by Maestraccio
#
#     /7/7/7
#    __|_|_|_o-
#   / /! | |
#   \ L'/! |
#    \  L' |
#     \___/

versie = "2.21"
datum = "20230916"
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
Resultaat              = LightCyan
#Resultaat              = LightYellow
Slecht                 = LightRed
Tekst                  = Reverse
Terug                  = DarkGray
Wit                    = White
forr2 = "{:>2}".format
forc3 = "{:^3}".format
inputindent = "  : "
afsluitlijst=["X","Q"]
veldlijst = ["1","2","3","4","5","6","10","11","12","13","14","15","16"]

print()
langsel = input(" >1 : Play in English\n  2 : Gioca in Italiano\n  3 : Speel in het Nederlands\n%s" % inputindent)
if langsel.upper() in afsluitlijst:
    exit()
elif langsel == "2":
    lang = "IT"
    print("\n\"H\" = Aiuto (dopo aver inserito i giocatori)\n\"Q\" = In dietro o Uscita\n")
    scorelijst = ["1","2","3","4","5","6","Subtot Sopra","Bonus 35 se SS >= 63","Totale Sopra","Tre Uguali","Quattro Uguali","Full House","Piccola Scala","Grande Scala","F I V er","Scelta Libera","Totale Sopra","Totale Sotto","TOTALE"]
    jalijst = ["S","SI","SÌ"]
    zeker = "Sei sicuro?\n%s" % inputindent
    allespelers = "Tutti i Giocatori"
    nog = "Avanzamento"
    speelt = "È l'opportunità di "
    ronde = "Giro "
    welkveld = "In %squale campo%s desideri registrare il tuo punteggio?\n%s" % (Kies,ResetAll,inputindent)
    welkewaarde = "Punteggio:\n%s" % (inputindent)
    waardeongeldig = "%sPunteggio invalido%s" % (Slecht,ResetAll)
    veldongeldig = "%sCampo invalido%s" % (Slecht,ResetAll)
    veldbezet = "%sCampo occupato%s" % (Slecht,ResetAll)
    tekort = "Da recuperare: "
    over = "Margine di manovra: "
    totbonus = "Fino al Bonus: "
    albonus = "Bonus raggiunto"
    nobonus = "Bonus non raggiunto"
    virtuelestenen = "Vuoi giocare con dadi virtuali?\n  1 : Sì\n >2 : No\n%s" % inputindent
    sorteren = "Ordinare"
    rolalledobbelstenen1 = "#1 Lancia tutti i dadi"
    kieswelke2 = "#2 Quali dadi vuoi rilanciare?\n%s" % inputindent
    kieswelke3 = "#3 Quali dadi vuoi rilanciare?\n%s" % inputindent
    suggesties = "Suggerimenti:"
    welkschrap = "Quale campo vuoi eliminare?\n%s" % inputindent
    wint = "Vince %s con un punteggio di %s"
elif langsel == "3":
    lang = "NL"
    print("\n\"H\" = Help (nadat je de spelers hebt opgegeven)\n\"Q\" = Terug of Verlaten\n")
    scorelijst = ["1","2","3","4","5","6","Subtot Boven","Bonus 35 als SB >= 63","Totaal Boven","Drie Dezelfde","Vier Dezelfde","Full House","Kleine Straat","Grote Straat","F I V er","Vrije Keus","Totaal Boven","Totaal Onder","TOTAAL"]
    jalijst = ["J","JA"]
    zeker = "Weet je het zeker?\n%s" % inputindent
    allespelers = "Alle Spelers"
    nog = "Voortgang"
    speelt = "De beurt is aan "
    ronde = "Ronde "
    welkveld = "In %swelk veld%s wil je je score registreren?\n%s" % (Kies,ResetAll,inputindent)
    welkewaarde = "Score:\n%s" % (inputindent)
    waardeongeldig = "%sOngeldige score%s" % (Slecht,ResetAll)
    veldongeldig = "%sOngeldig veld%s" % (Slecht,ResetAll)
    veldbezet = "%sVeld al in gebruik%s" % (Slecht,ResetAll)
    tekort = "In te halen: "
    over = "Speelruimte: "
    totbonus = "Tot aan de Bonus: "
    albonus = "Bonus behaald"
    nobonus = "Bonus niet behaald"
    virtuelestenen = "Wil je met virtuele dobbelstenen spelen?\n  1 : Ja\n >2 : Nee\n%s" % inputindent
    sorteren = "Sorteren"
    rolalledobbelstenen1 = "#1 Rol alle dobbelstenen"
    kieswelke2 = "#2 Welke wil je opnieuw rollen?\n%s" % inputindent
    kieswelke3 = "#3 Welke wil je opnieuw rollen?\n%s" % inputindent
    suggesties = "Suggesties:"
    welkschrap = "Welk veld wil je schrappen?\n%s" % inputindent
    wint = "%s wint met een score van %s"
else:
    lang = "EN"
    print("\n\"H\" = Help (after providing the players' names)\n\"Q\" = Back or Quit\n")
    scorelijst = ["1","2","3","4","5","6","Subtot Upper","Bonus 35 if SU >= 63","Total Upper","Three of a Kind","Four of a Kind","Full House","Small Straight","Large Straight","F I V er","Free Choice","Total Upper","Total Lower","TOTAL"]
    jalijst = ["Y","YES"]
    zeker = "Are you sure?\n%s" % inputindent
    allespelers = "All Players"
    nog = "Progress"
    speelt = "It's the turn of "
    ronde = "Round "
    welkveld = "In %swhich field%s do you want to record your score?\n%s" % (Kies,ResetAll,inputindent)
    welkewaarde = "Score:\n%s" % (inputindent)
    waardeongeldig = "%sInvalid score%s" % (Slecht,ResetAll)
    veldongeldig = "%sInvalid field%s" % (Slecht,ResetAll)
    veldbezet = "%sField already taken%s" % (Slecht,ResetAll)
    tekort = "Short: "
    over = "Leeway: "
    totbonus = "Until the Bonus: "
    albonus = "Bonus achieved"
    nobonus = "Bonus not achieved"
    virtuelestenen = "Do you want to play with virtual dice?\n  1 : Yes\n >2 : No\n%s" % inputindent
    sorteren = "Sorting"
    rolalledobbelstenen1 = "#1 Roll all dice"
    kieswelke2 = "#2 Choose which to roll again:\n%s" % inputindent
    kieswelke3 = "#3 Choose which to roll again:\n%s" % inputindent
    suggesties = "Suggestions:"
    welkschrap = "Which field do you want to cancel?\n%s" % inputindent
    wint = "%s wins with a score of %s"

maxlinkol = len(max(scorelijst, key = len))
forlinkol = ("{:^%s}" % maxlinkol).format
forllinkol = ("{:<%s}" % maxlinkol).format
forrlinkol = ("{:>%s}" % maxlinkol).format


def afsluitroutine():
    zekerweten = input(zeker)
    if zekerweten.upper() in jalijst:
        exit()

def nicklijst(init):
    if init == "A":
        nicks = [" the Awesome"," the Admirable", " the Amazing", " the Annihilator"]
    elif init == "B":
        nicks = [" the Bright"," the Brave", " the Bold", " the Bulldozer"]
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
            if len(spelerslijst) == 0:
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

def hellup():
    if lang == "IT":
        help1 = textwrap.wrap("\"FIVer\" è una variante del famoso gioco dei dadi Yahtzee. Puoi giocarlo con dei veri dadi fisici o utilizzando la funzione di dadi virtuali integrata. Il punteggio ed il progresso vengono registrati per ogni giocatore in tabelle chiare. Puoi inserire il punteggio in diversi modi:", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help2 = "Nei campi da 1 a 6:\n 1: %s5%s: \"15\"  (=15)\n 2: %s5%s: \"*3\"  (=15)\n 3: %s5%s: \"3*5\" (=15)\n 4: %s5%s: \"555\" (=15)" % (Kies,ResetAll,Kies,ResetAll,Kies,ResetAll,Kies,ResetAll)
        help3 = "Nei campi 10, 11 e 16:\n 1: %s10%s: \"15\"      (=15)\n 2: %s10%s: \"1+3*3+5\" (=15)\n 3: %s10%s: \"13335\"   (=15)" % (Kies,ResetAll,Kies,ResetAll,Kies,ResetAll)
        help4 = "Nei campi da 12 a 15:\n 1: %s13%s: (=30)\n 2: %s30%s: (=30)" % (Kies,ResetAll,Kies,ResetAll)
        help5 = textwrap.wrap("Quando giochi con i dadi virtuali, indichi quali dadi vuoi rilanciare, quindi non quelli che desideri tenere. Indica la/le lettera/-e corrispondente, non il valore. Tieni presente che i dadi vengono sempre ordinati per valore, quindi la lettera può cambiare ad ogni turno. Se non fai alcuna scelta (tra A, B, C, D o E), nessun dado viene rilanciato, \"*\" rilancia tutti i dadi.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help6 = textwrap.wrap("Per comodità, vengono visualizzate delle suggerimenti validi, ma possono essere ignorati.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help7 = textwrap.wrap("Per eliminare un campo (= immettendo un punteggio di \"0\"), puoi precedere il nome del campo con un \"/\" (\"/13\" = \"Piccola scala: 0\").", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help8 = textwrap.wrap("TIP: Su schermi stretti, inizia il nome del giocatore con un numero: 1Io, 2Tu, e così via, per evitare l'aggiunta di un \"nickname\".", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help9 = textwrap.wrap("Scegli \"H\" per questo aiuto o \"Q\" per uscire", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
    elif lang == "NL":
        help1 = textwrap.wrap("\"FIVer\" is een variant op het bekende Yahtzee-dobbelspel. Je kunt het spelen met echte, fysieke dobbelstenen, of met de ingebouwde virtuele dobbelfuctie. De score en de voortgang worden per speler bijgehouden in overzichtelijke tabellen. Je kunt die score op verschillende manieren invoeren:", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help2 = "In de velden 1 t/m 6:\n 1: %s5%s: \"15\"  (=15)\n 2: %s5%s: \"*3\"  (=15)\n 3: %s5%s: \"3*5\" (=15)\n 4: %s5%s: \"555\" (=15)" % (Kies,ResetAll,Kies,ResetAll,Kies,ResetAll,Kies,ResetAll)
        help3 = "In de velden 10, 11 en 16:\n 1: %s10%s: \"15\"      (=15)\n 2: %s10%s: \"1+3*3+5\" (=15)\n 3: %s10%s: \"13335\"   (=15)" % (Kies,ResetAll,Kies,ResetAll,Kies,ResetAll)
        help4 = "In de velden 12 t/m 15:\n 1: %s13%s: (=30)\n 2: %s30%s: (=30)" % (Kies,ResetAll,Kies,ResetAll)
        help5 = textwrap.wrap("Bij het spelen met virtuele dobbelstenen geef je aan welke stenen je opnieuw wilt rollen, en dus niet die je wilt vasthouden. Geef daarvoor de corresponderende letter(-s) op, niet de waarde. Let op dat de dobbelstenen steeds gesorteerd worden op waarde, en dat de letter dus per beurt kan veranderen. Geen keuze (uit A, B, C, D of E) rolt geen stenen opnieuw, \"*\" selecteert ze allemaal.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help6 = textwrap.wrap("Voor het gemak worden geldige suggesties weergegeven, maar die kunnen worden genegeerd.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help7 = textwrap.wrap("Om een veld te schrappen (= een score van \"0\" in te voeren) kun je de veldnaam laten voorafgaan door een \"/\" (\"/13\" = \"Kleine straat: 0\").", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help8 = textwrap.wrap("TIP: begin de spelersnaam op smalle schermen met een cijfer: 1Ik, 2Jij, enzovoorts, om te voorkomen dat een \"nickname\" wordt toegevoegd.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help9 = textwrap.wrap("Kies \"H\" voor deze help of \"Q\" om te verlaten", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
    else:
        help1 = textwrap.wrap("\"FIVer\" is a variant of the well-known Yahtzee dice game. You can play it with real, physical dice or with the built-in virtual dice function. The score and progress are kept for each player in clear tables. You can enter that score in different ways:", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help2 = "In the fields 1 through 6:\n 1: %s5%s: \"15\"  (=15)\n 2: %s5%s: \"*3\"  (=15)\n 3: %s5%s: \"3*5\" (=15)\n 4: %s5%s: \"555\" (=15)" % (Kies,ResetAll,Kies,ResetAll,Kies,ResetAll,Kies,ResetAll)
        help3 = "In the fields 10, 11 and 16:\n 1: %s10%s: \"15\"      (=15)\n 2: %s10%s: \"1+3*3+5\" (=15)\n 3: %s10%s: \"13335\"   (=15)" % (Kies,ResetAll,Kies,ResetAll,Kies,ResetAll)
        help4 = "In the fields 12 through 15:\n 1: %s13%s: (=30)\n 2: %s30%s: (=30)" % (Kies,ResetAll,Kies,ResetAll)
        help5 = textwrap.wrap("When playing with virtual dice, you indicate which dice you want to roll again, and not the ones you want to hold. Specify the corresponding letter(s) for that, not the value. Note that the dice are always sorted by value, so the letter can change per turn. No choice (from A, B, C, D, or E) means no dice will be rolled, \"*\" rolls all of them.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help6 = textwrap.wrap("For convenience, valid suggestions are displayed, but they can be ignored.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help7 = textwrap.wrap("To delete a field (= entering a score of \"0\"), you can prefix the field name with a \"/\" (\"/13\" = \"Small straight: 0\").", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help8 = textwrap.wrap("TIP: On narrow screens, start the player name with a number: 1Me, 2You, and so on, to prevent the addition of a nickname.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
        help9 = textwrap.wrap("Choose \"H\" for this help or \"Q\" to Quit", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
    print(ResetAll, end = "")
    for i in help1:
        print(i)
    print(help2)
    print(help3)
    print(help4)
    for i in help5:
        print(i)
    for i in help6:
        print(i)
    for i in help7:
        print(i)
    for i in help8:
        print(i)
    for i in help9:
        print(i)

def leeshellup():
    if lang == "IT":
        leeshellup = textwrap.wrap("Il testo di aiuto è già visualizzato sopra. Non c'è altro, continua a giocare.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
    elif lang == "NL":
        leeshellup = textwrap.wrap("De Helptekst wordt hierboven al weergegeven. Meer is er niet, speel verder.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
    else:
        leeshellup = textwrap.wrap("The Help text has already been displayed above. That's all there is, continue the game.", width = 1+maxlinkol+(1+maxspeler)*len(spelerslijst)+1)
    print(ResetAll, end = "")
    for i in leeshellup:
        print(i)

def maakscoretabel():
    scoretabel = []
    for i in spelerslijst:
        i = []
        for j in scorelijst:
            i.append("")
        scoretabel.append(i)
    return scoretabel
scoretabel = maakscoretabel()

maxscorelijst = []
for i in spelerslijst:
    maxscorelijst.append(0)

def bouwtabel(maxscorelijst,speler,spel,winnaar):
    maxscore = max(maxscorelijst)
    print(Tabel, end = "")
    pluslijn = "+"+"-"*maxlinkol+("+"+"-"*maxspeler)*len(spelerslijst)+"+"
    print(pluslijn)
    print("|"+forlinkol(allespelers),end = "")
    for i in spelerslijst:
        if i == speler and spel <= 13:
            col = Ronde
        elif spel > 13 and i == winnaar:
            col = Resultaat
        else:
            col = Tabel
        print("|"+col+forspeler(i)+Tabel, end = "")
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
        if max(maxscorelijst) == scoretabel[i-1][18]:
            col = Resultaat
        else:
            col = Tabel
        print("|"+col+forspeler(scoretabel[i-1][18])+Tabel,end = "")
    print("|")
    print(pluslijn)
    print(ResetAll, end = "")

def spelertabel(speler):
    pluslijn = "+"+"-"*maxlinkol+"+"+"-"*maxspeler+"+"
    doel = 63
    verschil = 0
    print(pluslijn)
    print("|"+forlinkol(nog)+"|"+Ronde+forspeler(speler)+ResetAll,end = "")
    print("|")
    print(pluslijn)
    if scoretabel[spelerslijst.index(speler)-1][0] != "" and scoretabel[spelerslijst.index(speler)-1][0] < 3*1:
        verschil += scoretabel[spelerslijst.index(speler)-1][0]-(3*1)
        doel -= scoretabel[spelerslijst.index(speler)-1][0]
        print("|"+forlinkol(scorelijst[0]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*1)-scoretabel[spelerslijst.index(speler)-1][0]))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][0] != "" and scoretabel[spelerslijst.index(speler)-1][0] > 3*1:
        verschil += scoretabel[spelerslijst.index(speler)-1][0]-(3*1)
        doel -= scoretabel[spelerslijst.index(speler)-1][0]
        print("|"+forlinkol(scorelijst[0]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][0]-(3*1)))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][0] != "" and scoretabel[spelerslijst.index(speler)-1][0] == 3*1:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][0]
        print("|"+forlinkol(scorelijst[0]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][1] != "" and scoretabel[spelerslijst.index(speler)-1][1] < 3*2:
        verschil += scoretabel[spelerslijst.index(speler)-1][1]-(3*2)
        doel -= scoretabel[spelerslijst.index(speler)-1][1]
        print("|"+forlinkol(scorelijst[1]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*2)-scoretabel[spelerslijst.index(speler)-1][1]))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][1] != "" and scoretabel[spelerslijst.index(speler)-1][1] > 3*2:
        verschil += scoretabel[spelerslijst.index(speler)-1][1]-(3*2)
        doel -= scoretabel[spelerslijst.index(speler)-1][1]
        print("|"+forlinkol(scorelijst[1]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][1]-(3*2)))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][1] != "" and scoretabel[spelerslijst.index(speler)-1][1] == 3*2:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][1]
        print("|"+forlinkol(scorelijst[1]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][2] != "" and scoretabel[spelerslijst.index(speler)-1][2] < 3*3:
        verschil += scoretabel[spelerslijst.index(speler)-1][2]-(3*3)
        doel -= scoretabel[spelerslijst.index(speler)-1][2]
        print("|"+forlinkol(scorelijst[2]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*3)-scoretabel[spelerslijst.index(speler)-1][2]))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][2] != "" and scoretabel[spelerslijst.index(speler)-1][2] > 3*3:
        verschil += scoretabel[spelerslijst.index(speler)-1][2]-(3*3)
        doel -= scoretabel[spelerslijst.index(speler)-1][2]
        print("|"+forlinkol(scorelijst[2]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][2]-(3*3)))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][2] != "" and scoretabel[spelerslijst.index(speler)-1][2] == 3*3:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][2]
        print("|"+forlinkol(scorelijst[2]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][3] != "" and scoretabel[spelerslijst.index(speler)-1][3] < 3*4:
        verschil += scoretabel[spelerslijst.index(speler)-1][3]-(3*4)
        doel -= scoretabel[spelerslijst.index(speler)-1][3]
        print("|"+forlinkol(scorelijst[3]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*4)-scoretabel[spelerslijst.index(speler)-1][3]))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][3] != "" and scoretabel[spelerslijst.index(speler)-1][3] > 3*4:
        verschil += scoretabel[spelerslijst.index(speler)-1][3]-(3*4)
        doel -= scoretabel[spelerslijst.index(speler)-1][3]
        print("|"+forlinkol(scorelijst[3]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][3]-(3*4)))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][3] != "" and scoretabel[spelerslijst.index(speler)-1][3] == 3*4:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][3]
        print("|"+forlinkol(scorelijst[3]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][4] != "" and scoretabel[spelerslijst.index(speler)-1][4] < 3*5:
        verschil += scoretabel[spelerslijst.index(speler)-1][4]-(3*5)
        doel -= scoretabel[spelerslijst.index(speler)-1][4]
        print("|"+forlinkol(scorelijst[4]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*5)-scoretabel[spelerslijst.index(speler)-1][4]))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][4] != "" and scoretabel[spelerslijst.index(speler)-1][4] > 3*5:
        verschil += scoretabel[spelerslijst.index(speler)-1][4]-(3*5)
        doel -= scoretabel[spelerslijst.index(speler)-1][4]
        print("|"+forlinkol(scorelijst[4]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][4]-(3*5)))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][4] != "" and scoretabel[spelerslijst.index(speler)-1][4] == 3*5:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][4]
        print("|"+forlinkol(scorelijst[4]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][5] != "" and scoretabel[spelerslijst.index(speler)-1][5] < 3*6:
        verschil += scoretabel[spelerslijst.index(speler)-1][5]-(3*6)
        doel -= scoretabel[spelerslijst.index(speler)-1][5]
        print("|"+forlinkol(scorelijst[5]), end = "")
        print("|"+Slecht+forspeler("-"+str((3*6)-scoretabel[spelerslijst.index(speler)-1][5]))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][5] != "" and scoretabel[spelerslijst.index(speler)-1][5] > 3*6:
        verschil += scoretabel[spelerslijst.index(speler)-1][5]-(3*6)
        doel -= scoretabel[spelerslijst.index(speler)-1][5]
        print("|"+forlinkol(scorelijst[5]), end = "")
        print("|"+Goed+forspeler("+"+str(scoretabel[spelerslijst.index(speler)-1][5]-(3*6)))+ResetAll,end = "")
        print("|")
    if scoretabel[spelerslijst.index(speler)-1][5] != "" and scoretabel[spelerslijst.index(speler)-1][5] == 3*6:
        verschil += 0
        doel -= scoretabel[spelerslijst.index(speler)-1][5]
        print("|"+forlinkol(scorelijst[5]), end = "")
        print("|"+Goed+forspeler(0)+ResetAll,end = "")
        print("|")
    klaarboven = 0
    bonusbehaald = False
    for j in scoretabel[spelerslijst.index(speler)-1][:6]:
        if j != "":
            klaarboven += 1
    if doel > 0 and klaarboven < 6:
        print("-"+forlinkol(totbonus), end = "")
        print("-"+forspeler(doel),end = "")
        print("-")
    elif doel > 0 and klaarboven == 6:
        print("-"+Slecht+forlinkol(nobonus)+ResetAll, end = "")
        print("-"+Slecht+forspeler(":-(")+ResetAll,end = "")
        print("-")
    else:
        print("-"+Goed+forlinkol(albonus)+ResetAll, end = "")
        print("-"+Goed+forspeler(":-)")+ResetAll,end = "")
        print("-")
        bonusbehaald = True
    if verschil < 0 and klaarboven < 6:
        print("-"+Slecht+forlinkol(tekort)+ResetAll, end = "")
        print("-"+Slecht+forspeler(verschil)+ResetAll,end = "")
        print("-")
    elif verschil >= 0 and klaarboven < 6 and bonusbehaald == False:
        print("-"+Goed+forlinkol(over)+ResetAll, end = "")
        print("-"+Goed+forspeler(verschil)+ResetAll,end = "")
        print("-")
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
    
def roll():
    def visualDice():
        Dicetop = " "+Reverse+Wit+"     "+ResetAll
        Dicebottom = Dicetop
        One1 =  " "+Reverse+Wit+"     "+ResetAll
        One2 = " "+Reverse+Wit+"  "+ResetAll+Wit+"_"+Reverse+Wit+"  "+ResetAll
        One3 = Dicetop
        Two1 = " "+Reverse+Wit+" "+ResetAll+Wit+"_"+Reverse+Wit+"   "+ResetAll
        Two2 = Dicetop
        Two3 = " "+Reverse+Wit+"   "+ResetAll+Wit+"_"+Reverse+Wit+" "+ResetAll
        Three1 = Two3
        Three2 = One2
        Three3 = Two1
        Four1 = " "+Reverse+Wit+" "+ResetAll+Wit+"_"+Reverse+Wit+" "+ResetAll+Wit+"_"+Reverse+Wit+" "+ResetAll
        Four2 = Dicetop
        Four3 = Four1
        Five1 = Four1
        Five2 = One2
        Five3 = Four1
        Six1 = Four1
        Six2 = Four1 
        Six3 = Four1 
        Dice = [Dicetop,Dicetop,Dicetop,Dicetop,Dicetop,"","","","","","","","","","","","","","","",Dicebottom,Dicebottom,Dicebottom,Dicebottom,Dicebottom]
        if A == 1:
            Dice[5] = One1
            Dice[10] = One2
            Dice[15] = One3
        elif A == 2: 
            Dice[5] = Two1
            Dice[10] = Two2
            Dice[15] = Two3
        elif A == 3:
            Dice[5] = Three1
            Dice[10] = Three2
            Dice[15] = Three3
        elif A == 4:
            Dice[5] = Four1
            Dice[10] = Four2
            Dice[15] = Four3
        elif A == 5:
            Dice[5] = Five1
            Dice[10] = Five2
            Dice[15] = Five3
        elif A == 6:
            Dice[5] = Six1
            Dice[10] = Six2
            Dice[15] = Six3
        if B == 1:
            Dice[6] = One1
            Dice[11] = One2
            Dice[16] = One3
        elif B == 2:
            Dice[6] = Two1
            Dice[11] = Two2
            Dice[16] = Two3
        elif B == 3:
            Dice[6] = Three1
            Dice[11] = Three2
            Dice[16] = Three3
        elif B == 4:
            Dice[6] = Four1
            Dice[11] = Four2
            Dice[16] = Four3
        elif B == 5:
            Dice[6] = Five1
            Dice[11] = Five2
            Dice[16] = Five3
        elif B == 6:
            Dice[6] = Six1
            Dice[11] = Six2
            Dice[16] = Six3
        if C == 1:
            Dice[7] = One1
            Dice[12] = One2
            Dice[17] = One3
        elif C == 2:
            Dice[7] = Two1
            Dice[12] = Two2
            Dice[17] = Two3
        elif C == 3:
            Dice[7] = Three1
            Dice[12] = Three2
            Dice[17] = Three3
        elif C == 4:
            Dice[7] = Four1
            Dice[12] = Four2
            Dice[17] = Four3
        elif C == 5:
            Dice[7] = Five1
            Dice[12] = Five2
            Dice[17] = Five3
        elif C == 6:
            Dice[7] = Six1
            Dice[12] = Six2
            Dice[17] = Six3
        if D == 1:
            Dice[8] = One1
            Dice[13] = One2
            Dice[18] = One3
        elif D == 2:
            Dice[8] = Two1
            Dice[13] = Two2
            Dice[18] = Two3
        elif D == 3:
            Dice[8] = Three1
            Dice[13] = Three2
            Dice[18] = Three3
        elif D == 4:
            Dice[8] = Four1
            Dice[13] = Four2
            Dice[18] = Four3
        elif D == 5:
            Dice[8] = Five1
            Dice[13] = Five2
            Dice[18] = Five3
        elif D == 6:
            Dice[8] = Six1
            Dice[13] = Six2
            Dice[18] = Six3
        if E == 1:
            Dice[9] = One1
            Dice[14] = One2
            Dice[19] = One3
        elif E == 2:
            Dice[9] = Two1
            Dice[14] = Two2
            Dice[19] = Two3
        elif E == 3:
            Dice[9] = Three1
            Dice[14] = Three2
            Dice[19] = Three3
        elif E == 4:
            Dice[9] = Four1
            Dice[14] = Four2
            Dice[19] = Four3
        elif E == 5:
            Dice[9] = Five1
            Dice[14] = Five2
            Dice[19] = Five3
        elif E == 6:
            Dice[9] = Six1
            Dice[14] = Six2
            Dice[19] = Six3
        return Dice

    roll = "Y"
    while roll == "Y":
        firstroll = []
        for i in range(5):
            firstroll.append(random.choice(range(1,7)))
        Firstroll = sorted(firstroll)
        A = Firstroll[0]
        B = Firstroll[1]
        C = Firstroll[2]
        D = Firstroll[3]
        E = Firstroll[4]
        Dice = visualDice()
        print(rolalledobbelstenen1)
        for i in [" ","_",Reverse+" ","A"," "+ResetAll,"_"," ","_",Reverse+" ","B"," "+ResetAll,"_"," ","_",Reverse+" ","C"," "+ResetAll,"_"," ","_",Reverse+" ","D"," "+ResetAll,"_"," ","_",Reverse+" ","E"," "+ResetAll,"_"," "]:
            print(i, end = "", flush = True)
            sleep(0.05)
        sleep(0.05)
        print()
        print("{:^31}".format(sorteren))
        print(" "*14, end = "")
        for i in "...":
            print(i, end = "", flush = True)
            sleep(0.5)
        print()
        counti = 0
        for i in Dice:
            print(i, end = "")
            counti += 1
            if counti % 5 == 0:
                print()
        print(DarkGray+"  A=%s   B=%s   C=%s   D=%s   E=%s" % (A,B,C,D,E)+ResetAll)
        choice = input(kieswelke2).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() == "H":
            hellup()
            choice = input(kieswelke2).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() == "H":
            leeshellup()
            choice = input(kieswelke2).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() in afsluitlijst:
            afsluitroutine()
        if choice == "*":
            choice = "ABCDE"
        Secondroll = Firstroll
        visualroll = [" ","_","_","A","_","_"," ","_","_","B","_","_"," ","_","_","C","_","_"," ","_","_","D","_","_"," ","_","_","E","_","_"," "]
        for i in choice:
            if i == "A":
                Secondroll[0] = random.choice(range(1,7))
                visualroll[2] = (Reverse+" ")
                visualroll[3] = ("A")
                visualroll[4] = (" "+ResetAll)
            if i == "B":
                Secondroll[1] = random.choice(range(1,7))
                visualroll[8] = (Reverse+" ")
                visualroll[9] = ("B")
                visualroll[10] = (" "+ResetAll)
            if i == "C":
                Secondroll[2] = random.choice(range(1,7))
                visualroll[14] = (Reverse+" ")
                visualroll[15] = ("C")
                visualroll[16] = (" "+ResetAll)
            if i == "D":
                Secondroll[3] = random.choice(range(1,7))
                visualroll[20] = (Reverse+" ")
                visualroll[21] = ("D")
                visualroll[22] = (" "+ResetAll)
            if i == "E":
                Secondroll[4] = random.choice(range(1,7))
                visualroll[26] = (Reverse+" ")
                visualroll[27] = ("E")
                visualroll[28] = (" "+ResetAll)
        Secondroll = sorted(Secondroll)
        A = Secondroll[0]
        B = Secondroll[1]
        C = Secondroll[2]
        D = Secondroll[3]
        E = Secondroll[4]
        Dice = visualDice()
        if choice != "":
            for i in visualroll:
                print(i, end = "", flush = True)
                sleep(0.05)
            sleep(0.05)
            print()
            print("{:^31}".format(sorteren))
            print(" "*14, end = "")
            for i in "...":
                print(i, end = "", flush = True)
                sleep(0.5)
        print()
        counti = 0
        for i in Dice:
            print(i, end = "")
            counti += 1
            if counti % 5 == 0:
                print()
        print(DarkGray+"  A=%s   B=%s   C=%s   D=%s   E=%s" % (A,B,C,D,E)+ResetAll)
        choice = input(kieswelke3).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() == "H":
            hellup()
            choice = input(kieswelke2).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() == "H":
            leeshellup()
            choice = input(kieswelke2).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() in afsluitlijst:
            afsluitroutine()
        if choice == "*":
            choice = "ABCDE"
        Thirdroll = Secondroll
        visualroll = [" ","_","_","A","_","_"," ","_","_","B","_","_"," ","_","_","C","_","_"," ","_","_","D","_","_"," ","_","_","E","_","_"," "]
        for i in choice:
            if i == "A":
                Secondroll[0] = random.choice(range(1,7))
                visualroll[2] = (Reverse+" ")
                visualroll[3] = ("A")
                visualroll[4] = (" "+ResetAll)
            if i == "B":
                Secondroll[1] = random.choice(range(1,7))
                visualroll[8] = (Reverse+" ")
                visualroll[9] = ("B")
                visualroll[10] = (" "+ResetAll)
            if i == "C":
                Secondroll[2] = random.choice(range(1,7))
                visualroll[14] = (Reverse+" ")
                visualroll[15] = ("C")
                visualroll[16] = (" "+ResetAll)
            if i == "D":
                Secondroll[3] = random.choice(range(1,7))
                visualroll[20] = (Reverse+" ")
                visualroll[21] = ("D")
                visualroll[22] = (" "+ResetAll)
            if i == "E":
                Secondroll[4] = random.choice(range(1,7))
                visualroll[26] = (Reverse+" ")
                visualroll[27] = ("E")
                visualroll[28] = (" "+ResetAll)
        Thirdroll = sorted(Thirdroll)
        A = Thirdroll[0]
        B = Thirdroll[1]
        C = Thirdroll[2]
        D = Thirdroll[3]
        E = Thirdroll[4]
        Dice = visualDice()
        if choice != "":
            for i in visualroll:
                print(i, end = "", flush = True)
                sleep(0.05)
            sleep(0.05)
            print()
            print("{:^31}".format(sorteren))
            print(" "*14, end = "")
            for i in "...":
                print(i, end = "", flush = True)
                sleep(0.5)
        print()
        counti = 0
        for i in Dice:
            print(i, end = "")
            counti += 1
            if counti % 5 == 0:
                print()
        print(DarkGray+"  A=%s   B=%s   C=%s   D=%s   E=%s" % (A,B,C,D,E)+ResetAll)
        return A,B,C,D,E

def suggestions():
    suggestionslist = []
    alnietsug = []
    if A == B == C and C != D: 
        sug = "%s: %s" % (Kies+forr2(A)+ResetAll,Goed+forr2(A+B+C)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(A))] == "":
            suggestionslist.append(sug)
    if B == C == D and A != B and D != E:
        sug = "%s: %s" % (Kies+forr2(B)+ResetAll,Goed+forr2(B+C+D)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(B))] == "":
            suggestionslist.append(sug)
    if C == D == E and B != C:
        sug = "%s: %s" % (Kies+forr2(C)+ResetAll,Goed+forr2(C+D+E)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(C))] == "":
            suggestionslist.append(sug)
    if A == B == C == D and D != E:
        sug = "%s: %s" % (Kies+forr2(A)+ResetAll,Goed+forr2(A+B+C+D)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(A))] == "":
            suggestionslist.append(sug)
    if B == C == D == E and A != B:
        sug = "%s: %s" % (Kies+forr2(B)+ResetAll,Goed+forr2(B+C+D+E)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(B))] == "":
            suggestionslist.append(sug)
    if (A == B == C == D == E):
        sug = "%s: %s" % (Kies+forr2(A)+ResetAll,Goed+forr2(A+B+C+D+E)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(A))] == "":
            suggestionslist.append(sug)
    if (A == B == C == D == E):
        sug = "%s: %s" % (Kies+forr2(15)+ResetAll,Goed+forr2(50)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][15-1] == "":
            suggestionslist.append(sug)
    if (A == B-1 and B == C-1 and C == D-1 and D == E-1):
        sug = "%s: %s" % (Kies+forr2(14)+ResetAll,Goed+forr2(40)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][14-1] == "":
            suggestionslist.append(sug)
    if (B == C-1 and C == D-1 and D == E-1) or (A == C-1 and C == D-1 and D == E-1) or (A == B-1 and B == D-1 and D == E-1) or (A == B-1 and B == C-1 and C == E-1) or (A == B-1 and B == C-1 and C == D-1):
        sug = "%s: %s" % (Kies+forr2(13)+ResetAll,Goed+forr2(30)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][13-1] == "":
            suggestionslist.append(sug)
    if (A == B == C and D == E) or (A == B and C == D == E):
        sug = "%s: %s" % (Kies+forr2(12)+ResetAll,Goed+forr2(25)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][12-1] == "":
            suggestionslist.append(sug)
    if (A == B == C == D) or (B == C == D == E):
        sug = "%s: %s" % (Kies+forr2(11)+ResetAll,Goed+forr2(A+B+C+D+E)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][11-1] == "":
            suggestionslist.append(sug)
    if (A == B == C) or (B == C == D) or (C == D == E):
        sug = "%s: %s" % (Kies+forr2(10)+ResetAll,Goed+forr2(A+B+C+D+E)+ResetAll)
        if scoretabel[spelerslijst.index(speler)-1][10-1] == "":
            suggestionslist.append(sug)
    if A == B and B != C:
        sug = "%s: %s" % (Kies+forr2(A)+ResetAll,forr2(A+B))
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(A))] == "":
            suggestionslist.append(sug)
    if A != B and B == C and C != D:
        sug = "%s: %s" % (Kies+forr2(B)+ResetAll,forr2(B+C))
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(B))] == "":
            suggestionslist.append(sug)
    if B != C and C == D and D != E:
        sug = "%s: %s" % (Kies+forr2(C)+ResetAll,forr2(C+D))
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(C))] == "":
            suggestionslist.append(sug)
    if C != D and D == E:
        sug = "%s: %s" % (Kies+forr2(D)+ResetAll,forr2(D+E))
        if scoretabel[spelerslijst.index(speler)-1][scorelijst.index(str(D))] == "":
            suggestionslist.append(sug)
    sug = "%s: %s" % (Kies+forr2(16)+ResetAll,forr2(A+B+C+D+E))
    if scoretabel[spelerslijst.index(speler)-1][16-1] == "":
        suggestionslist.append(sug)
    if len(suggestionslist) > 0:
        print(suggesties)
        for i in suggestionslist:
            print(i)
    return suggestionslist

virtu = input(virtuelestenen)
if virtu.upper() == "H":
    hellup()
    virtu = input(virtuelestenen)
if virtu.upper() == "H":
    leeshellup()
    virtu = input(virtuelestenen)
if virtu.upper() in afsluitlijst:
    afsluitroutine()

spel = 1
while spel <= len(veldlijst):
    winnaar = ""
    rondelijn = "+"+"-"*maxlinkol+("-"+("-"*maxspeler))*len(spelerslijst)+"+"
    forrondelijn = ("{:^%s}" % (len(rondelijn)-2)).format
    for i in range(len(spelerslijst)):
        print(Tabel+rondelijn+ResetAll)
        print(Tabel+"|"+ResetAll+Ronde+forrondelijn(ronde+str(spel))+ResetAll+Tabel+"|"+ResetAll)
        speler = spelerslijst[i]
        bouwtabel(maxscorelijst,speler,spel,winnaar)
        spelertabel(speler)
        allijst = []
        if virtu == "1":
            rolls = roll()
            A = rolls[0]
            B = rolls[1]
            C = rolls[2]
            D = rolls[3]
            E = rolls[4]
            suggestionslist = suggestions()
        print()
        if 1+maxlinkol + (1+maxspeler)*len(spelerslijst) + 1 <= 31*1:
            maxbreed = 1
        elif 1+maxlinkol + (1+maxspeler)*len(spelerslijst) + 1 <= 31*2:
            maxbreed = 2
        else:
            maxbreed = 3
        breed = 0
        for j in range(len(scorelijst)):
            if j not in [6,7,8,16,17,18] and scoretabel[spelerslijst.index(speler)-1][j] == "":
                print(Kies+forr2(j+1)+ResetAll+": "+forllinkol(scorelijst[j]),end = "")
                breed += 1
            elif j not in [6,7,8,16,17,18] and scoretabel[spelerslijst.index(speler)-1][j] != "":
                print(Terug+forr2(j+1)+": "+forllinkol(scorelijst[j])+ResetAll,end = "")
                allijst.append(j)
                breed += 1
            if breed == maxbreed or j == 5:
                print()
                breed = 0
        print()
        print()
        score = False
        while score == False:
            waarde = ""
            veld = input(welkveld+Kies)
            if veld.upper() == "H":
                hellup()
                veld = input(welkveld+Kies)
            if veld.upper() == "H":
                leeshellup()
                veld = input(welkveld+Kies)
            if veld == "25":
                veld = "12"
            elif veld == "30":
                veld = "13"
            elif veld == "40":
                veld = "14"
            elif veld == "50":
                veld = "15"
            elif veld == "/25":
                veld = "/12"
            elif veld == "/30":
                veld = "/13"
            elif veld == "/40":
                veld = "/14"
            elif veld == "/50":
                veld = "/15"
            print(ResetAll,end = "")
            if veld.upper() in afsluitlijst:
                afsluitroutine()
            if veld == "/":
                veld = input(welkschrap)
                if veld.upper() == "H":
                    hellup()
                    veld = input(welkschrap)
                if veld.upper() == "H":
                    leeshellup()
                    veld = input(welkschrap)
                if veld in veldlijst:
                    waarde = "0"
                    scoretabel[i-1][int(veld)-1] = 0
                    score = True
                else:
                    print(veldongeldig)
            elif len(veld) > 1 and veld[0] == "/":
                veld = veld[1:]
                if veld in veldlijst:
                    waarde = "0"
                    scoretabel[i-1][int(veld)-1] = 0
                    score = True
                else:
                    print(veldongeldig)
            else:
                try:
                    print(inputindent+Kies+veld+ResetAll+": "+scorelijst[int(veld)-1])
                except:
                    print(veldongeldig)
                    veld = "veldongeldig"
                if veld != "veldongeldig":
                    if waarde != "0":
                        if veld not in ["12","13","14","15"] and int(veld)-1 not in allijst:
                            waarde = input(welkewaarde+Resultaat).replace(" ","")
                            if waarde.upper() == "H":
                                hellup()
                                waarde = input(welkewaarde+Resultaat).replace(" ","")
                            if waarde.upper() == "H":
                                leeshellup()
                                waarde = input(welkewaarde+Resultaat).replace(" ","")
                            print(ResetAll, end = "")
                        if waarde.upper() in afsluitlijst:
                            afsluitroutine()
                        elif veld == "1":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if waarde % 1 == 0 and waarde <= 5 * 1:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 1:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard % 1 == 0 and waard <= 5 * 1:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
                                    try:
                                        waarde = eval(veld+waarde)
                                        if waarde % 1 == 0 and waarde <= 5 * 1:
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    except:
                                        print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "2":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if waarde % 2 == 0 and waarde <= 5 * 2:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 2:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard % 2 == 0 and waard <= 5 * 2:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
                                    try:
                                        waarde = eval(veld+waarde)
                                        if waarde % 2 == 0 and waarde <= 5 * 2:
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    except:
                                        print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "3":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if waarde % 3 == 0 and waarde <= 5 * 3:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 3:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard % 3 == 0 and waard <= 5 * 3:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
                                    try:
                                        waarde = eval(veld+waarde)
                                        if waarde % 3 == 0 and waarde <= 5 * 3:
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    except:
                                        print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "4":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if waarde % 4 == 0 and waarde <= 5 * 4:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 4:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard % 4 == 0 and waard <= 5 * 4:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
                                    try:
                                        waarde = eval(veld+waarde)
                                        if waarde % 4 == 0 and waarde <= 5 * 4:
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    except:
                                        print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "5":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if waarde % 5 == 0 and waarde <= 5 * 5:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 5:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard % 5 == 0 and waard <= 5 * 5:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
                                    try:
                                        waarde = eval(veld+waarde)
                                        if waarde % 5 == 0 and waarde <= 5 * 5:
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    except:
                                        print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "6":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if waarde % 6 == 0 and waarde <= 5 * 6:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 6:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard % 6 == 0 and waard <= 5 * 6:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                    else:
                                        print(waardeongeldig)
                                except:
                                    try:
                                        waarde = eval(veld+waarde)
                                        if waarde % 6 == 0 and waarde <= 5 * 6:
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    except:
                                        print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "10":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if 5 <= waarde <= 5 * 6:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 6:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard <= 5 * 6:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
                                    print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "11":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if 5 <= waarde <= 5 * 6:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 6:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard <= 5 * 6:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
                                    print(waardeongeldig)
                            else:
                                print(veldbezet)
                        elif veld == "12":
                            if scoretabel[i-1][int(veld)-1] == "":
                                waarde = 25
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(veldbezet)
                        elif veld == "13":
                            if scoretabel[i-1][int(veld)-1] == "":
                                waarde = 30
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(veldbezet)
                        elif veld == "14":
                            if scoretabel[i-1][int(veld)-1] == "":
                                waarde = 40
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(veldbezet)
                        elif veld == "15":
                            if scoretabel[i-1][int(veld)-1] == "":
                                waarde = 50
                                scoretabel[i-1][int(veld)-1] = waarde
                                score = True
                            else:
                                print(veldbezet)
                        elif veld == "16":
                            if scoretabel[i-1][int(veld)-1] == "":
                                try:
                                    waarde = eval(waarde)
                                    if 5 <= waarde <= 5 * 6:
                                        scoretabel[i-1][int(veld)-1] = waarde
                                        score = True
                                    elif waarde > 5 * 6:
                                        waard = 0
                                        for j in str(waarde):
                                            waard += int(j)
                                        if waard <= 5 * 6:
                                            waarde = waard
                                            scoretabel[i-1][int(veld)-1] = waarde
                                            score = True
                                        else:
                                            print(waardeongeldig)
                                    else:
                                        print(waardeongeldig)
                                except:
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
        maxscorelijst[spelerslijst.index(speler)] = scoretabel[i-1][18]
    spel += 1 
winnaar = spelerslijst[maxscorelijst.index(max(maxscorelijst))]
bouwtabel(maxscorelijst,speler,spel,winnaar)
print(wint % (Goed+winnaar+ResetAll,Resultaat+str(max(maxscorelijst))+ResetAll))
print()
