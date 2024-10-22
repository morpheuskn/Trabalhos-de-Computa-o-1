def cadastrar ():
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
        if continua.lower () != 's':  
            entrada = False
    return dados

def veterinario ():
    dados = ()  
    while True:
        print("Escolha uma opção:")
        print("1. Cadastrar")
        print("2. Mostrar cadastros")
        print("3. Sair")
        opcao = int(input("Opção: "))

        match opcao:
            case 1:
                novos_dados = cadastrar ()
                dados += novos_dados  
            case 2:
                if dados:
                    print("Cadastros realizados:")
                    for cadastro in dados:
                        print(cadastro)
                        for clie, ani, esp, ida, pes in cadastro:
                        	print(f"Cliente: {clie}, Animal: {ani}, Especie: {esp}, Idade: {ida} ano(s), Peso: {pes} Kg")
                else:
                    print("Nenhum cadastro realizado.")
            case 3:
                print("Saindo...")
                break
            case _:
                print("Opção inválida, tente novamente.")

veterinario()
