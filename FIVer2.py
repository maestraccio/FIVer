#!/usr/bin/python3
version = "1.2"
datum = "20230105"

import random

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
Bevestiging            = LightCyan
Tekst                  = LightMagenta
SubTekst               = Magenta
Goed                   = LightGreen
SubGoed                = Green
Matig                  = Yellow
Resultaat              = LightYellow
Slecht                 = LightRed
Tabel                  = LightBlue
SubTabel               = Blue
Terug                  = DarkGray
Wit                    = White
for2 = "{:>2}".format
forc3 = "{:^3}".format
forl3 = "{:<3}".format
forr3 = "{:>3}".format
forl10 =  "{:<10}".format
forc10 =  "{:^10}".format
forr10 =  "{:>10}".format
forl15 =  "{:<15}".format
forc15 =  "{:^15}".format
forr15 =  "{:>15}".format
forl41 =  "{:<41}".format
forc41 =  "{:^41}".format
forr41 =  "{:>41}".format
forl83 =  "{:<83}".format
forc83 =  "{:^83}".format
forr83 =  "{:>83}".format
forcall = "{:^86}".format
jalijst = ["Y","J","S"]
neelijst = ["N"]
afsluitlijst = ["Q","X"]
emptyscoretable = [
        15*"=",
        "   %sF I V er%s    " % (Resultaat,ResetAll),
        15*"-",
        7*" "+Tekst+"1"+ResetAll+7*" ",
        7*" "+Tekst+"2"+ResetAll+7*" ",
        7*" "+Tekst+"3"+ResetAll+7*" ",
        7*" "+Tekst+"4"+ResetAll+7*" ",
        7*" "+Tekst+"5"+ResetAll+7*" ",
        7*" "+Tekst+"6"+ResetAll+7*" ",
        15*"-",
        "%sSUBTOTAL UPPER%s " % (SubTekst,ResetAll),
        "     %sBONUS%s     " % (Matig,ResetAll),
        "  %sTOTAL UPPER%s  " % (SubGoed,ResetAll),
        15*"-",
        "%shree of a %sind%s" % (Tekst+"T"+SubTekst,Tekst+"K"+SubTekst,ResetAll),
        "%sour of a %sind%s " % (Tekst+"F"+SubTekst,Tekst+"K"+SubTekst,ResetAll),
        "%sull %souse    %s " % (Tekst+"F"+SubTekst,Tekst+"H"+SubTekst,ResetAll),
        "%small %straight %s" % (Tekst+"S"+SubTekst,Tekst+"S"+SubTekst,ResetAll),
        "%sarge %straight %s" % (Tekst+"L"+SubTekst,Tekst+"S"+SubTekst,ResetAll),
        "   %s I %s er%s    " % (Tekst+"F"+SubTekst,Tekst+"V"+SubTekst,ResetAll),
        "%sree %shoice%s    " % (Tekst+"F"+SubTekst,Tekst+"C"+SubTekst,ResetAll),
        15*"-",
        "  %sTOTAL LOWER%s  " % (SubTekst,ResetAll),
        "  %sTOTAL UPPER%s  " % (SubGoed,ResetAll),
        "  %sGRAND TOTAL%s  " % (Goed,ResetAll),
        15*"="
]
emptyscoretablecompact = [
        2*"=",
        "%sFV%s" % (Resultaat,ResetAll),
        2*"-",
        " "+Tekst+"1"+ResetAll,
        " "+Tekst+"2"+ResetAll,
        " "+Tekst+"3"+ResetAll,
        " "+Tekst+"4"+ResetAll,
        " "+Tekst+"5"+ResetAll,
        " "+Tekst+"6"+ResetAll,
        2*"-",
        "%sSU%s" % (SubTekst,ResetAll),
        "%sBS%s" % (Matig,ResetAll),
        "%sTU%s" % (SubGoed,ResetAll),
        2*"-",
        "%s" % (Tekst+"TK"+ResetAll),
        "%s" % (Tekst+"FK"+ResetAll),
        "%s" % (Tekst+"FH"+ResetAll),
        "%s" % (Tekst+"SS"+ResetAll),
        "%s" % (Tekst+"LS"+ResetAll),
        "%s" % (Tekst+"FV"+ResetAll),
        "%s" % (Tekst+"FC"+ResetAll),
        2*"-",
        "%sTL%s" % (SubTekst,ResetAll),
        "%sTU%s" % (SubGoed,ResetAll),
        "%sTT%s" % (Goed,ResetAll),
        2*"="
]
emptyscoretableNL = [
        15*"=",
        "   %sF I V er%s    " % (Resultaat,ResetAll),
        15*"-",
        7*" "+Tekst+"1"+ResetAll+7*" ",
        7*" "+Tekst+"2"+ResetAll+7*" ",
        7*" "+Tekst+"3"+ResetAll+7*" ",
        7*" "+Tekst+"4"+ResetAll+7*" ",
        7*" "+Tekst+"5"+ResetAll+7*" ",
        7*" "+Tekst+"6"+ResetAll+7*" ",
        15*"-",
        "%sSUBTOTAAL BOVEN%s" % (SubTekst,ResetAll),
        "     %sBONUS%s     " % (Matig,ResetAll),
        " %sTOTAAL BOVEN%s  " % (SubGoed,ResetAll),
        15*"-",
        "%srie %sezelfde  %s" % (Tekst+"D"+SubTekst,Tekst+"D"+SubTekst,ResetAll),
        "%sier %sezelfde  %s" % (Tekst+"V"+SubTekst,Tekst+"D"+SubTekst,ResetAll),
        "%sol %suis       %s" % (Tekst+"V"+SubTekst,Tekst+"H"+SubTekst,ResetAll),
        "%sleine %straat  %s" % (Tekst+"K"+SubTekst,Tekst+"S"+SubTekst,ResetAll),
        "%srote %straat   %s" % (Tekst+"G"+SubTekst,Tekst+"S"+SubTekst,ResetAll),
        "   %s I %s er%s    " % (Tekst+"F"+SubTekst,Tekst+"V"+SubTekst,ResetAll),
        "%srije %seus     %s" % (Tekst+"V"+SubTekst,Tekst+"K"+SubTekst,ResetAll),
        15*"-",
        " %sTOTAAL ONDER%s  " % (SubTekst,ResetAll),
        " %sTOTAAL BOVEN%s  " % (SubGoed,ResetAll),
        " %sTOTAAL ALLES%s  " % (Goed,ResetAll),
        15*"="
]
emptyscoretablecompactNL = [
        2*"=",
        "%sFV%s" % (Resultaat,ResetAll),
        2*"-",
        " "+Tekst+"1"+ResetAll,
        " "+Tekst+"2"+ResetAll,
        " "+Tekst+"3"+ResetAll,
        " "+Tekst+"4"+ResetAll,
        " "+Tekst+"5"+ResetAll,
        " "+Tekst+"6"+ResetAll,
        2*"-",
        "%sSB%s" % (SubTekst,ResetAll),
        "%sBS%s" % (Matig,ResetAll),
        "%sTB%s" % (SubGoed,ResetAll),
        2*"-",
        "%s" % (Tekst+"DD"+ResetAll),
        "%s" % (Tekst+"VD"+ResetAll),
        "%s" % (Tekst+"VH"+ResetAll),
        "%s" % (Tekst+"KS"+ResetAll),
        "%s" % (Tekst+"GS"+ResetAll),
        "%s" % (Tekst+"FV"+ResetAll),
        "%s" % (Tekst+"VK"+ResetAll),
        2*"-",
        "%sTO%s" % (SubTekst,ResetAll),
        "%sTB%s" % (SubGoed,ResetAll),
        "%sTA%s" % (Goed,ResetAll),
        2*"="
]
pipeline = ["#","|","+","|","|","|","|","|","|","+","|","|","|","+","|","|","|","|","|","|","|","+","|","|","|","#"]

