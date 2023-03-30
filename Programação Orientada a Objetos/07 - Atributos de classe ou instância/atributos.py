class Estudante:
    escola = 'Python.org'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
def mostrarvalores(*objs):
        for obj in objs:
            print(obj)
    
nico = Estudante('Nicolas', 1234)
nino = Estudante('NINO', 1235)

print(nino)
print(nico)
print('----')
nino.matricula = 4660
nino.nome = 'Claudio Alexandre Bittencourt'
nino.escola = 'Dio'
mostrarvalores(nino, nico)
print('----')

Estudante.escola = 'Dio'
mostrarvalores(nino, nico)
print('----')
josi = Estudante('Josilene', 1236)
mostrarvalores(nino, nico, josi)