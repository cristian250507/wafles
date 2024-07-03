contador = 0 
while True:
    opc1 = int(input(""" 1.- Sabor helado $1000
        Eliga su sabor: """))
    if opc1 == 1:
        contador += 1000
        opc2=input("Quiere agregar topin (Si/No) valor de por topin $500: ").lower()
        if opc2 == "si":
            opc3 = int(input("Cuantos topin quiere agragar hasta 3: "))
            if opc3 >3:
                print("ingrese una cantidad valida")
                break
            total_topin=opc3 * 500
            contador += total_topin
            opc4 = input("Quiere que le sirvan el waffle (Si/No)").lower()
            if opc4 == "si":
                contador -= 200
                print("Su total es de", contador)
                opc5= int(input("Ingrese con la cantidad de dinero que va a pagar: "))
                if opc5== 1000 and contador <= 1000:
                  print("Compra realizada con exisito")
                  break
                else:
                   total = opc5 - contador
                   print("Compra realizada con exisito")
                break
            elif opc4 == "no":
                contador +=200
                opc5= int(input("Ingrese con la cantidad de dinero que va a pagar: "))
                if contador<=1000:
                  print("Su total es", contador)
                  print("Compra realizada con exisito")
                  break
                elif opc5>1000:
                   print("Su total es",contador)
                   total = opc5 - contador
                   print("Su vuelto es", total)
                else:
                    print("No puede pagar con esa cantidad de dinero ingrese una cantidad valida")
                break
            else:
                print("Ingrese una opcion valida")
        elif opc2 == "no":
            opc6 = input(("Quiere que le sirvan el waffle (Si/No)").lower())
            if opc6 == "si":
                contador -= 200
                opc5= int(input("Ingrese con la cantidad de dinero que va a pagar: "))
                if contador<= 1000:
                   print("Compra realizada con exisito")
                   break
                elif opc5>1000:
                    print("Su total es",contador)
                    total = opc5 - contador
                    print("Su vuelto es de", total)
                    break
            elif opc6 == "no":
                contador +=200
                opc5= int(input("Ingrese con la cantidad de dinero que va a pagar: "))
                if contador<=1000:
                  print("Su total es", contador)
                  print("Compra realizada con exisito")
                  break
                elif opc5>1000:
                   print("Su total es",contador)
                   total = opc5 - contador
                   print("Su vuelto es", total)
                else:
                    print("No puede pagar con esa cantidad de dinero ingrese una cantidad valida")
                break
            else:
                print("Ingrese una opcion valida")
        else:
            print("Ingrese una opcion valida")
    else:
        print("Ingrese un opcion valida")
        break