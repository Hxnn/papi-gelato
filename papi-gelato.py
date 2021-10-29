Bol = True
Vraag = True
print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is!")
while Bol:
    Bol = str(input('Hoeveel bolletjes wilt u? '))
    if Bol <= str(3):
        while Vraag:
            Vraag = input('Wilt u deze bolletje(s) in A) een hoorntje of B) een bakje? ')
            if Vraag == 'A':
                Vraag1 = input(str('Hier is uw hoorntje met ' + Bol + ' bolletje(s). Wilt u nog meer bestellen? (Y/N) '))
                if Vraag1 == 'Y':
                    break
                else:
                    print('Bedankt en tot ziens!')
                    quit()
            elif Vraag == 'B':
                Vraag1 = input('Hier is uw bakje met ' + Bol + ' bolletje(s). Wilt u nog meer bestellen? (Y/N) ')
                if Vraag1 == 'Y':
                    break
                elif Vraag1 == 'N':
                    print('Bedankt en tot ziens!')
                    quit()
                else:
                    print('Sorry, dat snap ik niet...')
                break
            else:
                print('Sorry, dat snap ik niet...')
    elif str(4) <= Bol <= str(8):
        while Vraag:
            Vraag1 = input('Dan krijgt u van mij een bakje met ' + Bol + ' bolletjes. Wilt u nog meer bestellen? (Y/N) ')
            if Vraag1 == 'Y':
                break
            elif Vraag1 == 'N':
                print('Bedankt en tot ziens!')
                quit()
            else:
                print('Sorry, dat snap ik niet...')
            break
    elif Bol > str(8):
        print('Sorry, zulke grote bakken hebben we niet.')
    else:
        print('Sorry, dat snap ik niet...')
