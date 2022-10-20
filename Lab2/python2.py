x = input("Podaj literę: ")
if  len(x) > 1 or len(x) == 0:
    print("nie poprawne dane")
    exit()
if x >= 'a' and x <= 'z' :
    print("mala litera")
elif   x >= 'A' and x =< 'Z' :
    print("Duza litera")
else:
    print("duza litera")
