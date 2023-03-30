from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV')

    def desligar(self):
        print('Desligando a tv..\nDesligada.')
    
    @property
    def marca(self):
        return 'LG'

class ControleAR(ControleRemoto):
    def ligar(self):
        print('Ligando o AR')

    def desligar(self):
        print('Desligando o AR condicionado..\nDesligado.')
    
    @property
    def marca(self):
        return 'Philips'



controle = ControleTV()
controle.ligar()
controle.desligar()
controle2 = ControleAR()
controle2.ligar()
controle2.desligar()
print(controle.marca)
print(controle2.marca)
