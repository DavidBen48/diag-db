import platform
import subprocess

import tabulate

from utils.helpers import parse_wmic_saida


class Motherboard:

    @staticmethod
    def get_info() -> str:

        try:

            tabela = [
                ["Fabricante", "Produto", "Serial"]
            ]

            if platform.system() == "Windows":

                fabricante = subprocess.check_output(
                    "wmic baseboard get manufacturer",
                    shell=True
                ).decode(errors="ignore")

                produto = subprocess.check_output(
                    "wmic baseboard get product",
                    shell=True
                ).decode(errors="ignore")

                serial = subprocess.check_output(
                    "wmic baseboard get serialnumber",
                    shell=True
                ).decode(errors="ignore")

                tabela.append([
                    parse_wmic_saida(fabricante) or "Desconhecido",
                    parse_wmic_saida(produto) or "Desconhecido",
                    parse_wmic_saida(serial) or "Desconhecido"
                ])

            else:

                tabela.append([
                    "Não suportado",
                    "Não suportado",
                    "Não suportado"
                ])

            return tabulate.tabulate(
                tabela,
                headers="firstrow",
                tablefmt="grid"
            )

        except Exception as erro:

            return f"Erro ao obter informações da placa-mãe: {str(erro)}"