def playeradd():
    playercount = 0
    playeradd = "Y"
    playerlist = []
    playertableslist = []
    while playeradd == "Y":
        if taal == "EN":
            newplayer = input("Enter the name of the new player (max 10 characters) or \"%sS%s\" to Start\n  : " % (Tekst,ResetAll))[:10]
        else:
            newplayer = input("Naam van de nieuwe speler (max 10 karakters) of \"%sS%s\" om te Starten\n  : " % (Tekst,ResetAll))[:10]
        if newplayer.upper() in afsluitlijst:
            exit()
        elif newplayer.upper() == "S":
            if len(playerlist) == 0:
                if taal == "EN":
                    newplayer = "One_Player"
                else:
                    newplayer = "Eén_Speler"
                print(Goed+newplayer+ResetAll)
                playertableslist = [[10*"=",newplayer,10*"-","","","","","","",10*"-",0,0,0,10*"-","","","","","","","",10*"-",0,0,0,10*"="]]
            break
        else:
            playercount += 1
            if newplayer == "":
                if taal == "EN":
                    newplayer = "Player_"+str(playercount)+(10-len("Player_"+str(playercount)))*" "
                else:
                    newplayer = "Speler_"+str(playercount)+(10-len("Speler_"+str(playercount)))*" "
                print(Goed+newplayer+ResetAll)
            else:
                newplayer = newplayer+(10-len(newplayer))*" "
                print(Goed+newplayer+ResetAll)
            playerlist.append(newplayer)
    for i in playerlist:
        scores = [10*"=",i,10*"-","","","","","","",10*"-",0,0,0,10*"-","","","","","","","",10*"-",0,0,0,10*"="]
        playertableslist.append(scores)
    return playertableslist

def showall():
    if len(playertableslist) > 4:
        if taal == "EN":
            scoretable = emptyscoretablecompact
        else:
            scoretable = emptyscoretablecompactNL
    else:
        if taal == "EN":
            scoretable = emptyscoretable
        else:
            scoretable = emptyscoretableNL
    for i in range(len(scoretable)):
        for j in range(len(playertableslist)):
            if j == 0:
                print(Tabel+pipeline[i]+ResetAll+scoretable[i]+Tabel+pipeline[i]+ResetAll+forr10(playertableslist[j][i]), end = "")
            else:
                print(Tabel+pipeline[i]+ResetAll+forr10(playertableslist[j][i]), end = "")
        print(Tabel+pipeline[i]+ResetAll)

def suggestions():
    suggestionslist = []
    if A == B == C and C != D:
        sug = "%s @ %s" % (Goed+for2(A+B+C)+ResetAll,Tekst+str(A)+ResetAll)
        suggestionslist.append(sug)
    if B == C == D and A != B and D != E:
        sug = "%s @ %s" % (Goed+for2(B+C+D)+ResetAll,Tekst+str(B)+ResetAll)
        suggestionslist.append(sug)
    if C == D == E and B != C:
        sug = "%s @ %s" % (Goed+for2(C+D+E)+ResetAll,Tekst+str(C)+ResetAll)
        suggestionslist.append(sug)
    if A == B == C == D and D != E:
        sug = "%s @ %s" % (Goed+for2(A+B+C+D)+ResetAll,Tekst+str(A)+ResetAll)
        suggestionslist.append(sug)
    if B == C == D == E and A != B:
        sug = "%s @ %s" % (Goed+for2(B+C+D+E)+ResetAll,Tekst+str(B)+ResetAll)
        suggestionslist.append(sug)
    if (A == B == C == D == E):
        sug = "%s @ %s" % (Goed+for2(A+B+C+D+E)+ResetAll,Tekst+str(A)+ResetAll)
        suggestionslist.append(sug)
    if (A == B == C == D == E):
        if taal == "EN":
            sug = "%s @ %s" % (Goed+for2(50)+ResetAll,Tekst+"FV"+ResetAll)
        else:
            sug = "%s @ %s" % (Goed+for2(50)+ResetAll,Tekst+"FV"+ResetAll)
        suggestionslist.append(sug)
    if (A == B-1 and B == C-1 and C == D-1 and D == E-1):
        if taal == "EN":
            sug = "%s @ %s" % (Goed+for2(40)+ResetAll,Tekst+"LS"+ResetAll)
        else:
            sug = "%s @ %s" % (Goed+for2(40)+ResetAll,Tekst+"GS"+ResetAll)
        suggestionslist.append(sug)
    if (B == C-1 and C == D-1 and D == E-1) or (A == C-1 and C == D-1 and D == E-1) or (A == B-1 and B == D-1 and D == E-1) or (A == B-1 and B == C-1 and C == E-1) or (A == B-1 and B == C-1 and C == D-1):
        if taal == "EN":
            sug = "%s @ %s" % (Goed+for2(30)+ResetAll,Tekst+"SS"+ResetAll)
        else:
            sug = "%s @ %s" % (Goed+for2(30)+ResetAll,Tekst+"KS"+ResetAll)
        suggestionslist.append(sug)
    if (A == B == C and D == E) or (A == B and C == D == E):
        if taal == "EN":
            sug = "%s @ %s" % (Goed+for2(25)+ResetAll,Tekst+"FH"+ResetAll)
        else:
            sug = "%s @ %s" % (Goed+for2(25)+ResetAll,Tekst+"VH"+ResetAll)
        suggestionslist.append(sug)
    if (A == B == C == D) or (B == C == D == E):
        if taal == "EN":
            sug = "%s @ %s" % (Goed+for2(A+B+C+D+E)+ResetAll,Tekst+"FK"+ResetAll)
        else:
            sug = "%s @ %s" % (Goed+for2(A+B+C+D+E)+ResetAll,Tekst+"VD"+ResetAll)
        suggestionslist.append(sug)
    if (A == B == C) or (B == C == D) or (C == D == E):
        if taal == "EN":
            sug = "%s @ %s" % (Goed+for2(A+B+C+D+E)+ResetAll,Tekst+"TK"+ResetAll)
        else:
            sug = "%s @ %s" % (Goed+for2(A+B+C+D+E)+ResetAll,Tekst+"DD"+ResetAll)
        suggestionslist.append(sug)
    if A == B and B != C:
        sug = "%s @ %s" % (for2(A+B),str(A))
        suggestionslist.append(sug)
    if A != B and B == C and C != D:
        sug = "%s @ %s" % (for2(B+C),str(B))
        suggestionslist.append(sug)
    if B != C and C == D and D != E:
        sug = "%s @ %s" % (for2(C+D),str(C))
        suggestionslist.append(sug)
    if C != D and D == E:
        sug = "%s @ %s" % (for2(D+E),str(D))
        suggestionslist.append(sug)
    if taal == "EN":
        sug = "%s @ %s" % (for2(A+B+C+D+E),"FC")
    else:
        sug = "%s @ %s" % (for2(A+B+C+D+E),"VK")
    suggestionslist.append(sug)
    count = 1
    for i in suggestionslist:
        print(str(count)+": "+i)
        count += 1
    return suggestionslist

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
        #start = input()
        #if start.upper() in afsluitlijst:
        #    exit()
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
        if taal == "EN":
            print("#1 %sROLL all dice%s:" % (Tekst,ResetAll))
        else:
            print("#1 %sROL alle dobbelstenen%s:" % (Tekst,ResetAll))
        print(DarkGray+"   %s     %s     %s     %s     %s" % (A,B,C,D,E)+ResetAll)
        counti = 0
        for i in Dice:
            print(i, end = "")
            counti += 1
            if counti % 5 == 0:
                print()
        print(Wit+"   A     B     C     D     E"+ResetAll)
        if taal == "EN":
            choice = input("#2 %sCHOOSE%s which dice %sto ROLL%s\n  : " % (Tekst,ResetAll,Tekst,ResetAll)).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        else:
            choice = input("#2 %sKIES%s welke stenen je wilt %sROLLEN%s\n  : " % (Tekst,ResetAll,Tekst,ResetAll)).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() in afsluitlijst:
            exit()
        Secondroll = Firstroll
        for i in choice:
            if i == "A":
                Secondroll[0] = random.choice(range(1,7))
            if i == "B":
                Secondroll[1] = random.choice(range(1,7))
            if i == "C":
                Secondroll[2] = random.choice(range(1,7))
            if i == "D":
                Secondroll[3] = random.choice(range(1,7))
            if i == "E":
                Secondroll[4] = random.choice(range(1,7))
        Secondroll = sorted(Secondroll)
        A = Secondroll[0]
        B = Secondroll[1]
        C = Secondroll[2]
        D = Secondroll[3]
        E = Secondroll[4]
        Dice = visualDice()
        print(DarkGray+"   %s     %s     %s     %s     %s" % (A,B,C,D,E)+ResetAll)
        counti = 0
        for i in Dice:
            print(i, end = "")
            counti += 1
            if counti % 5 == 0:
                print()
        print(Wit+"   A     B     C     D     E"+ResetAll)
        if taal == "EN":
            choice = input("#3 %sCHOOSE%s which dice %sto ROLL%s or \"S\"\n  : " % (Tekst,ResetAll,Tekst,ResetAll)).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        else:
            choice = input("#3 %sKIES%s welke stenen je wilt %sROLLEN%s\n  : " % (Tekst,ResetAll,Tekst,ResetAll)).replace(" ","").replace(",","").replace(".","").replace("-","").replace("/","").replace("\\","").upper()
        if choice.upper() in afsluitlijst:
            exit()
        Thirdroll = Secondroll
        for i in choice:
            if i == "A":
                Thirdroll[0] = random.choice(range(1,7))
            if i == "B":
                Thirdroll[1] = random.choice(range(1,7))
            if i == "C":
                Thirdroll[2] = random.choice(range(1,7))
            if i == "D":
                Thirdroll[3] = random.choice(range(1,7))
            if i == "E":
                Thirdroll[4] = random.choice(range(1,7))
        Thirdroll = sorted(Thirdroll)
        A = Thirdroll[0]
        B = Thirdroll[1]
        C = Thirdroll[2]
        D = Thirdroll[3]
        E = Thirdroll[4]
        Dice = visualDice()
        print(DarkGray+"   %s     %s     %s     %s     %s" % (A,B,C,D,E)+ResetAll)
        counti = 0
        for i in Dice:
            print(i, end = "")
            counti += 1
            if counti % 5 == 0:
                print()
        print(Wit+"   A     B     C     D     E"+ResetAll)
        return A,B,C,D,E

