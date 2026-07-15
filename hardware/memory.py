import psutil

import tabulate

class Memory:

    @staticmethod
    def get_info() -> str:

        memoria = psutil.virtual_memory()

        gb = 1024 ** 3

        tabela = [
            ["Capacidade Total", round(memoria.total / gb, 2)],
            ["Capacidade Utilizada", round(memoria.used / gb, 2)],
            ["Capacidade Livre", round(memoria.available / gb, 2)],
            ["Uso (%)", f'{memoria.percent}%']
        ]

        return tabulate.tabulate(tabela, headers="firstrow", tablefmt="grid")