from os import system
system("cls")


a= input("pertecene a la florida?(si/no): ")
if a == "si":
    print("continua a la siguiente")
    b = input("tiene carnet?(si/no): ")
    if b == 'si':
        carnet=int(input(("ingrese numero: ")))
    if b == 'no':
        print("crear carnet aqui!")
        carnet=int(input("colocar 8 numeros: "))
    c = input("es jubilado?(si/no): ")
    if c == 'si':
        monto=int(input("ingrese monto: "))*0.75
        print("+ 25% -> total = ",round(monto))
    if c == 'no':
        print("se pago monto total $2000")    
else:
    print("gracias por visitar")