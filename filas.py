from collections import deque
import time

def main():
    fila = deque()

    while True:
        print("\n" + "=" * 45)
        print(" ESTRUTURA DE DADOS: FILA (FIFO) ")
        print(" Contexto: Fila de Atendimento do Banco")
        print("=" * 45)
        print(f" PRÓXIMO A SER ATENDIDO -> {fila[0] if fila else '[Fila Vazia]'}")
        print(f" Fila Completa          -> {list(fila)}")
        print("-" * 45)
        print("1. Chegada de Cliente (Enqueue)")
        print("2. Atender Próximo Cliente (Dequeue)")
        print("3. Espiar Primeiro da Fila (Peek)")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cliente = input("Digite o nome do cliente: ")
            if cliente.strip():
                fila.append(cliente)  # Enqueue (entra no final da fila)
                print(f"Cliente '{cliente}' entrou no FIM da fila!")
            else:
                print("Nome inválido.")

        elif opcao == "2":
            if fila:
                atendido = fila.popleft()  # Dequeue (sai do início da fila)
                print(f"Cliente atendido: '{atendido}'")
            else:
                print("A fila está vazia! Ninguém para atender.")

        elif opcao == "3":
            if fila:
                print(f"Primeiro da fila: '{fila[0]}'")
            else:
                print("A fila está vazia!")

        elif opcao == "0":
            print("\nSaindo do programa de Fila...")
            break
        else:
            print("Opção inválida!")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
