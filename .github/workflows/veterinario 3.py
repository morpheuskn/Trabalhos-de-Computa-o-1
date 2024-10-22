def cadastrar():
    entrada = True
    dados = ()
    while entrada:
        cliente = input("Cliente: ")
        animal = input("Animal: ")
        especie = input("Espécie: ")
        idade = input("Idade: ")
        peso = input("Peso: ")
        dados += ((cliente, animal, especie, idade, peso),)  
        continua = input("Deseja continuar (s/n)? ")
        if continua.lower() != 's':  
            entrada = False
    return dados

def veterinario():
    dados = ()  
    while True:
        print("Escolha uma opção:")
        print("1. Cadastrar")
        print("2. Mostrar cadastros")
        print("3. Buscar por Especie")
        print("4. Buscar por Cliente ")
        print("5. Buscar a Quantidade de Clientes e Excluir-los do Cadastro")
        print("6. Sair")
        opcao = int(input("Opção: "))

        match opcao:
            case 1:
                novos_dados = cadastrar()
                dados += novos_dados  
            case 2:
                if dados:
                    print("Cadastros realizados:")
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro  
                        print(f"Cliente: {cliente}, Animal: {animal}, Espécie: {especie}, Idade: {idade} ano(s), Peso: {peso} Kg")
                else:
                    print("Nenhum cadastro realizado.")
            case 3:
                 tipo = input("Digite a Especie: ")
                 if dados:
                    print("Cadastros realizados:")
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro 
                        if tipo in cadastro:
                        	print (f"Cliente: {cliente}, Animal: {animal}, Idade: {idade} ano(s), Peso: {peso} Kg")
            case 4:
                 nome = input("Digite o nome do cliente: ")
                 if dados:
                    print("Cadastros realizados:")
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro 
                        if nome in cadastro:
                        	print (f"Animal: {animal},Espécie: {especie}, Idade: {idade} ano(s), Peso: {peso} Kg")
            case 5:
                 nome = input("Digite o nome do cliente: ")
                 if dados:
                    print("Cadastros realizados:")
                    for cadastro in dados:
                        quantidade = 0
                        cliente, animal, especie, idade, peso = cadastro 
                        if nome in cadastro:
                        	quantidade += 1
                     print (f"{quantidade} cliente(s)")	  
            case 6:
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente.")

veterinario()
