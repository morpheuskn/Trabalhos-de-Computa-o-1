def calcular_bolos(ovos_disp, ovos_por_bolo, farinha_disp, farinha_por_bolo):
    # Verifica se os argumentos são válidos
    if ovos_disp < 0 or farinha_disp < 0 or ovos_por_bolo <= 0 or farinha_por_bolo <= 0:
        return (-1, -1, -1)
    
    # Calcula a quantidade de bolos possíveis com os ovos e farinha
    bolos_possiveis_ovos = ovos_disp // ovos_por_bolo
    bolos_possiveis_farinha = farinha_disp // farinha_por_bolo
    
    # A quantidade máxima de bolos será o mínimo entre bolos_possiveis_ovos e bolos_possiveis_farinha
    if bolos_possiveis_ovos < bolos_possiveis_farinha:
        bolos_possiveis = bolos_possiveis_ovos
    else:
        bolos_possiveis = bolos_possiveis_farinha
    
    # Calcula quantos ovos faltam para um bolo extra
    ovos_restantes = ovos_disp - (bolos_possiveis * ovos_por_bolo)
    if ovos_restantes < ovos_por_bolo:
        ovos_necessarios = ovos_por_bolo - ovos_restantes
    else:
        ovos_necessarios = 0
    
    # Calcula quantas caixas de ovos são necessárias (cada caixa contém 12 ovos)
    if ovos_necessarios > 0:
        caixas_ovos_necessarias = (ovos_necessarios + 11) // 12  # arredonda para cima
    else:
        caixas_ovos_necessarias = 0
    
    # Calcula quanta farinha falta para um bolo extra
    farinha_restante = farinha_disp - (bolos_possiveis * farinha_por_bolo)
    if farinha_restante < farinha_por_bolo:
        farinha_necessaria = farinha_por_bolo - farinha_restante
    else:
        farinha_necessaria = 0
    
    return (bolos_possiveis, caixas_ovos_necessarias, farinha_necessaria)

# Exemplo de uso
print(calcular_bolos(8, 10, 500, 250))  # Saída: (0, 1, 0)
