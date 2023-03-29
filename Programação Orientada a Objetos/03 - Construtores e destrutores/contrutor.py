class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe ...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Destruindo a classe')


    def falar(self):
        print('Au Au')

    
def criar_cachorro():
    c = cachorro('Juju', 'Preta', False)
    print(c.nome)

c = cachorro('Chappie', 'amarelo')
c.falar()
criar_cachorro()

print('ola mundo')
del c
print('ola mundo')
print('ola mundo')
print('ola mundo')
print('ola mundo')
print('ola mundo')