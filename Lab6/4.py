def maximum(*args):
    if len(args) == 0:
        return None
    pom = args[0]
    for a in args[1:]:
        if pom < a:
            pom = a
    return pom
maks = maximum(30, 2, 10, 2, 5)
#print(maks)
#maks = maximum()
#print(maks)
def maximum2(a1, *args):
    pom = a1
    for a in args:
        if pom < a:
            pom = a
    return pom
maks = maximum2(30, 2, 10, 2, 5)
print(maks)
maks = maximum2(2)
print(maks)