def calcstuff():
    if taal == "EN":
        calclist = [41*"=","Techy tips %s(!= try @home)%s" % (DarkGray,ResetAll)+16*" ",41*"-","","","","","","",41*"-","","","",41*"-","","","","","","","",41*"-","","","",41*"="]
    else:
        calclist = [41*"=","Techy tips %s(!= try @home)%s" % (DarkGray,ResetAll)+16*" ",41*"-","","","","","","",41*"-","","","",41*"-","","","","","","","",41*"-","","","",41*"="]
    for i in playertableslist:
        if i[1] == player:
            bonusscore = 0
            if i[3] == "":
                bonussum = 0
                calclist[3] = "1 = sum(for if == 1)"
            elif i[3] < 3:
                bonussum = (3-i[3])*-1
                bonusscore += bonussum
                if taal == "EN":
                    calclist[3] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                else:
                    calclist[3] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
            elif i[3] == 3:
                if taal == "EN":
                    calclist[3] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                else:
                    calclist[3] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
            else:
                bonussum = i[3]-3
                bonusscore += bonussum
                if taal == "EN":
                    calclist[3] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                else:
                    calclist[3] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
            if i[4] == "":
                bonussum = 0
                calclist[4] = "2 = sum(for if == 2)"
            elif i[4] < 6:
                bonussum = (6-i[4])*-1
                bonusscore += bonussum
                if taal == "EN":
                    calclist[4] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                else:
                    calclist[4] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
            elif i[4] == 6:
                if taal == "EN":
                    calclist[4] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                else:
                    calclist[4] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
            else:
                bonussum = i[4]-6
                bonusscore += bonussum
                if taal == "EN":
                    calclist[4] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                else:
                    calclist[4] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
            if i[5] == "":
                bonussum = 0
                calclist[5] = "3 = sum(for if == 3)"
            elif i[5] < 9:
                bonussum = (9-i[5])*-1
                bonusscore += bonussum
                if taal == "EN":
                    calclist[5] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                else:
                    calclist[5] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
            elif i[5] == 9:
                if taal == "EN":
                    calclist[5] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                else:
                    calclist[5] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
            else:
                bonussum = i[5]-9
                bonusscore += bonussum
                if taal == "EN":
                    calclist[5] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                else:
                    calclist[5] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
            if i[6] == "":
                bonussum = 0
                calclist[6] = "4 = sum(for if == 4)"
            elif i[6] < 12:
                bonussum = (12-i[6])*-1
                bonusscore += bonussum
                if taal == "EN":
                    calclist[6] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                else:
                    calclist[6] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
            elif i[6] == 12:
                if taal == "EN":
                    calclist[6] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                else:
                    calclist[6] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
            else:
                bonussum = i[6]-12
                bonusscore += bonussum
                if taal == "EN":
                    calclist[6] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                else:
                    calclist[6] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
            if i[7] == "":
                bonussum = 0
                calclist[7] = "5 = sum(for if == 5)"
            elif i[7] < 15:
                bonussum = (15-i[7])*-1
                bonusscore += bonussum
                if taal == "EN":
                    calclist[7] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                else:
                    calclist[7] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
            elif i[7] == 15:
                if taal == "EN":
                    calclist[7] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                else:
                    calclist[7] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
            else:
                bonussum = i[7]-15
                bonusscore += bonussum
                if taal == "EN":
                    calclist[7] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                else:
                    calclist[7] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
            if i[8] == "":
                bonussum = 0
                calclist[8] = "6 = sum(for if == 6)"
            elif i[8] < 18:
                bonussum = (18-i[8])*-1
                bonusscore += bonussum
                if taal == "EN":
                    calclist[8] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                else:
                    calclist[8] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
            elif i[8] == 18:
                if taal == "EN":
                    calclist[8] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                else:
                    calclist[8] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
            else:
                bonussum = i[8]-18
                bonusscore += bonussum
                if taal == "EN":
                    calclist[8] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                else:
                    calclist[8] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
            sumup = 0
            for j in i[3:9]:
                if j != "":
                    sumup += j
            i[10] = sumup
            if taal == "EN":
                calclist[10] = "if () in UPPER % 3: SUBTOTAL UPPER = 63"
            else:
                calclist[10] = "if () in BOVEN % 3: SUBTOTAAL BOVEN = 63"
            if "" in i[3:9] and sumup < 63:
                if taal == "EN":
                    calclist[11] = "if SUBTOTAL UPPER >= 63: BONUS = 35"
                else:
                    calclist[11] = "if SUBTOTAAL BOVEN >= 63: BONUS = 35"
            elif sumup < 63 and "" not in i[3:9]:
                if taal == "EN":
                    calclist[11] = "Failed, BONUS not achieved"
                else:
                    calclist[11] = "Mislukt, BONUS niet behaald"
            else:
                i[11] = 35
                if taal == "EN":
                    calclist[11] = 9*" "+"Success, %s achieved" % (Matig+"BONUS"+ResetAll)+9*" "
                else:
                    calclist[11] = 10*" "+"Gelukt, %s behaald" % (Matig+"BONUS"+ResetAll)+10*" "
            subsumup = i[10]+i[11]
            i[12] = subsumup
            i[23] = subsumup
            if bonusscore > 0:
                if taal == "EN":
                    bonushint = "%s over BONUS target" % (Goed+forr3(bonusscore)+ResetAll)+20*" "
                else:
                    bonushint = "%s boven BONUS target" % (Goed+forr3(bonusscore)+ResetAll)+19*" "
            elif bonusscore < 0:
                if taal == "EN":
                    bonushint = "%s below BONUS target" % (Slecht+forr3(bonusscore)+ResetAll)+19*" "
                else:
                    bonushint = "%s onder BONUS target" % (Slecht+forr3(bonusscore)+ResetAll)+19*" "
            else:
                if taal == "EN":
                    bonushint = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                else:
                    bonushint = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
            calclist[12] = bonushint
            if i[14] == "":
                if taal == "EN": 
                    calclist[14] = "if count(=) >= 3:         TK = sum()"
                else:
                    calclist[14] = "if count(=) >= 3:         DD = sum()"
            else:
                if taal == "EN":
                    calclist[14] = "completed"
                else:
                    calclist[14] = "klaar"
            if i[15] == "":
                if taal == "EN":
                    calclist[15] = "if count(=) >= 4:         FK = sum()"
                else:
                    calclist[15] = "if count(=) >= 4:         VD = sum()"
            else:
                if taal == "EN":
                    calclist[15] = "completed"
                else:
                    calclist[15] = "klaar"
            if i[16] == "":
                if taal == "EN":
                    calclist[16] = "if for count(=) in [2,3]: FH = 25"
                else:
                    calclist[16] = "if for count(=) in [2,3]: VH = 25"
            else:
                if taal == "EN":
                    calclist[16] = "completed"
                else:
                    calclist[16] = "klaar"
            if i[17] == "":
                if taal == "EN":
                    calclist[17] = "if count(+1 =) >= 4:      SS = 30"
                else:
                    calclist[17] = "if count(+1 =) >= 4:      KS = 30"
            else:
                if taal == "EN":
                    calclist[17] = "completed"
                else:
                    calclist[17] = "klaar"
            if i[18] == "":
                if taal == "EN":
                    calclist[18] = "if count(+1 =) == 5:      LS = 40"
                else:
                    calclist[18] = "if count(+1 =) == 5:      GS = 40"
            else:
                if taal == "EN":
                    calclist[18] = "completed"
                else:
                    calclist[18] = "klaar"
            if i[19] == "":
                if taal == "EN":
                    calclist[19] = "if count(=) == 5:         FV = 50"
                else:
                    calclist[19] = "if count(=) == 5:         FV = 50"
            else:
                if taal == "EN":
                    calclist[19] = "bummer"
                else:
                    calclist[19] = "jammer"
            if i[20] == "":
                if taal == "EN":
                    calclist[20] = "                          FC = sum()"
                else:
                    calclist[20] = "                          VK = sum()"
            else:
                if taal == "EN":
                    calclist[20] = "completed"
                else:
                    calclist[20] = "klaar"
            sumlow = 0
            for j in i[14:21]:
                if j != "":
                    sumlow += j
            i[22] = sumlow
            i[24] = i[22] + i[23]
    return calclist

