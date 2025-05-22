#verifica se a senha é forte
def verificar_senha():
    while True:
        pwd = input(
            "Senha (mín. 8c, 1 num, 1 letra) ou 'sair': "
        ).strip()  # 'pwd' é uma abreviação comum para password

        if pwd.lower() == "sair":
            print("Programa encerrado.")
            break

        # Verificações mais concisas
        len_ok = len(pwd) >= 8
        tem_num = any(c.isdigit() for c in pwd)  # Verifica se algum caractere é dígito
        tem_letra = any(c.isalpha() for c in pwd)  # Verifica se algum caractere é letra

        if len_ok and tem_num and tem_letra:
            print("Senha forte! Senha válida registrada.")
            break
        else:
            print("\nSenha fraca. Por favor, tente novamente. Requisitos:")
            if not len_ok:
                print("- A senha deve ter pelo menos 8 caracteres.")
            if not tem_num:
                print("- A senha deve conter pelo menos um número.")
            if not tem_letra:
                print("- A senha deve conter pelo menos uma letra.")
            print("-" * 30)

verificar_senha()

# calculando a gorjeta do garçom
def gorjeta():
    valor_conta = float(input("Digite o valor da conta: "))
    porcentagem_gorjeta = float(
        input("Digite a porcentagem da gorjeta (ex: 10 para 10%): ")
    )
    gorjeta = (porcentagem_gorjeta / 100) * valor_conta
    total = valor_conta + gorjeta
    print(f"A gorjeta é: R$ {gorjeta:.2f}")
    print(f"O total a pagar é: R$ {total:.2f}")
    return gorjeta, total

gorjeta()
