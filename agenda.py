import os
import time
import re
import json

ARQUIVO_CONTATOS = "contatos.json"  # <-- Corrigido nome da variável (antes estava "ARQUIVOS_CONTATOS")

# -----------------------------
# Funções utilitárias
# -----------------------------
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def pausar():
    input("\nPressione ENTER para continuar...")

# -----------------------------
# Funções de persistência
# -----------------------------
def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=4, ensure_ascii=False)

def carregar_contatos():
    if os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# -----------------------------
# Função de validação de campos
# -----------------------------
def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def formatar_data_nascimento():
    while True:
        data = input("Data de nascimento (DD/MM/AAAA): ").strip()
        numeros = re.sub(r'\D', '', data)

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

        print(f"Formato atual: {data_formatada}")

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

    contatos = carregar_contatos()
    novo_contato = {
        "nome": nome,
        "nascimento": data_nascimento,
        "telefone": telefone,
        "email": email
    }

    contatos.append(novo_contato)
    salvar_contatos(contatos)

    print("\n✅ Contato inserido com sucesso!")
    print(f"Nome: {nome}")
    print(f"Nascimento: {data_nascimento}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")

    pausar()
    menu_principal()

# -----------------------------
# Função: listar contatos
# -----------------------------
def listar_contatos():
    limpar_tela()
    contatos = carregar_contatos()

    if not contatos:
        print("Nenhum contato cadastrado.")
        pausar()
        menu_principal()
        return  
    print("=================================")
    print("          LISTAR CONTATOS        ")
    print("=================================\n")

    for i, contato in enumerate(contatos, start=1):
        print(f"[{i}] {contato['nome']}")
    
    print("\nDigite o número do contato para ver detalhes ou 0 para voltar")

    while True:
        escolha = input("\nEscolha: ").strip()

        if escolha == "0":
            menu_principal()
            return
        
        if escolha.isdigit() and 1 <= int(escolha) <= len(contatos):
            c = contatos[int(escolha) - 1]
            limpar_tela()
            print(f"=== DETALHES DO CONTATO [{escolha}] ===")
            print(f"Nome: {c['nome']}")
            print(f"Nascimento: {c['nascimento']}")
            print(f"Telefone: {c['telefone']}")
            print(f"E-mail: {c['email']}")
            pausar()
            listar_contatos()
            return
        else:
            print("Opção inválida. Digite um número válido.")

# -----------------------------
# Função: deletar contato
# -----------------------------
def deletar_contato():
    limpar_tela()
    contatos = carregar_contatos()

    if not contatos:
        print("Nenhum contato cadastrado.")
        pausar()
        menu_principal()
        return
    
    print("=================================")
    print("         DELETAR CONTATO         ")
    print("=================================\n")

    for i, contato in enumerate(contatos, start=1):
        print(f"[{i}] {contato['nome']}")
    
    print("\nDigite o número do contato que deseja deletar ou 0 para voltar")

    while True:
        escolha = input("\nEscolha ").strip()

        if escolha == "0":
            menu_principal()
            return
        
        if escolha.isdigit() and 1 <= int(escolha) <= len(contatos):
            indice = int(escolha) - 1
            contato = contatos[indice]

            limpar_tela()
            print(f"=== DETALHES DO CONTATO [{escolha}] ===")
            print(f"Nome: {contato['nome']}")
            print(f"Nascimento: {contato['nascimento']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"E-mail: {contato['email']}")
            print("\n[0] Voltar")
            print("[1] Deletar este contato")

            while True:
                confirmacao = input("\nEscolha: ").strip()
                if confirmacao == "0":
                    deletar_contato()
                    return
                elif confirmacao == "1":
                    nome_excluido = contato['nome']
                    del contatos[indice]
                    salvar_contatos(contatos)
                    print(f"\n Contato '{nome_excluido}' deletado com sucesso")
                    pausar()
                    menu_principal()
                    return
                else: print("Opção inválida. Digite [0] ou [1].")
            else:
                print("Opção inválida. Digite um número válido.")

# -----------------------------
# Função: editar contato
# -----------------------------
def editar_contato():
    limpar_tela()
    contatos = carregar_contatos()

    if not contatos:
        print("Nenhum contato cadastrado.")
        pausar()
        menu_principal()
        return

    print("=================================")
    print("          EDITAR CONTATO         ")
    print("=================================\n")

    for i, contato in enumerate(contatos, start=1):
        print(f"[{i}] {contato['nome']}")
    
    print("\nDigite o número do contato que deseja editar ou 0 para voltar.")

    while True:
        escolha = input("\nEscolha: ").strip()

        if escolha == "0":
            menu_principal()
            return

        if escolha.isdigit() and 1 <= int(escolha) <= len(contatos):
            indice = int(escolha) - 1
            contato = contatos[indice]

            while True:
                limpar_tela()
                print(f"=== EDITANDO CONTATO [{escolha}] ===")
                print(f"[1] Nome: {contato['nome']}")
                print(f"[2] Nascimento: {contato['nascimento']}")
                print(f"[3] Telefone: {contato['telefone']}")
                print(f"[4] E-mail: {contato['email']}")
                print("\n[0] Voltar (salvar alterações)")

                opcao = input("\nEscolha o campo que deseja editar: ").strip()

                if opcao == "0":
                    salvar_contatos(contatos)
                    print("\n✅ Alterações salvas com sucesso!")
                    pausar()
                    menu_principal()
                    return

                elif opcao == "1":
                    novo_nome = input("Novo nome: ").strip().title()
                    if validar_nome(novo_nome):
                        contato["nome"] = novo_nome
                        print("✅ Nome atualizado com sucesso!")
                    else:
                        print("❌ Nome inválido. Digite apenas letras.")

                elif opcao == "2":
                    novo_nascimento = formatar_data_nascimento()
                    contato["nascimento"] = novo_nascimento
                    print("✅ Data de nascimento atualizada!")

                elif opcao == "3":
                    while True:
                        novo_telefone = input("Novo telefone (DDD + número, apenas dígitos): ").strip()
                        if validar_telefone(novo_telefone):
                            contato["telefone"] = novo_telefone
                            print("✅ Telefone atualizado!")
                            break
                        else:
                            print("❌ Telefone inválido. Deve conter 11 dígitos (ex: 11987654321).")

                elif opcao == "4":
                    while True:
                        novo_email = input("Novo e-mail: ").strip()
                        if validar_email(novo_email):
                            contato["email"] = novo_email
                            print("✅ E-mail atualizado!")
                            break
                        else:
                            print("❌ E-mail inválido. Digite um e-mail válido.")

                else:
                    print("Opção inválida. Digite um número de 0 a 4.")
                
                pausar()
        else:
            print("Opção inválida. Digite um número válido.")

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
            listar_contatos()  
            break
        elif opcao == "3":
            deletar_contato()
            break
        elif opcao == "4":
            editar_contato()
            break
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
