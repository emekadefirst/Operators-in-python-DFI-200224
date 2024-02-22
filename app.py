print("which bus-top you dey con down\n ikeja - 200\negbeda - 300\nipaja - 400")

stop = input("where you dey come down>>>")
egbeda = 300
ikeja = 200
ipaja = 400

if stop == 'egbeda' or stop == "1":
    print(f"{stop} how much dey your hand")
    cash = int(input())
    if cash >= 600:
        print("come down abeg i no get change")
    elif cash <600 or cash == egbeda:
        balance = cash - egbeda
        print(f"oya enter your change na{balance}")
    else:
        print("wetin this one dey talk comot for here")

elif stop == 'ikeja' or stop == "2":
    print(f'how much dey your hand>>')
    cash = int(input())
    if cash >= 600:
        print("come down abeg i no get change")
    elif cash <600 or cash == ikeja:
        balance = cash - ikeja
        print(f"oya enter your change na {balance}")
    else:
        print("wetin this one dey talk comot for here")

elif stop == 'ipaja' or stop == "3":
    print(f'how much dey your hand>>')
    cash = int(input())
    if cash >= 600:
        print("come down abeg i no get change")
    elif cash <600 or cash == ipaja:
        balance = cash - ipaja
        print(f"oya enter your change na {balance}")
    else:
        print("wetin this one dey talk comot for here")

else:
    print(f"i no dey go {stop} come down make better passanger enter abeg")
    

