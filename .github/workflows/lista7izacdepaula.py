def cadastrar1():
    entrada = True
    dados = ()
    while entrada:
        cliente = input("Digite o nome do cliente: ").lower()  
        animal = input("Digite o nome do animal: ")
        especie = input("Digite a espécie do animal: ").lower()  
        idade = input("Digite a idade do animal (anos): ")
        peso = input("Digite o peso do animal (kg): ")
        dados += ((cliente, animal, especie, idade, peso),)  
        continua = input("Deseja inserir outro cliente? (s/n) ").lower()  
        if continua != 's':  
            entrada = False
    return dados

def veterinario1():
    dados = ()  
    while True:
        print("Escolha uma opção:")
        print("1 - Inserir um ou mais cliente(s)")
        print("2 - Mostrar a lista de clientes")
        print("3 - Listar clientes de uma espécie")
        print("4 - Listar animais de um cliente")
        print("5 - Remover um ou mais cliente(s)")
        print("6 - Sair")
        opcao = int(input("Digite uma opção: "))

        match opcao:
            case 1:
                novos_dados = cadastrar1()
                dados += novos_dados 
                
            case 2:
                if dados:
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro  
                        print(f"Dono: {cliente}, Animal: {animal}, Espécie: {especie}, Idade: {idade} ano(s), Peso: {peso} Kg")
                else:
                    print("Nenhum cadastro realizado.")
                    
            case 3:
                tipo = input("Digite a espécie que deseja procurar: ").lower()  
                if dados:
                    encontrado = False
                    for cadastro in dados:
                        cliente, animal, especie, idade, peso = cadastro 
                        if especie == tipo:
                            encontrado = True
                            print(f"Dono: {cliente}, Animal: {animal}, Idade: {idade} ano(s), Peso: {peso} Kg")
                    if not encontrado:
                        print(f"Nenhuma espécie '{tipo}' encontrada.")
                        
            case 4:
                nome = input("Digite o nome do cliente: ").lower()  
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
                while True:  
                    nome = input("Digite o nome do cliente que deseja remover: ").lower()  
                    if dados:
                        quantidade = 0
                        dados_lista = list(dados)  
                        encontrado = False
                        for cadastro in dados:
                            cliente, animal, especie, idade, peso = cadastro 
                            if cliente == nome:
                                encontrado = True
                                quantidade += 1
                                print(f"{quantidade} cliente(s) encontrado(s).")
                                confirma = input("Deseja excluir este cliente? (s/n) ").lower()  
                                if confirma == "s":
                                    dados_lista.remove(cadastro)
                                    print(f"Cliente {cliente.capitalize()} removido.")
                                elif confirma == "n":
                                    continue
                        if not encontrado:
                            print(f"Nenhum cliente com nome '{nome}' encontrado.")
                        else:
                            dados = tuple(dados_lista)  
                            print(f"{quantidade} cliente(s) removido(s).")
                    
                    continuar = input("Deseja excluir outro cliente? (s/n) ").lower()  
                    if continuar != 's':  
                        break
                        
            case 6:
                print(dados)
                print("Saindo...")
                break
                
            case _:
                print("Opção inválida, tente novamente.")

veterinario1()