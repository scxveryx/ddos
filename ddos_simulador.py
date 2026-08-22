import os
import time
import random

# Cores ANSI
CYAN = "\033[96m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RESET = "\033[0m"


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def barra(valor, maximo=100, tamanho=40):
    valor = min(valor, maximo)
    preenchido = int((valor / maximo) * tamanho)
    return "█" * preenchido + "░" * (tamanho - preenchido)


def painel():
    alvo = "LAB-TESTE"
    rps = 0
    total = 0
    bloqueado = False

    while True:
        limpar()

        print(CYAN + "=" * 60 + RESET)
        print(CYAN + "        DDOS SIMULATOR — LABORATÓRIO LOCAL" + RESET)
        print(CYAN + "=" * 60 + RESET)

        print(f"\n{WHITE}ALVO: {YELLOW}{alvo}")
        print(f"{WHITE}MODO: {GREEN}SIMULAÇÃO")
        print(f"{WHITE}TRÁFEGO REAL: {GREEN}DESATIVADO")
        print(f"{WHITE}STATUS: ", end="")

        if bloqueado:
            print(RED + "BLOQUEIO ATIVO" + RESET)
        else:
            print(GREEN + "MONITORANDO" + RESET)

        # Simulação de tráfego
        if not bloqueado:
            rps = random.randint(100, 5000)
            total += rps

        print(f"\n{CYAN}RPS ATUAL:{RESET} {rps}")
        print(f"{CYAN}TOTAL SIMULADO:{RESET} {total}")

        print(f"\n{WHITE}CARGA SIMULADA")
        print(f"{CYAN}[{barra(rps, 5000)}]{RESET}")

        if rps > 4000 and not bloqueado:
            print("\n" + RED + "!!! ALERTA: TRÁFEGO SIMULADO ELEVADO !!!" + RESET)

        if bloqueado:
            print("\n" + RED + "████████████████████████████████████████" + RESET)
            print(RED + "       BLOQUEIO FICTÍCIO ATIVADO" + RESET)
            print(RED + "████████████████████████████████████████" + RESET)

        print("\n" + GRAY + "-" * 60 + RESET)
        print(" [1] Iniciar simulação")
        print(" [2] Ativar bloqueio fictício")
        print(" [3] Desativar bloqueio")
        print(" [4] Resetar contador")
        print(" [5] Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            for _ in range(10):
                if bloqueado:
                    break

                limpar()
                rps = random.randint(500, 5000)
                total += rps

                print(CYAN + "DDOS SIMULATOR — EXECUÇÃO FICTÍCIA" + RESET)
                print(f"\nAlvo: {alvo}")
                print(f"RPS: {rps}")
                print(f"Total: {total}")
                print(f"[{barra(rps, 5000)}]")

                if rps > 4000:
                    print(RED + "\n[!] ALERTA DE TRÁFEGO" + RESET)

                time.sleep(1)

        elif opcao == "2":
            bloqueado = True
            print(GREEN + "\n[+] Bloqueio fictício ativado." + RESET)
            time.sleep(1)

        elif opcao == "3":
            bloqueado = False
            print(YELLOW + "\n[-] Bloqueio fictício desativado." + RESET)
            time.sleep(1)

        elif opcao == "4":
            total = 0
            rps = 0
            print(GREEN + "\n[+] Contador resetado." + RESET)
            time.sleep(1)

        elif opcao == "5":
            limpar()
            print(CYAN + "Encerrando simulador..." + RESET)
            break

        else:
            print(RED + "\nOpção inválida." + RESET)
            time.sleep(1)


if __name__ == "__main__":
    painel()
