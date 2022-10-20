x = float(input("Podaj pierwsza liczba: "))
y = float(input("Podaj druga liczbe: "))
print("Jaka operacje chcesz wykonac - (dodawanie(1) /// odejmowanie (2) /// mnozenie(3) /// dzielenie (4) /// potegowanie(4)")

z = int(input())
if z == 1:
    c = x + y
elif z == 2:
    c = x - y
elif z == 3:
    c = x * y
elif z == 4:
    if y == 0:
    print("Nie mozna dzielic przez 0")
    c = x / y
elif z == 5:
    c = x ** y
else:
    print("Nie jest poprawne")
    exit()
print(c)