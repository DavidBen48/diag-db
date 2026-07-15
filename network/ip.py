import psutil
import socket
import tabulate


class IPAddress:

    @staticmethod
    def get_info() -> str:

        linhas = []

        try:

            interfaces = psutil.net_if_addrs()

            for interface, enderecos in interfaces.items():

                ipv4 = []
                ipv6 = []

                for endereco in enderecos:

                    if endereco.family == socket.AF_INET:
                        ipv4.append(endereco.address)

                    elif endereco.family == socket.AF_INET6:
                        ipv6.append(endereco.address)

                linhas.append([
                    interface,
                    ", ".join(ipv4) or "Não encontrado",
                    ", ".join(ipv6) or "Não encontrado"
                ])

        except Exception as erro:

            linhas.append([
                "Erro",
                str(erro),
                "-"
            ])

        return tabulate.tabulate(
            linhas,
            headers=["Interface", "IPv4", "IPv6"],
            tablefmt="grid"
        )