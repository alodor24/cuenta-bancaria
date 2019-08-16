class Bank_Account:
    def __init__(self):
        self.balance = 0
        print('*** Bienvenido al sistema informático del banco ***')

    def deposit(self):
        amount = float(input('Introduzca el monto a depositar: '))
        self.balance += amount
        print('\n Monto depositado:', amount)

    def withdraw(self):
        amount = float(input('Introduzca el monto a retirar: '))

        if self.balance >= amount:
            self.balance -= amount
            print('\n Monto retirado:', amount)
        else:
            print('\n Balance insuficiente')

    def display(self):
        print('\n Saldo neto disponible =', self.balance)

# Creando un objeto de la clase
s = Bank_Account()

# Ejecutar acciones
s.deposit()
s.withdraw()
s.display()