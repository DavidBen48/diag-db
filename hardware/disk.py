import psutil
import tabulate


class Disk:

    @staticmethod
    def get_info() -> str:

        try:
            gb = 1024 ** 3
            saida = []

            for indice, particao in enumerate(psutil.disk_partitions(), start=1):
                try:

                    uso = psutil.disk_usage(particao.mountpoint)

                    tabela = [
                        ["Campo", "Valor"],
                        ["Dispositivo", particao.device],
                        ["Ponto de Montagem", particao.mountpoint],
                        ["Tipo", particao.fstype],
                        ["Capacidade (GB)", round(uso.total / gb, 2)],
                        ["Utilizado (GB)", round(uso.used / gb, 2)],
                        ["Livre (GB)", round(uso.free / gb, 2)],
                        ["Uso (%)", f"{uso.percent}%"]
                    ]

                    saida.append(f"Disco {indice}")
                    saida.append(
                        tabulate.tabulate(
                            tabela,
                            headers="firstrow",
                            tablefmt="grid"
                        )
                    )

                except Exception:
                    continue

            if not saida:
                return "Nenhum disco encontrado."

            return "\n\n".join(saida)

        except Exception as erro:
            return {"erro": str(erro)}