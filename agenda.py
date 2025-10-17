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
        print("\n Encerrando o programa...")
        time.sleep(1)
        exit
    elif escolha == "1":
        print("\n Inicinado o programa...")
        time.sleep(1)
        break
    else:
        print("Opção inválida, digite [0] ou [1].")

if __name__ == "__main__":
    tela_inicial()