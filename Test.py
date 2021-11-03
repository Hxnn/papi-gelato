Bol = True
Vraag = True

print("Welkom bij Papi Gelato u mag kiezen uit 4 smaken!")
while Bol:
    Bol = Bol1 = int(input('Hoeveel bolletjes wilt u? '))
    BolP = BolP1 = Bol * 1.10
    HorP = HorP1 = Bol * 1.25
    BakP = BakP1 = 1 * 0.75
    Geen = 0
    if Bol1 <= 3:
        for i in range(Bol1):
            Smaak = str(input('Welke smaak wilt u voor uw bolletje? Kies uit: A) Aardbei, C) Chocolade, M) Munt of V) '
                              'Vanille? '))
            Topping = str(input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?'))
            Topping1 = int("B" and "C" and "D")
            if Topping == "B":
                var = Topping1 + 0.5
            elif Topping == "C":
                var = Topping1 + 0.3
            elif Topping == "D":
                var = Topping1 + 0.6

        while Vraag:
            Vraag = input('Wilt u deze bolletje(s) in A) een hoorntje of B) een bakje? ')
            if Vraag == 'A' or 'a':
                Vraag1 = input(str('Hier is uw hoorntje met ' + str(Bol1) + 'bolletje(s). Wilt u nog meer bestellen? ('
                                                                            'Y/N) '))
                if Vraag1 == 'Y':
                    break
                elif Vraag1 == 'N':
                    print('Bedankt en tot ziens!')
                    Topping1 = int("B" + "C" + "D")
                    Totaal = BolP + HorP + Topping1
                    print('---------[Papi Gelato]---------')
                    print('Bolletje(s)   ', Bol1, 'x €1.10 =', round(BolP, 3))
                    print('Hoorntje(s)   ', Bol1, 'x €1.25 =', round(HorP, 3))
                    print('Bakje(s)      ', 0, 'x €0.75 =', round(BakP, 3))
                    print('Topping(s)      ', round(Topping1, 3))
                    print('----------')
                    print('Totaal', round(Totaal, 3))
                    quit()
            elif Vraag == 'B':
                Vraag1 = input('Hier is uw bakje met ' + str(Bol1) + ' bolletje(s). Wilt u nog meer bestellen? (Y/N) ')
                if Vraag1 == 'Y':
                    break
                elif Vraag1 == 'N':
                    print('Bedankt en tot ziens!')
                    Topping1 = int("B" + "C" + "D")
                    Totaal1 = BolP1 + BakP + Topping1
                    print('---------[Papi Gelato]---------')
                    print('Bolletje(s)   ', Bol1, 'x €1.10 =', round(BolP1, 3))
                    print('Hoorntje(s)   ', Bol, 'x €1.25 =', round(HorP1, 3))
                    print('Bakje(s)      ', 1, 'x €0.75 =', round(BakP, 3))
                    print('----------')
                    print('Totaal', round(Totaal1, 3))
                    quit()
                else:
                    print('Sorry, dat snap ik niet...')
                break
            else:
                print('Sorry, dat snap ik niet...')
    elif int(str(4)) <= Bol <= int(str(8)):
        for i in range(int(Bol)):
            Smaak = str(input(
                'Welke smaak wilt u voor uw bolletje? Kies uit: A) Aardbei, C) Chocolade, M) Munt of V) Vanille? '))
        while Vraag:
            Vraag1 = input(
                'Dan krijgt u van mij een bakje met ' + str(Bol) + ' bolletjes. Wilt u nog meer bestellen? (Y/N) ')
            if Vraag1 == 'Y':
                break
            elif Vraag1 == 'N':
                print('Bedankt en tot ziens!')
                Topping1 = int("B" + "C" + "D")
                Totaal1 = BolP1 + BakP + Topping1
                print('---------[Papi Gelato]---------')
                print('Bolletje(s)   ', Bol, 'x €1.10 =', round(BolP1, 3))
                print('Hoorntje(s)   ', Bol, 'x €1.25 =', round(HorP1, 3))
                print('Bakje(s)      ', 1, 'x €0.75 =', round(BakP, 3))
                print('----------')
                print('Totaal', round(Totaal1, 3))
                quit()
            else:
                print('Sorry, dat snap ik niet...')
            break
    elif Bol > int(str(8)):
        print('Sorry, zulke grote bakken hebben we niet.')
    else:
        print('Sorry, dat snap ik niet...')