def showone():
    if taal == "EN":
        scoretable = emptyscoretable
    else:
        scoretable = emptyscoretableNL
    for i in playertableslist:
        if i[1] == player:
            i[1] = Goed+player+ResetAll
            for j in range(len(scoretable)):
                print(pipeline[j]+scoretable[j]+pipeline[j]+forr10(i[j])+pipeline[j]+forl41(calclist[j]), end = "")
                print(pipeline[j])
            i[1] = i[1].replace(Goed,"").replace(ResetAll,"")

print()
print(Tabel+"+ -"+ResetAll+forcall(Resultaat+"- %s F I V er %s -" % (Reverse,ResetAll+Resultaat)+ResetAll)+Tabel+"- +"+ResetAll)
print()

taal = input("%sFirst select your language%s | %sKies eerst je taal%s\n>1: %sEnglish%s\n 2: %sNederlands%s\n  : " % (Tekst,ResetAll,Tekst,ResetAll,Wit,ResetAll,Resultaat,ResetAll))
if taal.upper() in afsluitlijst:
    exit()
elif taal == "2":
    taal = "NL"
    print("%sNederlands%s" % (Goed,ResetAll))
else:
    taal = "EN"
    print("%sEnglish%s" % (Goed,ResetAll))
if taal == "EN":
    print("%sThen add one ore more players%s" % (Tekst,ResetAll))
else:
    print("%sVoeg dan één of meer spelers toe%s" % (Tekst,ResetAll))
playertableslist = playeradd()
disman = "0"
skiproll = "N"
if taal == "EN":
    alea = input("%sAnd last%s\nRoll %svirtual%s or %sphysical%s dice\n>1: %svirtual%s\n 2: %sphysical%s\n  : " % (Tekst,ResetAll,Wit,ResetAll,Resultaat,ResetAll,Wit,ResetAll,Resultaat,ResetAll))
else:
    alea = input("%sEn als laatste%s\nSpeel met %svirtuele%s of %sfysieke%s dobbelstenen\n>1: %svirtuele%s\n 2: %sfysieke%s\n  : " % (Tekst,ResetAll,Wit,ResetAll,Resultaat,ResetAll,Wit,ResetAll,Resultaat,ResetAll))
if alea.upper() in afsluitlijst:
    exit()
elif alea == "2":
    skiproll = "Y"
    if taal == "EN":
        print("%sphysical%s" % (Goed,ResetAll))
    else:
        print("%sfysieke%s" % (Goed,ResetAll))
else:
    if taal == "EN":
        print("%sVirtual dice%s" % (Goed,ResetAll))
        disman = input("%sOk, one more question%s\n>1: %smanual entry allowed%s\n 2: %sonly suggested%s\n  : " % (Tekst,ResetAll,Wit,ResetAll,Resultaat,ResetAll))
        if disman.upper() in afsluitlijst:
            exit()
        elif disman == "2":
            print("%sonly suggested%s" % (Goed,ResetAll))
        else:
            disman = "1"
    else:
        print("%sVirtuele dobbelstenen%s" % (Goed,ResetAll))
        disman = input("%sOk, één vraag dan nog%s\n>1: %stoestaan handmatige invoer%s\n 2: %salleen suggesties%s\n  : " % (Tekst,ResetAll,Wit,ResetAll,Resultaat,ResetAll))
        if disman.upper() in afsluitlijst:
            exit()
        elif disman == "2":
            print("%salleen suggesties%s" % (Goed,ResetAll))
if taal == "EN":
    print(forc83("%s Have fun %s" % (Reverse+Tekst,ResetAll)))
else:
    print(forc83("%s Veel plezier %s" % (Reverse+Tekst,ResetAll)))

