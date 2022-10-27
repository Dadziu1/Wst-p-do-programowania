x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj druga liczbe: "))

if(x>y):
    x,y = y,x

while(x <= y):
    if x % 2 == 1:
        x += 1
        continue
    print(x, end=" ")
    x = x + 1
