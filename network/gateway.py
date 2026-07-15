import platform
import subprocess
import tabulate


class Gateway:

    @staticmethod
    def get_info() -> str:

        try:

            sistema = platform.system()

            if sistema == "Windows":

                saida = subprocess.check_output(
                    "route print 0.0.0.0",
                    shell=True,
                    text=True,
                    errors="ignore"
                )

                linhas = saida.splitlines()

                for linha in linhas:

                    if "0.0.0.0" in linha:

                        partes = linha.split()

                        if len(partes) >= 3:

                            return tabulate.tabulate(
                                [["Gateway", partes[2]]],
                                headers=["Campo", "Valor"],
                                tablefmt="grid"
                            )

            elif sistema == "Linux":

                saida = subprocess.check_output(
                    "ip route",
                    shell=True,
                    text=True
                )

                linhas = saida.splitlines()

                for linha in linhas:

                    if linha.startswith("default"):

                        return tabulate.tabulate(
                            [["Gateway", linha.split()[2]]],
                            headers=["Campo", "Valor"],
                            tablefmt="grid"
                        )

        except Exception as erro:

            return tabulate.tabulate(
                [["Erro", str(erro)]],
                headers=["Campo", "Valor"],
                tablefmt="grid"
            )

        return tabulate.tabulate(
            [["Gateway", "Não encontrado"]],
            headers=["Campo", "Valor"],
            tablefmt="grid"
        )