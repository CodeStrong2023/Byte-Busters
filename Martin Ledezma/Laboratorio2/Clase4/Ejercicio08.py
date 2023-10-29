print("Menu Interactivo - Cajero Automatico")
#hacer un programa que simule ser un cajero automatico con un saldo
#incial de 1000 y tendra el sig. menu de opciones:
#       1.Ingresar el dinero de la cuenta
#       2.Retirar dinero de la cuenta
#       3.Mostrar dinero disponible
#       4.Salir

saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1.Igresar el dinero de la cuenta")
    print("2.Retirar dinero de la cuenta")
    print("3.Mostrar dinero disponible")
    print("4.Salir")
    print("")
    opcion = int(input("digite una opcion del menu:"))
    print()
    if opcion == 1:
        extra = float(input("cuanto dinero desea ingresar ->"))
        saldo += extra
        print(f"diner en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        retirar = float(input("cuanto dinero desea retirar ->"))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"dinero en la cuenta al momento: ${saldo}")
    elif opcion == 4:
        print("Gracias por utilizar su cajero automatico, hasta pronto")
        break
    else:
        print("Error, se equivoco de opcion de menus")
