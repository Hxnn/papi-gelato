#  Paar variables die ik later nodig heb ↓
print('Welkom bij Papi Gelato u mag kiezen uit 4 smaken!')
Sorry = 'Sorry dat is geen optie die we aanbieden...'
HorP = 'Hoorntjes    1 x € 1.25    = € 1.25  '
BakP = 'Bakjes       1 x € 0.75    = € 0.75  '
x = '                          -------- +'


#  Bonnentje definen en wat het moet doen ↓
def bon():
    sprP = Bol * 0.30
    BolP = Bol * 0.95
    print('----------[Papi Gelato]----------')
    print('Bolletjes   ', Bol, 'x € 0.95    = €', BolP)
    if Topping == 'Geen' and HoBa == 'hoorntje':
        print(HorP)
        print(x)
        print('Totaal                    = €', BolP + 1.25)
    if Topping == 'Geen' and HoBa == 'bakje':
        print(BakP)
        print(x)
        print('Totaal                    = €', BolP + 0.75)
    if Topping == 'Slagroom' and HoBa == 'bakje':
        print(BakP)
        print('Topping      1 x € 0.50    = € 0.50  ')
        print(x)
        print('Totaal                     = €', BolP + 0.50 + 0.75)
    elif Topping == 'Slagroom' and HoBa == 'hoorntje':
        print(HorP)
        print('Topping      1 x € 0.50    = € 0.50  ')
        print(x)
        print('Totaal                     = €', BolP + 0.50 + 1.25)
    if Topping == 'Sprinkels' and HoBa == 'hoorntje':
        print(HorP)
        print('Topping      1 x €', sprP, '    = €', sprP)
        print(x)
        print("Totaal                     = €", BolP + sprP + 1.25)
    elif Topping == 'Sprinkels' and HoBa == 'bakje':
        print(BakP)
        print("Topping      1 x €", sprP, '    = €', sprP)
        print(x)
        print('Totaal                     = €', BolP + sprP + 0.75)
    if Topping == 'Caramel' and HoBa == 'hoorntje':
        print(HorP)
        print('Topping      1 x € 0.60  = € 0.60')
        print(x)
        print('Totaal                    = €', (BolP + 0.60 + 1.25))
    elif Topping == 'Caramel' and HoBa == 'bakje':
        print(BakP)
        print('Topping      1 x € 0.90    = € 0.90')
        print(x)
        print('Totaal                     = €', (BolP + 0.90 + 0.75))


# De zakelijke bon maken, want hier kan je geen bakjes kiezen etc ↓.
def bonZ():
    LP = liter * 9.80
    Quotient = LP / 100
    Procent = Quotient * 6

    print('----------[Papi Gelato]----------')
    print('Liter     ', liter, ' x € 9.80    = €', round(LP, 3))
    print(x)
    print('Totaal                    = €', round(LP))
    print('BTW (6%)                  = €', round(Procent))


# Begin maken, als de gebruiker particulier of zakelijk wilt kopen ↓.
def start():
    markt = int(input('Bent u 1) particulier of 2) zakelijk? '))
    if markt == 1:
        stap1()
    elif markt == 2:
        zakelijk1()
    else:
        print(Sorry)
        return start()


# Zakelijke keuze ↓.
def zakelijk1():
    global liter
    liter = int(input('Hoeveel liter ijs wilt u? '))
    if liter > 1:
        zakelijk2()
    else:
        print(Sorry)
        return zakelijk1()


# Zakelijke keuze 2e gedeelte, vragen voor smaak ↓.
def zakelijk2():
    global smaakL
    for i in range(liter, 0, -1):
        smaakL = input('Welke smaak wilt u voor uw liters ijs? A) Aardbei, C) Chocolade of V) Vanille ')
        if smaakL == "A" or smaakL == "C" or smaakL == "V":
            stap4()
        else:
            print(Sorry)
            return zakelijk2()


# Particulier versie, vragen hoeveel bolletjes de gebruiker wilt ↓.
def stap1():
    global Bol
    Bol = int(input('Hoeveel bolletjes wilt u? '))
    if Bol in range(1, 4):
        smaakKeuze()
    elif Bol in range(4, 8):
        print('Dan krijgt u van mij een bakje met ', Bol, ' bolletjes. ')
        smaakKeuze()
    elif Bol > 8:
        print("Sorry, zulke grote bakken hebben we niet")
        return stap1()
    else:
        print(Sorry)
        return stap1()


# Particuliere smaakkeuze ↓.
def smaakKeuze():
    global smaak
    for o in range(Bol, 0, -1):
        smaak = input(
            ('Welke smaak wilt u voor bolletje nummer', o, '? A) Aardbei, C) Chocolade of V) Vanille '))
    if smaak == "A" or smaak == "C" or smaak == "M" or smaak == "V":
        stap2()
    else:
        print(Sorry)
        return smaakKeuze()


# Vragen voor een hoorntje of bakje als het minder adn 3 is ↓.
def stap2():
    global HoBa
    HoBa = input(('Wilt u deze', Bol, 'bolletje(s) in A) een hoorntje of B) een bakje? '))
    if HoBa == "A":
        HoBa = "hoorntje"
        toppings()
    elif HoBa == "B":
        HoBa = "bakje"
        toppings()
    else:
        print(Sorry)
        return stap2()


# Vragen voor de toppings ↓.
def toppings():
    global Topping
    Topping = input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ')
    if Topping == "A":
        Topping = "Geen"
        stap3()
    elif Topping == "B":
        Topping = "Slagroom"
        stap3()
    elif Topping == "C":
        Topping = "Sprinkels"
        stap3()
    elif Topping == "D":
        Topping = "Caramel"
        stap3()
    else:
        print(Sorry)


# Zeggen hoeveel bolletjes ze hebben etc. En vragen als ze nog meer willen bestellen ↓.
def stap3():
    nogmaals = input(('Hier is uw', HoBa, "met", Bol, 'bolletje(s). Wilt u nog meer bestellen? Y/N '))
    if nogmaals == "Y":
        stap1()
    elif nogmaals == "N":
        bon()
        print("Bedankt en tot ziens!")
        quit()
    else:
        print(Sorry)


# Voor de zakelijke stap, vragen als ze nog meer willen bestellen ↓.
def stap4():
    nogmaals = input(('Hier is uw, ' + str(liter) + ' liter ijs. Wilt u nog meer bestellen? Y/N '))
    if nogmaals == "Y":
        stap1()
    elif nogmaals == "N":
        bonZ()
        print("Bedankt en tot ziens!")
        quit()
    else:
        print(Sorry)


start()
