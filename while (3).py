from random import randint


ile = 0
r = 0
while True:
    los = randint(1,6)
    print(los)
    if los == 6 and r == 1:
        ile += 1
        break
    elif los != 6:
        r = 0
    elif los == 6:
        r += 1
    ile += 1
print(ile)


saldo = 1000
while True:
    print(f"1 - wplata 2 - wyplata 0 - koniec")
    inp = int(input())
    if inp == 0:
        break
    elif inp == 1:
        print(f"saldo = {saldo}")
        saldo += float(input())
    elif inp == 2:
        print(f"saldo = {saldo}")
        inp = float(input())
        if inp > saldo:
            print("nie masz tyle kasy")
        else:
            saldo -= inp 