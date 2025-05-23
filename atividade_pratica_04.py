# Nome do arquivo
nome_arquivo = "minhas_notas.txt"

# 1. Criar e escrever 3 frases no arquivo usando 'w'
print(f"Abrindo o arquivo '{nome_arquivo}' em modo de escrita ('w')...")
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    # encoding utf-8
    print("Escrevendo 3 frases iniciais...")
    arquivo.write("Esta é a primeira frase do arquivo.\n")
    arquivo.write("Python é uma linguagem de programação poderosa.\n")
    arquivo.write("Manipular arquivos é uma tarefa comum.\n")
print("Frases iniciais escritas e arquivo fechado.\n")

# 2. Adicionar 2 frases novas usando 'a'
print(f"Abrindo o arquivo '{nome_arquivo}' em modo de acréscimo ('a')...")
with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
    print("Adicionando 2 novas frases...")
    arquivo.write("Adicionando mais uma linha com o modo append.\n")
    arquivo.write("Esta é a última frase adicionada.\n")
print("Novas frases adicionadas e arquivo fechado.\n")

# 3. Ler e imprimir o conteúdo com 'with'
print(f"Lendo e imprimindo o conteúdo do arquivo '{nome_arquivo}':")
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read() # Lê todo o conteúdo do arquivo
        print("\n--- Conteúdo do Arquivo ---")
        print(conteudo)
        print("--- Fim do Conteúdo ---\n")
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")

print("Operações com o arquivo concluídas!")
