import platform

import tabulate

import cpuinfo
import psutil

info = cpuinfo.get_cpu_info()

class CPU:

    @staticmethod
    def get_info() -> str:
        tabela = [
            ["Fabricante", info.get("vendor_id_raw", "Desconhecido")],
            ["Modelo", info.get("brand_raw", "Desconhecido")],
            ["Frequência", psutil.cpu_freq().current],
            ["Núcleos", psutil.cpu_count(logical=False)],
            ["Threads", psutil.cpu_count(logical=True)],
            ["Uso", psutil.cpu_percent(interval=1)]
        ]

        try:
            return tabulate.tabulate(tabela, headers="firstrow", tablefmt="grid")
        except Exception as erro:

            return {"erro": str(erro)}