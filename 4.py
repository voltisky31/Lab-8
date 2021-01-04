Lista = {}
a = 0
b = 1
while b != "x":
    b = input('Wpisz email lub x aby zakończyć: ')
    if b != "x":
        Lista[a] = b
    a += 1

for email in Lista.items():
    print(email)