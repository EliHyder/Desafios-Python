class Conta_Bancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque deve ser positivo.")

    def extrato(self):
        print(f"Extrato da conta de {self.titular}: Saldo atual: R${self.saldo:.2f}")

class SaldoInsuficienteError(Exception):
    """Exceção levantada quando o saldo é insuficiente."""
    pass

class ContaBancariaPro:
    def __init__(self, titular):
        self.titular = titular
        self._saldo = 0.0  # Privado!

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return True
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")

    def __str__(self):
        return f"Titular: {self.titular} | Saldo: R${self._saldo:.2f}"
    

class ContaCorrente(ContaBancariaPro):
    def __init__(self, titular, limite):
        super().__init__(titular)
        self.limite = limite

    def sacar(self, valor):
        if 0 < valor <= self.limite + self._saldo:
            self._saldo -= valor
            return True
        raise SaldoInsuficienteError("Saldo e limite insuficientes para realizar o saque.")
    

lista_contas = [
    ContaBancariaPro("Alice"),
    ContaBancariaPro("Bob"),
    ContaCorrente("Charlie", 500)
]

for conta in lista_contas:
    try:
        conta.sacar(200)  # Tentativa de saque sem saldo
    except SaldoInsuficienteError as e:
        print(f"Erro ao sacar da conta de {conta.titular}: {e}")
    print(conta)

if __name__ == "__main__":
    conta = Conta_Bancaria("João")
    conta.depositar(1000)
    conta.sacar(200)
    conta.extrato()

    conta_pro = ContaBancariaPro("Maria")
    print(conta_pro)
    conta_pro.sacar(50)  # Tentativa de saque sem saldo
    print(conta_pro)
