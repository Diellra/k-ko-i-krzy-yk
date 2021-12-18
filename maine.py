# Tu będzie gra kółko i krzyżyk

PlanszaDoGry = {'7':'','8':'','9':'',
                '4':'','5':'','6':'',
                '1':'','2':'','3':''}

KlawiszeGry = []

for key in PlanszaDoGry:
    KlawiszeGry.append(key)

def drukujPlansze(pole):
    print('' + '|' + '' + '|' + '')
    print('-+-+-')
    print('' + '|' + '' + '|' + '')
    print('-+-+-')
    print('' + '|' + '' + '|' + '')

drukujPlansze('pole')

def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")

drukujPlansze(PlanszaDoGry)

def gra():

    gracz='x'
    licznik=0
    for i in range(10): 
        drukujPlansze(PlanszaDoGry)
       
        
        move=input(f'To jest ruch, {gracz}. Wybierz gdzie chcesz ustawić znak!')

        if PlanszaDoGry[move]=='':
            PlanszaDoGry[move]=gracz
            licznik+=1
        else:
            print("Miejsce jest juz zajęte!!!\nWstaw swój znak gdzieś indziej")
            continue

        if licznik>=5:
            if PlanszaDoGry['7']==PlanszaDoGry['8']==PlanszaDoGry['9']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')
            elif PlanszaDoGry['4']==PlanszaDoGry['5']==PlanszaDoGry['6']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')

            elif PlanszaDoGry['1']==PlanszaDoGry['2']==PlanszaDoGry['3']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')
#tutaj koncza sie wygrane poziomy

            elif PlanszaDoGry['1']==PlanszaDoGry['4']==PlanszaDoGry['7']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')

            elif PlanszaDoGry['2']==PlanszaDoGry['5']==PlanszaDoGry['8']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')

            elif PlanszaDoGry['3']==PlanszaDoGry['6']==PlanszaDoGry['9']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')

            elif PlanszaDoGry['1']==PlanszaDoGry['5']==PlanszaDoGry['9']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')

            elif PlanszaDoGry['7']==PlanszaDoGry['5']==PlanszaDoGry['3']!= '':
                drukujPlansze(PlanszaDoGry)
                print('n\KoniecGry!\n')
                print(f'WYGRAŁ GRACZ:{gracz}')

            if licznik==9:
                print('\nKONIEC GRY!\n')
                print('\JEST REMIS!\n')

        if gracz=='x':
            gracz='0'
        else:
            gracz='x'

    restart=input('CZY CHCESZ ZAGRAĆ PONOWNIE/9t/n')
    if restart=='t' or restart=='T':
        for key in KlawiszeGry:
            PlanszaDoGry[key]=''





