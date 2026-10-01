nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: ")) 
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média final é: {media}")
# Turma A
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
disciplinas = ['Matemática', 'Português', 'Ciências', 'História', 'Geografia']
notas_turma_a = [7.5, 8.0, 6.5, 9.0, 7.0]
cores = ["#7ACEF8", "#FA9CCB", "#ADFFAA", "#FFA98F",  "#3E0057"]

barras_a = ax1.bar(disciplinas, notas_turma_a, color=cores)
ax1.bar(disciplinas, notas_turma_a, color=cores)
ax1.set_title('Notas da turma A')
ax1.set_xlabel('Disciplinas')
ax1.set_ylabel('Notas')
ax1.bar_label(barras_a)
# Turma B
disciplinas = ['Matemática', 'Português', 'Ciências', 'História', 'Geografia']
notas_turma_b = [8.5, 7.0, 8.0, 6.5, 8.5]
cores = ["#4F07F7", "#238861", "#67087A", "#EBFC07",  "#F30F0F"]

barras_b = ax2.bar(disciplinas, notas_turma_b, color=cores)
ax2.bar(disciplinas, notas_turma_b, color=cores)
ax2.set_title('Notas da turma B')
ax2.set_xlabel('Disciplinas')
ax2.set_ylabel('Notas')
ax2.bar_label(barras_b)
plt.tight_layout()
plt.ylim(0, 10.5)
plt.savefig('comparacao_turmas.png')
plt.show()
dados_vendas = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset', 
                'Notebook', 'Mouse', 'Teclado', 'Monitor', 'Headset'],
    'Vendedor': ['Ana', 'João', 'Ana', 'João', 'Maria', 
                 'Maria', 'Ana', 'João', 'Maria', 'Ana'],
    'Quantidade': [5, 10, 8, 3, 15, 7, 12, 6, 4, 9],
    'Preco': [2500, 80, 200, 1200, 300, 2500, 80, 200, 1200, 300],
    'Data': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
             '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10']
}

df_vendas = pd.DataFrame(dados_vendas)
def calcular_salario(valor_hora, horas_trabalhadas):
    if valor_hora < 0 or horas_trabalhadas < 0:
      ValueError('Não pode ser negativo')
    return valor_hora * horas_trabalhadas
valor_hora = float(input('Digite quanto voce ganha por hora: '))
horas = float(input('Digite quantas horas voce trabalha no mês: '))
        
salario = calcular_salario(valor_hora, horas)
print(f'Seu salário do mês é: R${salario}')