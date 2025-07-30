class CuentaBancaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0.0

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se depositaron ${monto:.2f}")
        else:
            print("El monto debe ser mayor a cero")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Se retiraron ${monto:.2f}")
        else:
            print("Fondos insuficientes o monto inválido")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.nombre}: ${self.saldo:.2f}")

def menu_banco():
    print("\n=== Banco Simple ===")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver saldo")
    print("4. Salir")

def main():
    nombre = input("Ingresa tu nombre: ")
    cuenta = CuentaBancaria(nombre)

    while True:
        menu_banco()
        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            monto = float(input("Monto a depositar: "))
            cuenta.depositar(monto)
        elif opcion == '2':
            monto = float(input("Monto a retirar: "))
            cuenta.retirar(monto)
        elif opcion == '3':
            cuenta.mostrar_saldo()
        elif opcion == '4':
            print("Gracias por usar el banco.")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
