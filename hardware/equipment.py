import platform
import socket
import subprocess
import uuid

import tabulate

from utils.helpers import parse_wmic_saida

class Equipment:
    @staticmethod
    def get_info() -> str:

        dados = [
            ["Identificação", socket.gethostname()],
            ["Fabricante", "Não identificado"],
            ["Modelo", "Não identificado"],
            ["Serial", "Não identificado"]
        ]

        if platform.system() == "Windows":

                fabricante = subprocess.check_output(
                    "wmic computersystem get manufacturer",
                    shell=True
                ).decode(errors="ignore")

                modelo = subprocess.check_output(
                    "wmic computersystem get model",
                    shell=True
                ).decode(errors="ignore")

                serial = subprocess.check_output(
                    "wmic bios get serialnumber",
                    shell=True
                ).decode(errors="ignore")

                if valor := parse_wmic_saida(fabricante):
                    dados[1][1] = valor

                if valor := parse_wmic_saida(modelo):
                    dados[2][1] = valor

                if valor := parse_wmic_saida(serial):
                    dados[3][1] = valor

        return tabulate.tabulate(dados, headers="firstrow", tablefmt="grid")