# Determinar o tipo de notas que o usuário deseja, se por peso ou valores reais
tipo = input(
    "Deseja notas por peso ou valores reais?(resposta deve ser 'peso' ou 'real'): ")
if tipo == "peso":
    print("Você escolheu notas por peso!")
elif tipo == "real":
    print("Você escolheu notas reais!")
else:
    print("Opção inválida!")
    exit()
# Por Peso
if tipo == "peso":
    # Determinar o valor das médias
    prova = float(input("Digite a nota da prova: "))
    caderno = float(input("Digite a nota do caderno: "))
    participação = float(input("Digite a nota por participação: "))
    comportamento = float(input("Digite a nota por comportamento: "))
    # Prova vale 50%
    # Caderno vale 20%
    # Participação vale 10%
    # Comportamento vale 20%
    # Determinar o valor das notas
    prova = prova * 0.5
    caderno = caderno * 0.2
    participação = participação * 0.1
    comportamento = comportamento * 0.2

    # determinar a média
    media = (prova + caderno + participação + comportamento)

    # Verificar se a média é maior ou igual a 7
    if media >= 7:
        print(f"A sua média é: {media:.2f}, você foi aprovado!")
    elif media >= 5:
        print(f"A sua média é: {media:.2f}, você está no conselho de classe!")
    else:
        print(f"A sua média é: {media:.2f}, você foi reprovado!")

# Por Valores Reais
if tipo == "real":
    # Determinar o valor das médias
    prova = float(input("Digite a nota da prova: "))
    caderno = float(input("Digite a nota do caderno: "))
    participação = float(input("Digite a nota por participação: "))
    comportamento = float(input("Digite a nota por comportamento: "))
    # Prova vale 5 pontos
    # Caderno vale 2 pontos
    # Participação vale 1 ponto
    # Comportamento vale 2 pontos
    # determinar a média
    media = (prova + caderno + participação + comportamento)
    if prova > 5 or caderno > 2 or participação > 1 or comportamento > 2:
        print("Uma das notas está maior que o permitido, gostaria de corrigir?")
        resposta = input("Digite sim ou não: ")
        if resposta == "sim":
            prova = float(input("Digite a nota da prova: "))
            caderno = float(input("Digite a nota do caderno: "))
            participação = float(input("Digite a nota por participação: "))
            comportamento = float(input("Digite a nota por comportamento: "))
        else:
            media = media
    if media > 10:
        print("A média está maior que 10, gostaria de corrigir?")
        resposta = input("Digite sim ou não: ")
        if resposta == "sim":
            media = float(input("Digite a média correta: "))
        else:
            media = media

    # Verificar se a média é maior ou igual a 7
    if media >= 7 and media <= 10:
        print(f"A sua média é: {media:.2f}, você foi aprovado!")
    elif media >= 5 and media < 7:
        print(f"A sua média é: {media:.2f}, você está no conselho de classe!")
    elif media > 10:
        print(
            f"A sua média é: {media:.2f}, você foi aprovado com nota maior que 10! seu ponto extra ficara para o próximo bimestre!")
    else:
        print(f"A sua média é: {media:.2f}, você foi reprovado!")
