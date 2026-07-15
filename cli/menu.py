from utils.helpers import (
    limpar_tela,
    pausar,
    cabecalho
)

from utils.loader import Loader
from utils.web_launcher import WebLauncher


class Menu:

    def run(self):

        while True:

            limpar_tela()

            cabecalho(
                "DIAG-DB"
            )

            print("[1] Hardware")
            print("[2] Network")
            print("[3] Sistema Operacional")
            print("[4] Processos")
            print("[5] Relatórios")
            print("[6] Web")
            print("[0] Sair")
            print()

            opcao = input("Escolha: ").strip()
         
            if opcao == "1":
                self.menu_hardware()

            elif opcao == "2":
                self.menu_network()

            elif opcao == "3":
                self.menu_sistema()

            elif opcao == "4":
                self.menu_processos()

            elif opcao == "5":
                self.menu_relatorios()

            elif opcao == "6":
                WebLauncher.abrir_web()

            elif opcao == "0":
                self.sair()

            else:
                print("\nOpção inválida.")
                pausar()

    # ======================================================
    # HARDWARE
    # ======================================================

    def menu_hardware(self):

        from hardware.equipment import Equipment
        from hardware.cpu import CPU
        from hardware.memory import Memory
        from hardware.bios import BIOS
        from hardware.disk import Disk
        from hardware.motherboard import Motherboard

        while True:

            limpar_tela()
            cabecalho("Hardware")

            print("[1] Equipamento")
            print("[2] CPU")
            print("[3] Memória")
            print("[4] BIOS")
            print("[5] Disco")
            print("[6] Placa-Mãe")
            print("[0] Voltar")
            print()

            opcao = input("Escolha: ").strip()

            if opcao == "0":
                return

            elif opcao == "1":
                dados = Equipment.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "2":
                dados = CPU.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "3":
                dados = Memory.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "4":
                dados = BIOS.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "5":
                dados = Disk.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "6":
                dados = Motherboard.get_info()
                print("\n", dados, "\n")
                pausar()

            else:
                print("\nOpção inválida.")
                pausar()

    def menu_network(self):

        from network.interfaces import Interfaces
        from network.ip import IPAddress
        from network.gateway import Gateway
        from network.dns import DNS
        from network.ping import Ping
        from network.ports import Ports

        while True:

            limpar_tela()
            cabecalho("Network")

            print("[1] Interfaces")
            print("[2] Endereços IP")
            print("[3] Gateway")
            print("[4] DNS")
            print("[5] Ping Google")
            print("[6] Portas")
            print("[0] Voltar")
            print()

            opcao = input("Escolha: ").strip()

            if opcao == "0":
                return

            elif opcao == "1":
                dados = Interfaces.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "2":
                dados = IPAddress.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "3":
                dados = Gateway.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "4":
                dados = DNS.get_info()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "5":
                dados = Ping.ping_google()
                print("\n", dados, "\n")
                pausar()

            elif opcao == "6":
                dados = Ports.get_info()
                print("\nTop portas (primeiras 20):\n")
                print(dados[:20])
                pausar()

            else:
                print("\nOpção inválida.")
                pausar()

    def menu_sistema(self):

        from system.os_info import OSInfo

        limpar_tela()
        cabecalho("Sistema Operacional")

        dados = OSInfo.get_info()

        print("\n", dados, "\n")

        pausar()


    def menu_processos(self):

        from processes.process_list import ProcessList

        limpar_tela()
        cabecalho("Processos")

        resumo = ProcessList.resumo_formatado()
        processos = ProcessList.get_info_formatado(limit=30)

        print("\nRESUMO:\n")
        print(resumo)

        print("\nPROCESSOS:\n")
        print(processos)

        pausar() 

    def menu_relatorios(self):

        from reports.exporter import ReportExporter

        limpar_tela()
        cabecalho("Relatórios")

        print("[1] Exportar TXT")
        print("[2] Exportar JSON")
        print("[0] Voltar")
        print()

        opcao = input("Escolha: ").strip()

        if opcao == "0":
            return

        if opcao == "1":
            arquivo = ReportExporter.exportar_txt()
            print("\nRelatório gerado:", arquivo)

        elif opcao == "2":
            arquivo = ReportExporter.exportar_json()
            print("\nRelatório gerado:", arquivo)

        else:
            print("\nOpção inválida.")

        pausar()
    def sair(self):

        print("\nA interface WEB deve continuar ativa?")
        print("[S] Sim")
        print("[N] Não")
        print()

        resposta = input("Escolha: ").strip().upper()

        if resposta == "N":
            WebLauncher.encerrar_servidor()

        raise SystemExit