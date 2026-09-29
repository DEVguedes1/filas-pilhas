from collections import deque
import time

def main():
    pilha = deque()

    while True:
        print("\n" + "=" * 45)
        print(" ESTRUTURA DE DADOS: PILHA (LIFO) ")
        print(" Contexto: Histórico de Ações (Ctrl+Z)")
        print("=" * 45)
        print(f" TOPO DA PILHA -> {pilha[-1] if pilha else '[Pilha Vazia]'}")
        print(f" Estado Atual  -> {list(pilha)}")
        print("-" * 45)
        print("1. Inserir Ação (Push)")
        print("2. Desfazer Última Ação (Pop)")
        print("3. Espiar o Topo (Peek)")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            acao = input("Digite a ação realizada (ex: Digitou 'Olá'): ")
            if acao.strip():
                pilha.append(acao)  # Push (empilha no topo)
                print(f"Ação '{acao}' empilhada no TOPO!")
            else:
                print("Texto inválido.")

        elif opcao == "2":
            if pilha:
                removido = pilha.pop()  # Pop (desempilha do topo)
                print(f"[Ctrl+Z] Ação desfeita: '{removido}'")
            else:
                print("A pilha está vazia! Não há o que desfazer.")

        elif opcao == "3":
            if pilha:
                print(f" Elemento no TOPO atual: '{pilha[-1]}'")
            else:
                print("A pilha está vazia!")

        elif opcao == "0":
            print("\nSaindo do programa de Pilha...")
            break
        else:
            print("Opção inválida!")
        
        time.sleep(1)

if __name__ == "__main__":
    main()