def _menu():
    
    print("Calculadora")
    print("1.-Sumar")
    print("2.-Restar")
    print("3.-Multiplicar")
    print("4.-Dividir")
    print("5.-Salir")

def _solicitar_numeros():
    
    numero1 = float(input("Ingresa el primer numero: "))
    numero2 = float(input("Ingresa el segundo numero: "))
    return numero1,numero2

def main():
    while True:
        _menu()
        opcion_menu = input("Selecciona una opcion: ")
        if opcion_menu == '5':
            print("Adios")
            break
        if opcion_menu in ("1","2","3","4"):
            numero1,numero2 = _solicitar_numeros()
            if opcion_menu=="1":
                print("El resultado es:", numero1+numero2)
            elif opcion_menu=="2":
                print("El resultado es:", numero1-numero2)
            elif opcion_menu=="3":
                print("El resultado es:", numero1*numero2)
            elif opcion_menu=="4":
                if numero2!=0:
                    print("El resultnumero1do es:", numero1/numero2)
                else:
                    print("Error: Division por 0")
        else:
            print("Opcion no valida, intenta de nuevo")


if __name__ == "__main__":
    main()
