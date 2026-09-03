def calcular_media_turma(lista_de_notas):
    # Etapa 3: Evita erro de divisão por zero caso a lista venha vazia
    if not lista_de_notas:
        return 0.0
    
    # Etapa 2 e 4: Nomes claros e simplificação usando sum()
    soma_total = sum(lista_de_notas)
    total_alunos = len(lista_de_notas)
    
    return soma_total / total_alunos

# Dados de teste
notas_alunos = [7, 8, 6, 10, 5]
resultado_media = calcular_media_turma(notas_alunos)

print(f"Média final: {resultado_media:.2f}")
