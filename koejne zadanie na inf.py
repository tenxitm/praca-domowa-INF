import math

class statyczne_metody:

    @staticmethod
    def liczba(lst):
        l1 = []
        for el in lst:
            if el % 2 == 0:
                l1.append(el)
        return l1
    
    @staticmethod
    def liczba_2(lst):
        l2 = []
        for el in lst:
            if el % 3 == 0:
                l2.append(el)
        return l2
    
    @staticmethod
    def liczba_3(lst):
        l3 = []
        for el in lst:
            if el % 5 == 0:
                l3.append(el)
        return l3
    
    @staticmethod
    def liczba_4(lst):
        l4 = []
        for el in lst:
            if el % 7 == 0:
                l4.append(el)
        return l4
    
    @staticmethod
    def liczba_5(lst):
        l5 = []
        for el in lst:
             if el % 9 == 0:
                 l5.append(el)
        return l5
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def prostokont(x, y):
        return x * y
    
    @staticmethod
    def kwadrat(x):
        return x**2
    
    @staticmethod
    def pierwiastek(n):
        return math.sqrt(n)
    
    @staticmethod
    def rok_przestempczy(rok):
        return(rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)
    

xd = [i for i in range(1,100)]

print(f"Liczby z zakresu 1 - 100 podzielne przez 2: {statyczne_metody.liczba(xd)}")
print("="*40)
print(f"Liczby z zakresu 1 - 100 podzielne przez 3: {statyczne_metody.liczba_2(xd)}")
print("="*40)
print(f"Liczby z zakresu 1 - 100 podzielne przez 5: {statyczne_metody.liczba_3(xd)}")
print("="*40)
print(f"Liczby z zakresu 1 - 100 podzielne przez 7: {statyczne_metody.liczba_4(xd)}")
print("="*40)
print(f"Liczby z zakresu 1 - 100 podzielne przez 9: {statyczne_metody.liczba_5(xd)}")
print("="*40)

x = int(input("Podaj wartosc x: "))
y = int(input("Podaj wartosc y: "))
n = int(input("Podaj liczbe podpierwiastkowo: "))
podaj_rok = int(input("Podaj rok a system sprawdzi czy jest to kork przesempczy: "))

print(f"Suma liczb x + y = {statyczne_metody.add(x, y)}")
print("="*40)
print(f"Pole prostokonta o bokach x i y jest rowne: {statyczne_metody.prostokont(x, y)}")
print("="*40)
print(f"Pole kwadratyu o boku a jest rowne: {statyczne_metody.kwadrat(x)}")
print("="*40)
print(f"Pierwiastek z podanej liczby n jest rowny: {statyczne_metody.pierwiastek(n)}")
print("="*40)
print(f"Podany rok({podaj_rok}: {statyczne_metody.rok_przestempczy(podaj_rok)})")