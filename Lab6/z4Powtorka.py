def znaki(s):
    result ={}
    for char in s:
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    return result
s = 'znaki napisu'
ch = znaki(s)
print(ch)

for k in sorted(ch.keys()):
    print(k,ch[k] )
