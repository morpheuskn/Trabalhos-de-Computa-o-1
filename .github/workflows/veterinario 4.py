def cadastrar1():
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
        print("4. Buscar por Cliente")
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
                tipo = input("Digite a Espécie: ")
                if dados:
                    encontrado = False
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro 
                        if especie == tipo:
                            encontrado = True
                            print(f"Cliente: {cliente}, Animal: {animal}, Idade: {idade} ano(s), Peso: {peso} Kg")
                    if not encontrado:
                        print(f"Nenhuma espécie '{tipo}' encontrada.")
                        
                        
            case 4:
                nome = input("Digite o nome do cliente: ")
                if dados:
                    encontrado = False
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro 
                        if cliente == nome:
                            encontrado = True
                            print(f"Animal: {animal}, Espécie: {especie}, Idade: {idade} ano(s), Peso: {peso} Kg")
                    if not encontrado:
                        print(f"Nenhum cliente com nome '{nome}' encontrado.")
                        
                        
            case 5:
                nome = input("Digite o nome do cliente: ")
                if dados:
                    quantidade = 0
                    dados_lista = list(dados)  
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro 
                        if cliente == nome:
                            quantidade += 1
                        print (f"{Quantidade} cliente(s) encontrados.")
                        confirma = input ("Deseja excluir este cliente? (s/n) ")
                        if confirma == "s":
                            dados_lista.remove(cadastro)  
                    dados = tuple(dados_lista)  
                    print(f"{quantidade} cliente(s) removido(s).")
                        if confirma == "n":
                        	 continue
                    if quantidade == 0:
                        print(f"Nenhum cliente com nome '{nome}' encontrado.")
                        
                        
            case 6:
                print("Saindo...")
                break
                
                
            case _:
                print("Opção inválida, tente novamente.")

veterinario()