class Titulo:
    def __init__(self, numero1, nome1):
        self.numero2 = numero1
        self.nome2 = nome1

    def Exercicio(self):
        return print(f'\n\33[31m{"=" * 15}\33[m \33[35m{"Exercício"} {self.numero2}\33[m \33[34m{"=" * 15}\33[m\n'
                     f'\n\33[4;32m{self.nome2}\33[m\n')

    def Desafio(self):
        return print(f'\n\33[31m{"=" * 15}\33[m \33[35m{"Desafio"} {self.numero2}\33[m \33[34m{"=" * 15}\33[m\n'
                     f'\n\33[4;32m{self.nome2}\33[m\n')
    def Aula(self):
        return print(f'\n\033[34m{"=-*" * 10}\033[m \033[35m{"Aula"} {self.numero2}\033[m \033[34m{"=-*" * 10}\033[m\n'
                     f'\n\33[4;32m{self.nome2}\33[m\n')

