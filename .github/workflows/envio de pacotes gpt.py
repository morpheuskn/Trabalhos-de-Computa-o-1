def calcula_pacotes(t, x, y):
    pacotes_totais = 0
    sobra = 0
    producao_dia = [x] * t  # Lista que contém a produção diária (x) repetida t vezes
    pacotes_dia = []
    
    i = 0
    while i < t:
        # Produção do dia + sobra do dia anterior
        total_chips = producao_dia[i] + sobra
        # Calcula quantos pacotes podem ser enviados no dia
        pacotes_enviados = total_chips // y
        pacotes_dia.append(pacotes_enviados)  # Armazena o número de pacotes enviados no dia
        # Atualiza o total de pacotes enviados
        pacotes_totais += pacotes_enviados
        # Atualiza a sobra de chips para o próximo dia
        sobra = total_chips % y
        # Avança para o próximo dia
        i += 1
    
    return pacotes_totais