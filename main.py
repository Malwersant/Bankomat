import time

print('Dzień dobry. Włóż kartę do bankomatu.')
pin1 = input('Podaj nr PIN: ')
balance = 5000.11
i = 0
while pin1 != '6666' and i < 3:
    i += 1
    if i == 3:
        print(f'Wprowadzono {i} razy błędnie nr PIN. Karta została zablokowana.\nUdaj się do oddziału w celu odblokowania karty')
        break
    print('Podałeś nieprawidłowy PIN. Spróbuj jeszcze raz!')
    pin1 = input('Podaj nr PIN: ')

else:
    print('PIN jest poprawny.')
    time.sleep(1.0)


    def print_operations():
        operations = {1: 'sprawdzanie salda rachunku', 2: 'wypłata gotówki', 3: 'wpłata gótówki',
                      4: 'zmiana numeru PIN',
                      5: 'złożenie wniosku kredytowego', 6: 'doładowanie telefonu', 0: 'kończymy na dziś'}
        print('Dostępne operacje:')
        for key, value in operations.items():
            print('{}: {}'.format(key, value))


    cash_withdrawals = {1: 50, 2: 100, 3: 200, 4: 500}


    def print_values(pairs):
        for key, value in pairs.items():
            print(f'{key} - {value} złotych.')


    def checking_and_changing_the_balance(user_choice, operation_num, amount):
        if user_choice == 2:
            if amount < cash_withdrawals[operation_num]:
                print(
                    f'Nie masz wystarczających środków, żeby zrealizować tę operację.\nMasz na koncie {amount} złotych, a próbujesz wybrać {cash_withdrawals[operation_num]} złotych.')
            else:
                amount -= cash_withdrawals[operation_num]
        elif user_choice == 3:
            amount += cash_withdrawals[operation_num]
        return round(amount, 2)


    print_operations()

    choice1 = int(input('Którą operację wybierasz: 1,2,3,4,5,6 czy 0?: '))  # obsłużyć przypadek z wprowadzeniem wartości poza przedziałem 0-6 (ma się wyświetlać komunikat, że wybrano nieprawidłowa wartość) oraz 0 (ma się wyświetlać komunikat kończymy na dziś)

    while choice1 != 0:
        if choice1 == 1:
            print(f'Stan dostępnych środków na twoim koncie wynosi\n{balance} złotych.')
            time.sleep(1.0)
            print_operations()
            choice1 = int(input('Którą operację wybierasz: 1,2,3,4,5,6 czy 0?: '))

        elif choice1 == 2:
            if balance < min(val for val in cash_withdrawals.values()):  # Tu chodzi o to, że jeśli np. kiedyś będzie można pobierać z bankomatu 10 zł, to wtedy tylko zaktualizuję słownik cash_withdrawals, a program wybierze najniższą kwotę do wypłaty, z która ma porównac stan salda
                print('Nie masz wystarczajacej ilości gotówki, żeby zrealizować tę operację.')
            else:
                print('Dostępne możliwości wypłaty gotówki:')
                print_values(cash_withdrawals)
                choice2 = int(input('Którą kwotę wybierasz: 1, 2, 3, czy 4?: '))

            balance = (checking_and_changing_the_balance(choice1, choice2, balance))
            print_operations()
            choice1 = int(input('Którą operację wybierasz: 1,2,3,4,5,6 czy 0?: '))

        elif choice1 == 3:
            print('Dostępne możliwości wpłaty gotówki:')
            print_values(cash_withdrawals)
            choice3 = int(input("Która kwotę wybierasz: 1, 2, 3, czy 4?: "))
            balance = (checking_and_changing_the_balance(choice1, choice3, balance))
            print_operations()
            choice1 = int(input('Którą operację wybierasz: 1,2,3,4,5,6 czy 0?: '))

        elif choice1 == 4:
            pin2 = input('Podaj nowy nr PIN: ')
            if pin2 != pin1:
                pin1 = pin2
                print('Twój PIN został zmieniony.')
            else:
                print('Twój nowy PIN jest taki sam jak stary i dlatego nie został zmieniony. Spróbuj ponownie.')

        print_operations()
        choice1 = int(input('Którą operację wybierasz: 1,2,3,4,5,6 czy 0?: '))







    #         elif choice1 == 5:
    #             print(
    #                 "Minimalna kwota pożyczki udzielonej w bankomacie wynosi 200 zł, a maksymalna 2000 zł.  Jeśli chcesz pożyczyć więcej, udaj się do oddziału lub skorzystaj z bankowości elektronicznej. ")
    #             c = float(input("Podaj liczbę z przedziału od 200 zł do 2000 zł: "))
    #             if 200 <= c <= 2000:
    #                 b += round(c, 2)
    #                 print("Dopisano do twojego konta", c, "złotych. Obecnie masz na koncie", b + c,
    #                       "złotych. W celu poznania wysokości oprocentowania kredytu, terminu spłaty oraz ilości rat, udaj się do odziału lub skorzystaj z bankowości elektronicznej.")  # obsłużyć prawidłowe wyświetlanie tego komunikatu
    #             else:
    #                 print(
    #                     "Wybrałeś nieprawidłowa kwotę. Minimalna kwota pożyczki udzielonej w bankomacie wynosci 200 zł, a maksymalna 2000 zł. ")
    #         elif choice1 == 6:
    #             d = input("Podaj numer telefonu, który chcesz doładować: ")
    #             print("Podaj na jaka kwotę chcesz doładować telefon. Dostępne opcje:")
    #             print("1 - 10 złotych")
    #             print("2 - 20 złotych")
    #             print("3 - 50 złotych")
    #             print("4 - 100 złotych")
    #             choice4 = int(input("Która kwotę wybierasz: 1, 2, 3 czy 4? "))
    #             if choice4 == 1:
    #                 b -= 10
    #             elif choice4 == 2:
    #                 b -= 20
    #             elif choice4 == 3:
    #                 b -= 50
    #             elif choice4 == 4:
    #                 b -= 100
    else:
        print('Życzymy miłego dnia i zapraszamy ponownie.')

# # while choice1 in (0, 1, 2, 3, 4, 5, 6):
