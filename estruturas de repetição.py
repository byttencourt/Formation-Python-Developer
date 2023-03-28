limite = 1000
opcao = -1
while opcao != 0:   
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))  
        
    if opcao == 1:       
        print("Sacando...")
        valor = float(input('Qual valor do saque?'))
        if limite < valor:
            print('Saque bloqueado valor excede limite.')
        else:
            print('Retire o valor na gaveta.')   
    elif opcao == 2:       
        print("Exibindo o extrato...")
    else:
        break
