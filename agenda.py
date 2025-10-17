import os
import time

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

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
            print("\nInserindo novo contato...\n")
            time.sleep(1)
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

if __name__ == "__main__":
    tela_inicial()
