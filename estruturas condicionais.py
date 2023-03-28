MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
        print('Voce pode tirar a CNH')
elif idade == IDADE_ESPECIAL:
        print('Pode fazer a prova para a CNH')
else:
        print('Ainda não pode tirar Habilitação')