playround = 0
while playround < 13 :
    playround += 1
    if len(playertableslist) > 1:
        print()
        showall()
    players = []
    scores = []
    for i in playertableslist:
        players.append(i[1])
        scores.append(i[24])
    if len(players) > 1:
        topscore = max(scores)
        counttops = 0
        for i in scores:
            if i == topscore:
                counttops += 1
        if counttops == 1:
            topplayer = players[scores.index(topscore)]
            if taal == "EN":
                print("%s is ahead @ %s points" % (Goed+topplayer.strip()+ResetAll,Goed+str(topscore)+ResetAll))
            else:
                print("%s staat vóór @ %s punten" % (Goed+topplayer.strip()+ResetAll,Goed+str(topscore)+ResetAll))
        elif counttops == len(playertableslist) and playround != 1:
            if taal == "EN":
                print("Draw @ %s points" % (SubGoed+str(topscore)+ResetAll))
            else:
                print("Gelijkspel @ %s punten" % (SubGoed+str(topscore)+ResetAll))
        elif counttops != len(playertableslist) and playround != 1:
            if taal == "EN":
                print("The players @ %s points are ahead" % (SubGoed+str(topscore)+ResetAll))
            else:
                print("De spelers @ %s punten staan vóór" % (SubGoed+str(topscore)+ResetAll))
    print()
    if taal == "EN":
        print("ROUND #%s" % (Resultaat+str(playround)+ResetAll))
    else:
        print("RONDE #%s" % (Resultaat+str(playround)+ResetAll))
    for i in playertableslist:
        print()
        player = i[1]
        if len(playertableslist) > 1:
            if taal == "EN":
                print("%s's turn" % (Goed+player.strip()+ResetAll))
            else:
                print("%s is aan de beurt" % (Goed+player.strip()+ResetAll))
        calclist = calcstuff()
        showone()
        if skiproll == "Y":
            print()
        else:
            rolls = roll()
            A = rolls[0]
            B = rolls[1]
            C = rolls[2]
            D = rolls[3]
            E = rolls[4]
        checkinput = "Y"
        while checkinput == "Y":
            chk = "N"
            if skiproll != "Y":
                suggestionslist = suggestions()
            writeifvalid = "Y"
            while writeifvalid == "Y":
                if skiproll == "Y":
                    if taal == "EN":
                        score = input("Enter your score like \"%sRESULT%s @ %sWHERE%s\"\n  : " % (Goed,ResetAll,Tekst,ResetAll)).replace(" ","")
                    else:
                        score = input("Voer je score in als \"%sRESULTAAT%s @ %sWAAR%s\"\n  : " % (Goed,ResetAll,Tekst,ResetAll)).replace(" ","")
                else:
                    if taal == "EN":
                        if disman == "2":
                            score = input("Choose a suggestion\n  : ").replace(" ","")
                        else:
                            score = input("Choose a suggestion or enter your score like \"%sRESULT%s @ %sWHERE%s\"\n  : " % (Goed,ResetAll,Tekst,ResetAll)).replace(" ","")
                    else:
                        if disman == "2":
                            score = input("Kies een suggestie\n  : ").replace(" ","")
                        else:
                            score = input("Kies een suggestie of voer je score in als \"%sRESULTAAT%s @ %sWAAR%s\"\n  : " % (Goed,ResetAll,Tekst,ResetAll)).replace(" ","")
                if score.upper() in afsluitlijst:
                    exit()
                try:
                    intscore = int(score)-1
                    if intscore in range(len(suggestionslist)):
                        score = suggestionslist[intscore].replace(" ","").replace(Goed,"").replace(Tekst,"").replace(ResetAll,"")
                    else:
                        intscore = int(endederror)
                except(Exception) as error:
                    #print(error)
                    if disman == "2" and len(score) > 1 and score[0] == "/":
                        pass
                    elif disman == "2":
                        break
                    else:
                        pass
                if taal == "EN":
                    if not "@" in score:
                        if (score.upper() in ["FV","50","YAY","OK","YES"] or score.upper() in jalijst) and i[19] == "":
                            i[19] = 50
                            calclist[19] = "completed"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["SHIT","FUCK","BITCH","DAMN","NO"] or score.upper() in neelijst) and i[19] == "":
                            i[19] = 0
                            calclist[19] = "bummer"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["LS","40"]) and i[18] == "":
                            i[18] = 40
                            calclist[18] = "completed"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[18]+ResetAll+emptyscoretable[18]+Tabel+pipeline[18]+ResetAll+Goed+forr10(i[18])+ResetAll+Tabel+pipeline[18]+ResetAll+forl41(calclist[18])+Tabel+pipeline[18]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["SS","30"]) and i[17] == "":
                            i[17] = 30
                            calclist[17] = "completed"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[17]+ResetAll+emptyscoretable[17]+Tabel+pipeline[17]+ResetAll+Goed+forr10(i[17])+ResetAll+Tabel+pipeline[17]+ResetAll+forl41(calclist[17])+Tabel+pipeline[17]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["FH","25"]) and i[16] == "":
                            i[16] = 25
                            calclist[16] = "completed"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[16]+ResetAll+emptyscoretable[16]+Tabel+pipeline[16]+ResetAll+Goed+forr10(i[16])+ResetAll+Tabel+pipeline[16]+ResetAll+forl41(calclist[16])+Tabel+pipeline[16]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif len(score) > 1 and score[0] == "/":
                            if score[1:] == "1" and i[3] == "":
                                i[3] = 0
                                bonussum = -3 * 1
                                calclist[3] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[3]+ResetAll+emptyscoretable[3]+Tabel+pipeline[3]+ResetAll+Goed+forr10(i[3])+ResetAll+Tabel+pipeline[3]+ResetAll+forl41(calclist[3])+Tabel+pipeline[3]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "2" and i[4] == "":
                                i[4] = 0
                                bonussum = -3 * 2
                                calclist[4] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[4]+ResetAll+emptyscoretable[4]+Tabel+pipeline[4]+ResetAll+Goed+forr10(i[4])+ResetAll+Tabel+pipeline[4]+ResetAll+forl41(calclist[4])+Tabel+pipeline[4]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "3" and i[5] == "":
                                i[5] = 0
                                bonussum = -3 * 3
                                calclist[5] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[5]+ResetAll+emptyscoretable[5]+Tabel+pipeline[5]+ResetAll+Goed+forr10(i[5])+ResetAll+Tabel+pipeline[5]+ResetAll+forl41(calclist[5])+Tabel+pipeline[5]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "4" and i[6] == "":
                                i[6] = 0
                                bonussum = -3 * 4
                                calclist[6] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[6]+ResetAll+emptyscoretable[6]+Tabel+pipeline[6]+ResetAll+Goed+forr10(i[6])+ResetAll+Tabel+pipeline[6]+ResetAll+forl41(calclist[6])+Tabel+pipeline[6]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "5" and i[7] == "":
                                i[7] = 0
                                bonussum = -3 * 5
                                calclist[7] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[7]+ResetAll+emptyscoretable[7]+Tabel+pipeline[7]+ResetAll+Goed+forr10(i[7])+ResetAll+Tabel+pipeline[7]+ResetAll+forl41(calclist[7])+Tabel+pipeline[7]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "6" and i[8] == "":
                                i[8] = 0
                                bonussum = -3 * 6
                                calclist[8] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[8]+ResetAll+emptyscoretable[8]+Tabel+pipeline[8]+ResetAll+Goed+forr10(i[8])+ResetAll+Tabel+pipeline[8]+ResetAll+forl41(calclist[8])+Tabel+pipeline[8]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif (score.upper()[1:] in ["FV","50","YAY","OK","YES"] or score.upper()[1:] in jalijst) and i[19] == "":
                                i[19] = 0
                                calclist[19] = "bummer"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["LS","40"] and i[18] == "":
                                i[18] = 0
                                calclist[18] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[18]+ResetAll+emptyscoretable[18]+Tabel+pipeline[18]+ResetAll+Goed+forr10(i[18])+ResetAll+Tabel+pipeline[18]+ResetAll+forl41(calclist[18])+Tabel+pipeline[18]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["SS","30"] and i[17] == "":
                                i[17] = 0
                                calclist[17] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[17]+ResetAll+emptyscoretable[17]+Tabel+pipeline[17]+ResetAll+Goed+forr10(i[17])+ResetAll+Tabel+pipeline[17]+ResetAll+forl41(calclist[17])+Tabel+pipeline[17]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["FH","25"] and i[16] == "":
                                i[16] = 0
                                calclist[16] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[16]+ResetAll+emptyscoretable[16]+Tabel+pipeline[16]+ResetAll+Goed+forr10(i[16])+ResetAll+Tabel+pipeline[16]+ResetAll+forl41(calclist[16])+Tabel+pipeline[16]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["FK"] and i[15] == "":
                                i[15] = 0
                                calclist[15] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[15]+ResetAll+emptyscoretable[15]+Tabel+pipeline[15]+ResetAll+Goed+forr10(i[15])+ResetAll+Tabel+pipeline[15]+ResetAll+forl41(calclist[15])+Tabel+pipeline[15]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["TK"] and i[14] == "":
                                i[14] = 0
                                calclist[14] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[14]+ResetAll+emptyscoretable[14]+Tabel+pipeline[14]+ResetAll+Goed+forr10(i[14])+ResetAll+Tabel+pipeline[14]+ResetAll+forl41(calclist[14])+Tabel+pipeline[14]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["FC"] and i[20] == "": # Stupid, but hey
                                i[20] = 0
                                calclist[20] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[20]+ResetAll+emptyscoretable[20]+Tabel+pipeline[20]+ResetAll+Goed+forr10(i[20])+ResetAll+Tabel+pipeline[20]+ResetAll+forl41(calclist[20])+Tabel+pipeline[20]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            else:
                                pass
                    else:
                        try:
                            scoreval = eval(score[:score.index("@")])
                            if score[score.index("@")+1:] == "1" and scoreval % 1 == 0 and scoreval <= 5*1 and i[3] == "":
                                i[3] = scoreval
                                if i[3] < 3 * 1:
                                    bonussum = (3 * 1 -i[3]) * -1
                                    calclist[3] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                elif i[3] == 3 * 1:
                                    calclist[3] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                                else:
                                    bonussum = i[3] -3 * 1
                                    calclist[3] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[3]+ResetAll+emptyscoretable[3]+Tabel+pipeline[3]+ResetAll+Goed+forr10(i[3])+ResetAll+Tabel+pipeline[3]+ResetAll+forl41(calclist[3])+Tabel+pipeline[3]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "2" and scoreval % 2 == 0 and scoreval <= 5*2 and i[4] == "":
                                i[4] = scoreval
                                if i[4] < 3 * 2:
                                    bonussum = (3 * 2 -i[4]) * -1
                                    calclist[4] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                elif i[4] == 3 * 2:
                                    calclist[4] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                                else:
                                    bonussum = i[4] -3 * 2
                                    calclist[4] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[4]+ResetAll+emptyscoretable[4]+Tabel+pipeline[4]+ResetAll+Goed+forr10(i[4])+ResetAll+Tabel+pipeline[4]+ResetAll+forl41(calclist[4])+Tabel+pipeline[4]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "3" and scoreval % 3 == 0 and scoreval <= 5*3 and i[5] == "":
                                i[5] = scoreval
                                if i[5] < 3 * 3:
                                    bonussum = (3 * 3 -i[5]) * -1
                                    calclist[5] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                elif i[5] == 3 * 3:
                                    calclist[5] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                                else:
                                    bonussum = i[5] -3 * 3
                                    calclist[5] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[5]+ResetAll+emptyscoretable[5]+Tabel+pipeline[5]+ResetAll+Goed+forr10(i[5])+ResetAll+Tabel+pipeline[5]+ResetAll+forl41(calclist[5])+Tabel+pipeline[5]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "4" and scoreval % 4 == 0 and scoreval <= 5*4 and i[6] == "":
                                i[6] = scoreval
                                if i[6] < 3 * 4:
                                    bonussum = (3 * 4 -i[6]) * -1
                                    calclist[6] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                elif i[6] == 3 * 4:
                                    calclist[6] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                                else:
                                    bonussum = i[6] -3 * 4
                                    calclist[6] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[6]+ResetAll+emptyscoretable[6]+Tabel+pipeline[6]+ResetAll+Goed+forr10(i[6])+ResetAll+Tabel+pipeline[6]+ResetAll+forl41(calclist[6])+Tabel+pipeline[6]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "5" and scoreval % 5 == 0 and scoreval <= 5*5 and i[7] == "":
                                i[7] = scoreval
                                if i[7] < 3 * 5:
                                    bonussum = (3 * 5 -i[7]) * -1
                                    calclist[7] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                elif i[7] == 3 * 5:
                                    calclist[7] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                                else:
                                    bonussum = i[7] -3 * 5
                                    calclist[7] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[7]+ResetAll+emptyscoretable[7]+Tabel+pipeline[7]+ResetAll+Goed+forr10(i[7])+ResetAll+Tabel+pipeline[7]+ResetAll+forl41(calclist[7])+Tabel+pipeline[7]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "6" and scoreval % 6 == 0 and scoreval <= 5*6 and i[8] == "":
                                i[8] = scoreval
                                if i[8] < 3 * 6:
                                    bonussum = (3 * 6 -i[8]) * -1
                                    calclist[8] = Slecht+forr3(bonussum)+ResetAll+" below BONUS target"+19*" "
                                elif i[8] == 3 * 6:
                                    calclist[8] = Wit+"  ="+ResetAll+" on BONUS target"+22*" "
                                else:
                                    bonussum = i[8] -3 * 6
                                    calclist[8] = Goed+forr3(bonussum)+ResetAll+" over BONUS target"+20*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[8]+ResetAll+emptyscoretable[8]+Tabel+pipeline[8]+ResetAll+Goed+forr10(i[8])+ResetAll+Tabel+pipeline[8]+ResetAll+forl41(calclist[8])+Tabel+pipeline[8]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() == "TK" and 5*1 <= scoreval <= 5*6 and i[14] == "":
                                i[14] = scoreval
                                calclist[14] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[14]+ResetAll+emptyscoretable[14]+Tabel+pipeline[14]+ResetAll+Goed+forr10(i[14])+ResetAll+Tabel+pipeline[14]+ResetAll+forl41(calclist[14])+Tabel+pipeline[14]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() == "FK" and 5*1 <= scoreval <= 5*6 and i[15] == "":
                                i[15] = scoreval
                                calclist[15] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[15]+ResetAll+emptyscoretable[15]+Tabel+pipeline[15]+ResetAll+Goed+forr10(i[15])+ResetAll+Tabel+pipeline[15]+ResetAll+forl41(calclist[15])+Tabel+pipeline[15]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() == "FC" and 5*1 <= scoreval <= 5*6 and i[20] == "":
                                i[20] = scoreval
                                calclist[20] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[20]+ResetAll+emptyscoretable[20]+Tabel+pipeline[20]+ResetAll+Goed+forr10(i[20])+ResetAll+Tabel+pipeline[20]+ResetAll+forl41(calclist[20])+Tabel+pipeline[20]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["FH","25"] and i[16] == "":
                                i[16] = 25
                                calclist[16] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[16]+ResetAll+emptyscoretable[16]+Tabel+pipeline[16]+ResetAll+Goed+forr10(i[16])+ResetAll+Tabel+pipeline[16]+ResetAll+forl41(calclist[16])+Tabel+pipeline[16]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["SS","30"] and i[17] == "":
                                i[17] = 30
                                calclist[17] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[17]+ResetAll+emptyscoretable[17]+Tabel+pipeline[17]+ResetAll+Goed+forr10(i[17])+ResetAll+Tabel+pipeline[17]+ResetAll+forl41(calclist[17])+Tabel+pipeline[17]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["LS","40"] and i[18] == "":
                                i[18] = 40
                                calclist[18] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[18]+ResetAll+emptyscoretable[18]+Tabel+pipeline[18]+ResetAll+Goed+forr10(i[18])+ResetAll+Tabel+pipeline[18]+ResetAll+forl41(calclist[18])+Tabel+pipeline[18]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["FV","50","YAY","OK","YES"] and i[19] == "":
                                i[19] = 50
                                calclist[19] = "completed"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" played:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            else:
                                pass
                        except(Exception) as error:
                            #print(error)
                            pass
                else:
                    if not "@" in score:
                        if (score.upper() in ["FV","50","OK","JA","YES"] or score.upper() in jalijst) and i[19] == "":
                            i[19] = 50
                            calclist[19] = "klaar"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["SHIT","FUCK","KUT","NEE"] or score.upper() in neelijst) and i[19] == "":
                            i[19] = 0
                            calclist[19] = "jammer"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["GS","40"]) and i[18] == "":
                            i[18] = 40
                            calclist[18] = "klaar"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[18]+ResetAll+emptyscoretable[18]+Tabel+pipeline[18]+ResetAll+Goed+forr10(i[18])+ResetAll+Tabel+pipeline[18]+ResetAll+forl41(calclist[18])+Tabel+pipeline[18]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["KS","30"]) and i[17] == "":
                            i[17] = 30
                            calclist[17] = "klaar"
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[17]+ResetAll+emptyscoretable[17]+Tabel+pipeline[17]+ResetAll+Goed+forr10(i[17])+ResetAll+Tabel+pipeline[17]+ResetAll+forl41(calclist[17])+Tabel+pipeline[17]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif (score.upper() in ["VH","25"]) and i[16] == "":
                            i[16] = 25
                            calclist[16] = ""
                            print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            print(Tabel+pipeline[16]+ResetAll+emptyscoretable[16]+Tabel+pipeline[16]+ResetAll+Goed+forr10(i[16])+ResetAll+Tabel+pipeline[16]+ResetAll+forl41(calclist[16])+Tabel+pipeline[16]+ResetAll)
                            print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                            chk = "Y"
                        elif len(score) > 1 and score[0] == "/":
                            if score[1:] == "1" and i[3] == "":
                                i[3] = 0
                                bonussum = -3 * 1
                                calclist[3] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[3]+ResetAll+emptyscoretable[3]+Tabel+pipeline[3]+ResetAll+Goed+forr10(i[3])+ResetAll+Tabel+pipeline[3]+ResetAll+forl41(calclist[3])+Tabel+pipeline[3]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "2" and i[4] == "":
                                i[4] = 0
                                bonussum = -3 * 2
                                calclist[4] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[4]+ResetAll+emptyscoretable[4]+Tabel+pipeline[4]+ResetAll+Goed+forr10(i[4])+ResetAll+Tabel+pipeline[4]+ResetAll+forl41(calclist[4])+Tabel+pipeline[4]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "3" and i[5] == "":
                                i[5] = 0
                                bonussum = -3 * 3
                                calclist[5] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[5]+ResetAll+emptyscoretable[5]+Tabel+pipeline[5]+ResetAll+Goed+forr10(i[5])+ResetAll+Tabel+pipeline[5]+ResetAll+forl41(calclist[5])+Tabel+pipeline[5]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "4" and i[6] == "":
                                i[6] = 0
                                bonussum = -3 * 4
                                calclist[6] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[6]+ResetAll+emptyscoretable[6]+Tabel+pipeline[6]+ResetAll+Goed+forr10(i[6])+ResetAll+Tabel+pipeline[6]+ResetAll+forl41(calclist[6])+Tabel+pipeline[6]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "5" and i[7] == "":
                                i[7] = 0
                                bonussum = -3 * 5
                                calclist[7] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[7]+ResetAll+emptyscoretable[7]+Tabel+pipeline[7]+ResetAll+Goed+forr10(i[7])+ResetAll+Tabel+pipeline[7]+ResetAll+forl41(calclist[7])+Tabel+pipeline[7]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[1:] == "6" and i[8] == "":
                                i[8] = 0
                                bonussum = -3 * 6
                                calclist[8] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[8]+ResetAll+emptyscoretable[8]+Tabel+pipeline[8]+ResetAll+Goed+forr10(i[8])+ResetAll+Tabel+pipeline[8]+ResetAll+forl41(calclist[8])+Tabel+pipeline[8]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif (score.upper()[1:] in ["FV","50","OK","JA","YES"] or score.upper()[1:] in jalijst) and i[19] == "":
                                i[19] = 0
                                calclist[19] = "jammer"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["GS","40"] and i[18] == "":
                                i[18] = 0
                                calclist[18] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[18]+ResetAll+emptyscoretable[18]+Tabel+pipeline[18]+ResetAll+Goed+forr10(i[18])+ResetAll+Tabel+pipeline[18]+ResetAll+forl41(calclist[18])+Tabel+pipeline[18]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["KS","30"] and i[17] == "":
                                i[17] = 0
                                calclist[17] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[17]+ResetAll+emptyscoretable[17]+Tabel+pipeline[17]+ResetAll+Goed+forr10(i[17])+ResetAll+Tabel+pipeline[17]+ResetAll+forl41(calclist[17])+Tabel+pipeline[17]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["VH","25"] and i[16] == "":
                                i[16] = 0
                                calclist[16] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[16]+ResetAll+emptyscoretable[16]+Tabel+pipeline[16]+ResetAll+Goed+forr10(i[16])+ResetAll+Tabel+pipeline[16]+ResetAll+forl41(calclist[16])+Tabel+pipeline[16]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["VD"] and i[15] == "":
                                i[15] = 0
                                calclist[15] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[15]+ResetAll+emptyscoretable[15]+Tabel+pipeline[15]+ResetAll+Goed+forr10(i[15])+ResetAll+Tabel+pipeline[15]+ResetAll+forl41(calclist[15])+Tabel+pipeline[15]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["DD"] and i[14] == "":
                                i[14] = 0
                                calclist[14] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[14]+ResetAll+emptyscoretable[14]+Tabel+pipeline[14]+ResetAll+Goed+forr10(i[14])+ResetAll+Tabel+pipeline[14]+ResetAll+forl41(calclist[14])+Tabel+pipeline[14]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score.upper()[1:] in ["VK"] and i[20] == "": # Stupid, but hey
                                i[20] = 0
                                calclist[20] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" klaar:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[20]+ResetAll+emptyscoretable[20]+Tabel+pipeline[20]+ResetAll+Goed+forr10(i[20])+ResetAll+Tabel+pipeline[20]+ResetAll+forl41(calclist[20])+Tabel+pipeline[20]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            else:
                                pass
                    else:
                        try:
                            scoreval = eval(score[:score.index("@")])
                            if score[score.index("@")+1:] == "1" and scoreval % 1 == 0 and scoreval <= 5*1 and i[3] == "":
                                i[3] = scoreval
                                if i[3] < 3 * 1:
                                    bonussum = (3 * 1 -i[3]) * -1
                                    calclist[3] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                elif i[3] == 3 * 1:
                                    calclist[3] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
                                else:
                                    bonussum = i[3] -3 * 1
                                    calclist[3] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[3]+ResetAll+emptyscoretable[3]+Tabel+pipeline[3]+ResetAll+Goed+forr10(i[3])+ResetAll+Tabel+pipeline[3]+ResetAll+forl41(calclist[3])+Tabel+pipeline[3]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "2" and scoreval % 2 == 0 and scoreval <= 5*2 and i[4] == "":
                                i[4] = scoreval
                                if i[4] < 3 * 2:
                                    bonussum = (3 * 2 -i[4]) * -1
                                    calclist[4] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                elif i[4] == 3 * 2:
                                    calclist[4] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
                                else:
                                    bonussum = i[4] -3 * 2
                                    calclist[4] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[4]+ResetAll+emptyscoretable[4]+Tabel+pipeline[4]+ResetAll+Goed+forr10(i[4])+ResetAll+Tabel+pipeline[4]+ResetAll+forl41(calclist[4])+Tabel+pipeline[4]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "3" and scoreval % 3 == 0 and scoreval <= 5*3 and i[5] == "":
                                i[5] = scoreval
                                if i[5] < 3 * 3:
                                    bonussum = (3 * 3 -i[5]) * -1
                                    calclist[5] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                elif i[5] == 3 * 3:
                                    calclist[5] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
                                else:
                                    bonussum = i[5] -3 * 3
                                    calclist[5] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[5]+ResetAll+emptyscoretable[5]+Tabel+pipeline[5]+ResetAll+Goed+forr10(i[5])+ResetAll+Tabel+pipeline[5]+ResetAll+forl41(calclist[5])+Tabel+pipeline[5]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "4" and scoreval % 4 == 0 and scoreval <= 5*4 and i[6] == "":
                                i[6] = scoreval
                                if i[6] < 3 * 4:
                                    bonussum = (3 * 4 -i[6]) * -1
                                    calclist[6] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                elif i[6] == 3 * 4:
                                    calclist[6] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
                                else:
                                    bonussum = i[6] -3 * 4
                                    calclist[6] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[6]+ResetAll+emptyscoretable[6]+Tabel+pipeline[6]+ResetAll+Goed+forr10(i[6])+ResetAll+Tabel+pipeline[6]+ResetAll+forl41(calclist[6])+Tabel+pipeline[6]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "5" and scoreval % 5 == 0 and scoreval <= 5*5 and i[7] == "":
                                i[7] = scoreval
                                if i[7] < 3 * 5:
                                    bonussum = (3 * 5 -i[7]) * -1
                                    calclist[7] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                elif i[7] == 3 * 5:
                                    calclist[7] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
                                else:
                                    bonussum = i[7] -3 * 5
                                    calclist[7] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[7]+ResetAll+emptyscoretable[7]+Tabel+pipeline[7]+ResetAll+Goed+forr10(i[7])+ResetAll+Tabel+pipeline[7]+ResetAll+forl41(calclist[7])+Tabel+pipeline[7]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:] == "6" and scoreval % 6 == 0 and scoreval <= 5*6 and i[8] == "":
                                i[8] = scoreval
                                if i[8] < 3 * 6:
                                    bonussum = (3 * 6 -i[8]) * -1
                                    calclist[8] = Slecht+forr3(bonussum)+ResetAll+" onder BONUS target"+19*" "
                                elif i[8] == 3 * 6:
                                    calclist[8] = Wit+"  ="+ResetAll+" op BONUS target"+22*" "
                                else:
                                    bonussum = i[8] -3 * 6
                                    calclist[8] = Goed+forr3(bonussum)+ResetAll+" boven BONUS target"+19*" "
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[8]+ResetAll+emptyscoretable[8]+Tabel+pipeline[8]+ResetAll+Goed+forr10(i[8])+ResetAll+Tabel+pipeline[8]+ResetAll+forl41(calclist[8])+Tabel+pipeline[8]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() == "DD" and 5*1 <= scoreval <= 5*6 and i[14] == "":
                                i[14] = scoreval
                                calclist[14] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[14]+ResetAll+emptyscoretable[14]+Tabel+pipeline[14]+ResetAll+Goed+forr10(i[14])+ResetAll+Tabel+pipeline[14]+ResetAll+forl41(calclist[14])+Tabel+pipeline[14]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() == "VD" and 5*1 <= scoreval <= 5*6 and i[15] == "":
                                i[15] = scoreval
                                calclist[15] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[15]+ResetAll+emptyscoretable[15]+Tabel+pipeline[15]+ResetAll+Goed+forr10(i[15])+ResetAll+Tabel+pipeline[15]+ResetAll+forl41(calclist[15])+Tabel+pipeline[15]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() == "VK" and 5*1 <= scoreval <= 5*6 and i[20] == "":
                                i[20] = scoreval
                                calclist[20] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[20]+ResetAll+emptyscoretable[20]+Tabel+pipeline[20]+ResetAll+Goed+forr10(i[20])+ResetAll+Tabel+pipeline[20]+ResetAll+forl41(calclist[20])+Tabel+pipeline[20]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["VH","25"] and i[16] == "":
                                i[16] = 25
                                calclist[16] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[16]+ResetAll+emptyscoretable[16]+Tabel+pipeline[16]+ResetAll+Goed+forr10(i[16])+ResetAll+Tabel+pipeline[16]+ResetAll+forl41(calclist[16])+Tabel+pipeline[16]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["KS","30"] and i[17] == "":
                                i[17] = 30
                                calclist[17] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[17]+ResetAll+emptyscoretable[17]+Tabel+pipeline[17]+ResetAll+Goed+forr10(i[17])+ResetAll+Tabel+pipeline[17]+ResetAll+forl41(calclist[17])+Tabel+pipeline[17]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["GS","40"] and i[18] == "":
                                i[18] = 40
                                calclist[18] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[18]+ResetAll+emptyscoretable[18]+Tabel+pipeline[18]+ResetAll+Goed+forr10(i[18])+ResetAll+Tabel+pipeline[18]+ResetAll+forl41(calclist[18])+Tabel+pipeline[18]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            elif score[score.index("@")+1:].upper() in ["FV","50","OK","JA","YES"] and i[19] == "":
                                i[19] = 50
                                calclist[19] = "klaar"
                                print(Bevestiging+forc15(i[1].strip()+ResetAll+" speelde:"))
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                print(Tabel+pipeline[19]+ResetAll+emptyscoretable[19]+Tabel+pipeline[19]+ResetAll+Goed+forr10(i[19])+ResetAll+Tabel+pipeline[19]+ResetAll+forl41(calclist[19])+Tabel+pipeline[19]+ResetAll)
                                print(Tabel+pipeline[0]+ResetAll+emptyscoretable[2]+Tabel+pipeline[0]+ResetAll+forr10(i[2])+Tabel+pipeline[0]+ResetAll+forl41(calclist[2])+Tabel+pipeline[0]+ResetAll)
                                chk = "Y"
                            else:
                                pass
                        except(Exception) as error:
                            #print(error)
                            pass
                if chk == "Y":
                    subup = 0
                    for j in i[3:9]:
                        if j != "":
                            subup += j
                    i[10] = subup
                    sumup = subup + i[11]
                    i[12] = sumup
                    sumlow = 0
                    for j in i[14:21]:
                        if j != "":
                            sumlow += j
                    i[22] = sumlow
                    i[23] = sumup
                    i[24] = sumup + sumlow
                    calclist = calcstuff()
                    writeifvalid = "N"
                    checkinput = "N"
                    break
    if playround == 13:
        print()
        print("+"+68*"-"+"+")
        print()
        showall()
        players = []
        scores = []
        for i in playertableslist:
            players.append(i[1])
            scores.append(i[24])
            topscore = max(scores)
        if len(players) > 1:
            counttops = 0
            for i in scores:
                if i == topscore:
                    counttops += 1
            if counttops == 1:
                topplayer = players[scores.index(topscore)]
                if taal == "EN":
                    print("%s wins @ %s points" % (Goed+topplayer.strip()+ResetAll,Goed+str(topscore)+ResetAll))
                else:
                    print("%s wint @ %s punten" % (Goed+topplayer.strip()+ResetAll,Goed+str(topscore)+ResetAll))
            elif counttops == len(playertableslist) and playround != 1:
                if taal == "EN":
                    print("Draw @ %s points" % (SubGoed+str(topscore)+ResetAll))
                else:
                    print("Gelijkspel @ %s punten" % (SubGoed+str(topscore)+ResetAll))
            elif counttops != len(playertableslist) and playround != 1:
                if taal == "EN":
                    print("The players @ %s won" % (SubGoed+str(topscore)+ResetAll))
                else:
                    print("De spelers @ %s hebben gewonnen" % (SubGoed+str(topscore)+ResetAll))
        else:
            topplayer = players[0]
            if taal == "EN":
                print("%s's score is %s points" % (Goed+topplayer.strip()+ResetAll,Goed+str(topscore)+ResetAll))
            else:
                print("%s's score is %s punten" % (Goed+topplayer.strip()+ResetAll,Goed+str(topscore)+ResetAll))
        print()
        print("+"+68*"-"+"+")
        print()
