import os
import time
import re

# -----------------------------
# Funções utilitárias
# -----------------------------
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def pausar():
    input("\nPressione ENTER para continuar...")

# -----------------------------
# Função de validação de campos
# -----------------------------
def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def formatar_data_nascimento():
    while True:
        data = input("Data de nascimento (DD/MM/AAAA): ").strip()

        # Remove tudo que não for número
        numeros = re.sub(r'\D', '', data)

        # Monta a data automaticamente conforme digita
        if len(numeros) >= 2:
            data_formatada = numeros[:2]
            if len(numeros) >= 4:
                data_formatada += '/' + numeros[2:4]
                if len(numeros) > 4:
                    data_formatada += '/' + numeros[4:8]
            elif len(numeros) > 2:
                data_formatada += '/' + numeros[2:]
        else:
            data_formatada = numeros

        # Exibe a formatação automática
        print(f"Formato atual: {data_formatada}")

        # Validação final
        if re.fullmatch(r'\d{2}/\d{2}/\d{4}', data_formatada):
            dia, mes, ano = map(int, data_formatada.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
                return data_formatada
            else:
                print("Data inválida. Tente novamente.")
        else:
            print("Formato incorreto. Digite no formato DD/MM/AAAA.")

def validar_telefone(telefone):
    telefone = re.sub(r'\D', '', telefone)
    return len(telefone) == 11

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

# -----------------------------
# Função: inserir novo contato
# -----------------------------
def inserir_contato():
    limpar_tela()
    print("=================================")
    print("       INSERIR NOVO CONTATO      ")
    print("=================================\n")

    while True:
        nome = input("Nome: ").strip().title()
        if validar_nome(nome):
            break
        else:
            print("❌ Nome inválido. Digite apenas letras.\n")

    data_nascimento = formatar_data_nascimento()

    while True:
        telefone = input("Telefone (DDD + número, apenas dígitos): ").strip()
        if validar_telefone(telefone):
            break
        else:
            print("❌ Telefone inválido. Deve conter 11 dígitos (ex: 11987654321).\n")

    while True:
        email = input("E-mail: ").strip()
        if validar_email(email):
            break
        else:
            print("❌ E-mail inválido. Digite um e-mail válido (ex: nome@email.com)\n")

    print("\n✅ Contato inserido com sucesso!")
    print(f"Nome: {nome}")
    print(f"Nascimento: {data_nascimento}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")

    pausar()
    menu_principal()

# -----------------------------
# Funções principais
# -----------------------------
def tela_inicial():
    limpar_tela()
    print(r"""
                               _       
     /\                       | |      
    /  \   __ _  ___ _ __   __| | __ _ 
   / /\ \ / _` |/ _ \ '_ \ / _` |/ _` |
  / ____ \ (_| |  __/ | | | (_| | (_| |
 /_/    \_\__, |\___|_| |_|\__,_|\__,_|
           __/ |                       
          |___/                        
    """)

    print("Aperte [0] para encerrar o programa.")
    print("Aperte [1] para começar\n")
    print("Feito por Italo Costa - v1.0\n")

    while True: 
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "0":
            print("\nEncerrando o programa...")
            time.sleep(1)
            exit()
        elif escolha == "1":
            print("\nIniciando o programa...")
            time.sleep(1)
            menu_principal()
            break
        else:
            print("Opção inválida. Digite [0] ou [1].")

def menu_principal():
    limpar_tela()
    print("=================================")
    print("         AGENDA DE CONTATOS      ")
    print("=================================\n")
    print("Escolha uma opção abaixo:\n")
    print("[1] Inserir novo contato")
    print("[2] Listar contatos")
    print("[3] Deletar contatos")
    print("[4] Editar contatos")
    print("[5] Sair\n")

    while True:
        opcao = input("Digite sua opção: ").strip()

        if opcao == "1":
            inserir_contato()
            break
        elif opcao == "2":
            print("\nListando contatos...\n")
            time.sleep(1)
        elif opcao == "3":
            print("\nDeletando contatos...\n")
            time.sleep(1)
        elif opcao == "4":
            print("\nEditando contatos...\n")
            time.sleep(1)
        elif opcao == "5":
            print("\nAtualizações feitas... fechando o programa...\n")
            time.sleep(1)
            exit()
        else:
            print("Opção inválida. Digite um número de 1 a 5.\n")

# -----------------------------
# Execução
# -----------------------------
if __name__ == "__main__":
    tela_inicial()
