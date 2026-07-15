import psutil
import tabulate


class Ports:

    @staticmethod
    def get_info() -> str:

        linhas = []

        try:

            conexoes = psutil.net_connections()

            for conexao in conexoes:

                if conexao.status != "LISTEN":
                    continue

                porta = None

                if conexao.laddr:
                    porta = conexao.laddr.port

                pid = conexao.pid

                processo = "Desconhecido"

                if pid:

                    try:
                        processo = psutil.Process(pid).name()
                    except Exception:
                        pass

                linhas.append([porta, pid, processo])

        except Exception as erro:

            linhas.append(["Erro", "-", str(erro)])

        linhas = sorted(
            linhas,
            key=lambda x: x[0] or 0
        )

        return tabulate.tabulate(
            linhas[:100],
            headers=["Porta", "PID", "Processo"],
            tablefmt="grid"
        )