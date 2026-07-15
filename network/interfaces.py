import psutil
import tabulate


class Interfaces:

    @staticmethod
    def get_info() -> str:

        linhas = []

        try:

            interfaces = psutil.net_if_stats()

            for nome, dados in interfaces.items():

                linhas.append([
                    nome,
                    "UP" if dados.isup else "DOWN",
                    dados.speed,
                    dados.mtu
                ])

        except Exception as erro:

            linhas.append([
                "Erro",
                str(erro),
                "-",
                "-"
            ])

        return tabulate.tabulate(
            linhas,
            headers=["Nome", "Status", "Velocidade (Mbps)", "MTU"],
            tablefmt="grid"
        )