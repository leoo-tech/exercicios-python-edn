# Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.

# Inicializa a lista de notas

notas = []

# Loop para solicitar notas

while True:
    nota = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

    # Verifica se o usuário deseja encerrar
    if nota.lower() == 'fim':
        break

    # Tenta converter a entrada para float
    try:
        nota = float(nota)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")
        continue

    # Verifica se a nota está dentro do intervalo válido
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida. As notas devem estar entre 0 e 10.")
        
# Verifica se há notas registradas
if notas:
    # Calcula a média
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
    
else:
    print("Nenhuma nota válida foi registrada.")
# Fim do programa

# O programa solicita notas de alunos até que o usuário digite 'fim'.