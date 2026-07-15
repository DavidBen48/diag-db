import json
import socket
from datetime import datetime
from pathlib import Path

import tabulate

from hardware.equipment import Equipment
from hardware.cpu import CPU
from hardware.memory import Memory
from hardware.bios import BIOS
from hardware.disk import Disk
from hardware.motherboard import Motherboard

from network.interfaces import Interfaces
from network.ip import IPAddress
from network.gateway import Gateway
from network.dns import DNS
from network.ports import Ports

from system.os_info import OSInfo

from processes.process_list import ProcessList


class ReportExporter:

    REPORT_DIR = Path("relatorios")

    @classmethod
    def coletar_dados(cls) -> dict:

        return {
            "equipamento": Equipment.get_info(),
            "cpu": CPU.get_info(),
            "memoria": Memory.get_info(),
            "bios": BIOS.get_info(),
            "discos": Disk.get_info(),
            "placa_mae": Motherboard.get_info(),
            "interfaces": Interfaces.get_info(),
            "ips": IPAddress.get_info(),
            "gateway": Gateway.get_info(),
            "dns": DNS.get_info(),
            "portas": Ports.get_info(),
            "sistema_operacional": OSInfo.get_info(),
            "processos": ProcessList.get_info(limit=300),
            "resumo_processos": ProcessList.resumo()
        }

    @classmethod
    def gerar_nome_arquivo(cls, extensao: str) -> str:

        hostname = socket.gethostname()

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H%M%S"
        )

        return f"{hostname}_{timestamp}.{extensao}"

    @classmethod
    def exportar_json(cls) -> str:

        cls.REPORT_DIR.mkdir(
            exist_ok=True
        )

        dados = cls.coletar_dados()

        arquivo = (
            cls.REPORT_DIR /
            cls.gerar_nome_arquivo("json")
        )

        with open(
            arquivo,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                dados,
                f,
                indent=4,
                ensure_ascii=False
            )

        return str(arquivo)

    @classmethod
    def exportar_txt(cls) -> str:

        cls.REPORT_DIR.mkdir(
            exist_ok=True
        )

        dados = cls.coletar_dados()

        arquivo = (
            cls.REPORT_DIR /
            cls.gerar_nome_arquivo("txt")
        )

        with open(
            arquivo,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                cls._formatar_txt(
                    dados
                )
            )

        return str(arquivo)

    @classmethod
    def _formatar_txt(
        cls,
        dados: dict
    ) -> str:

        linhas = []

        linhas.append("=" * 70)
        linhas.append("DIAG-DB")
        linhas.append("RELATÓRIO DE DIAGNÓSTICO")
        linhas.append("=" * 70)
        linhas.append("")

        for secao, conteudo in dados.items():

            linhas.append(
                f"[ {secao.upper()} ]"
            )

            linhas.append(
                "-" * 50
            )

            if isinstance(
                conteudo,
                dict
            ):

                linhas.extend(
                    tabulate.tabulate(
                        [[chave, valor] for chave, valor in conteudo.items()],
                        headers=["Campo", "Valor"],
                        tablefmt="github"
                    ).splitlines()
                )

            elif isinstance(
                conteudo,
                list
            ):

                if conteudo and isinstance(conteudo[0], dict):
                    headers = list(conteudo[0].keys())
                    linhas.extend(
                        tabulate.tabulate(
                            [
                                [item.get(chave, "") for chave in headers]
                                for item in conteudo
                            ],
                            headers=headers,
                            tablefmt="github"
                        ).splitlines()
                    )
                else:
                    for item in conteudo:

                        linhas.append(
                            str(item)
                        )

            else:

                linhas.append(
                    str(conteudo)
                )

            linhas.append("")
            linhas.append("")

        return "\n".join(linhas)