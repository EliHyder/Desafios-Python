class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_pagamento(self):
        return self.salario_base


class Programador(Funcionario):
    def __init__(self, nome, salario_base, bonus_projeto):
        super().__init__(nome, salario_base)
        self.bonus_projeto = bonus_projeto

    def calcular_pagamento(self):
        # A assinatura agora é idêntica à do pai: não recebe nada extra
        return self.salario_base + self.bonus_projeto

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, gratificacao):
        super().__init__(nome, salario_base)
        self.gratificacao = gratificacao

    def calcular_pagamento(self):
        return self.salario_base + self.gratificacao
    
class Empresa:
    def __init__(self, funcionarios: list):
        self.funcionarios = funcionarios

    def folha_pagamento(self):
        total = 0
        for funcionario in self.funcionarios:
            total += funcionario.calcular_pagamento()
        return total


if __name__ == "__main__":
    funcionario = Funcionario("João", 3000)
    print(funcionario.calcular_pagamento())  # Saída: 3000
    programador = Programador("Maria", 5000, 1000)
    print(programador.calcular_pagamento())  # Saída: 6000
    gerente = Gerente("Carlos", 7000, 2000)
    print(gerente.calcular_pagamento())  # Saída: 9000
    empresa = Empresa([funcionario, programador, gerente])
    print(empresa.folha_pagamento())  # Saída: 18000