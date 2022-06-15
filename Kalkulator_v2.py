import logging
from pickletools import float8
import string
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    print("Witaj w kalkulatorze!")
    calculator = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    if calculator == '1':
        print("Wybrałeś dodawanie!")
        num_1 = float(input("Podaj składnik 1: "))
        num_2 = float(input("Podaj składnik 2: "))
        num_3 = float(input("Podaj składnik 3: "))
        logging.info(f"Dodaję {num_1}, {num_2} i {num_3}")
        sum = num_1 + num_2 + num_3
        print(f"Wynik to {sum}")
    elif calculator == '2':
        print("Wybrałeś odejmowanie!")
        num_1 = float(input("Podaj składnik 1: "))
        num_2 = float(input("Podaj składnik 2: "))
        logging.info(f"Odejmuję {num_1} i {num_2}")
        sub = num_1 - num_2
        print(f"Wynik to {sub}")
    elif calculator == '3':
        print("Wybrałeś mnożenie!")
        num_1 = float(input("Podaj składnik 1: "))
        num_2 = float(input("Podaj składnik 2: "))
        num_3 = float(input("Podaj składnik 3: "))
        logging.info(f"Mnożę {num_1}, {num_2} i {num_3}")
        mult = num_1 * num_2 * num_3
        print(f"Wynik to {mult}")
    elif calculator == '4':
        print("Wybrałeś dzielenie!")
        num_1 = float(input("Podaj składnik 1: "))
        num_2 = float(input("Podaj składnik 2: "))
        if num_2 > 0:
            logging.info(f"Dzielę {num_1} i {num_2}")
            div = (num_1 / num_2)
            print(f"Wynik to {div}")
        else:
            print("Błąd! Dzielnie przez 0!")
            exit(1)
    else:
        print("Pod tym numerem nie ma żadnego działania")
        exit(1)        
