import platform
import subprocess

import tabulate

from utils.helpers import parse_wmic_saida


class BIOS:

    @staticmethod
    def get_info() -> str:

        tabela = [
            ["Fabricante", "Versão", "Data"]
        ]

        try:

            if platform.system() == "Windows":

                fabricante = subprocess.check_output(
                    "wmic bios get manufacturer",
                    shell=True
                ).decode(errors="ignore")

                versao = subprocess.check_output(
                    "wmic bios get smbiosbiosversion",
                    shell=True
                ).decode(errors="ignore")

                data = subprocess.check_output(
                    "wmic bios get releasedate",
                    shell=True
                ).decode(errors="ignore")

                tabela.append([
                    parse_wmic_saida(fabricante) or "Não identificado",
                    parse_wmic_saida(versao) or "Não identificado",
                    parse_wmic_saida(data) or "Não identificado"
                ])

            else:

                tabela.append([
                    "Não suportado",
                    "Não suportado",
                    "Não suportado"
                ])

            return tabulate.tabulate(
                tabela, headers="firstrow", tablefmt="grid"
            )

        except Exception as erro:

            return {"erro": str(erro)}