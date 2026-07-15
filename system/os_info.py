import platform
import socket
from datetime import datetime

import psutil
import tabulate


class OSInfo:

    @staticmethod
    def get_info() -> str:

        try:

            boot_timestamp = psutil.boot_time()

            boot_datetime = datetime.fromtimestamp(
                boot_timestamp
            )

            agora = datetime.now()

            uptime = agora - boot_datetime

            dias = uptime.days

            horas, resto = divmod(
                uptime.seconds,
                3600
            )

            minutos, segundos = divmod(
                resto,
                60
            )

            dados = [
                ["Hostname", socket.gethostname()],
                ["Sistema", platform.system()],
                ["Versão", platform.version()],
                ["Release", platform.release()],
                ["Build", platform.platform()],
                ["Arquitetura", platform.machine()],
                ["Processador", platform.processor()],
                ["Usuário logado", OSInfo._usuario_logado()],
                ["Boot time", boot_datetime.strftime("%d/%m/%Y %H:%M:%S")],
                ["Uptime", f"{dias}d {horas}h {minutos}m {segundos}s"]
            ]

            return tabulate.tabulate(
                dados,
                headers=["Campo", "Valor"],
                tablefmt="grid"
            )

        except Exception as erro:

            return tabulate.tabulate(
                [["Erro", str(erro)]],
                headers=["Campo", "Valor"],
                tablefmt="grid"
            )

    @staticmethod
    def _usuario_logado():

        try:
            return psutil.users()[0].name

        except Exception:
            return "Não identificado"