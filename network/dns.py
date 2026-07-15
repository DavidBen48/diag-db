import platform
import re
import tabulate


class DNS:

    @staticmethod
    def get_info() -> str:

        try:
            sistema = platform.system()

            if sistema == "Windows":

                return DNS._windows_dns()

            elif sistema == "Linux":

                return DNS._linux_dns()

        except Exception as erro:

            return tabulate.tabulate(
                [["Erro", str(erro)]],
                headers=["Campo", "Valor"],
                tablefmt="grid"
            )

        return tabulate.tabulate(
            [["DNS", "Não encontrado"]],
            headers=["Campo", "Valor"],
            tablefmt="grid"
        )

    @staticmethod
    def _windows_dns() -> str:

        import subprocess

        saida = subprocess.check_output(
            "ipconfig /all",
            shell=True,
            text=True,
            errors="ignore"
        )

        dns_encontrados = []

        regex = r"(\d+\.\d+\.\d+\.\d+)"

        for linha in saida.splitlines():

            if "DNS" in linha.upper():

                ips = re.findall(regex, linha)

                dns_encontrados.extend(ips)

        dns = sorted(set(dns_encontrados))

        if not dns:
            return tabulate.tabulate(
                [["DNS", "Não encontrado"]],
                headers=["Campo", "Valor"],
                tablefmt="grid"
            )

        return tabulate.tabulate(
            [["DNS", ip] for ip in dns],
            headers=["Campo", "Valor"],
            tablefmt="grid"
        )

    @staticmethod
    def _linux_dns() -> str:

        dns = []

        with open("/etc/resolv.conf", "r") as arquivo:

            for linha in arquivo:

                if linha.startswith("nameserver"):

                    dns.append(
                        linha.split()[1]
                    )

        if not dns:
            return tabulate.tabulate(
                [["DNS", "Não encontrado"]],
                headers=["Campo", "Valor"],
                tablefmt="grid"
            )

        return tabulate.tabulate(
            [["DNS", ip] for ip in dns],
            headers=["Campo", "Valor"],
            tablefmt="grid"
        )