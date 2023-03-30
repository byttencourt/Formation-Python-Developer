from datetime import datetime

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = datetime.now().year - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    

p = Pessoa('Severo', 28)
print(p.nome, p.idade)

p2 = Pessoa.criar_data_nascimento(1979,3,21,"kuizkuiz")
print(p2.nome, p2.idade)
print('-----')
print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))

