from datetime import datetime

import psutil
import tabulate


class ProcessList:

    @staticmethod
    def resumo() -> dict:

        try:

            return {
                "total_processos": len(psutil.pids()),
                "cpu_global": round(
                    psutil.cpu_percent(interval=1),
                    2
                ),
                "memoria_global": round(
                    psutil.virtual_memory().percent,
                    2
                )
            }

        except Exception as erro:

            return {
                "erro": str(erro)
            }

    @staticmethod
    def resumo_formatado() -> str:

        try:

            dados = [
                ["Total de processos", len(psutil.pids())],
                ["CPU global", f"{round(psutil.cpu_percent(interval=1), 2)}%"],
                ["Memória global", f"{round(psutil.virtual_memory().percent, 2)}%"]
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
    def get_info(limit: int = 200) -> list:

        processos = []

        try:

            for proc in psutil.process_iter(
                [
                    "pid",
                    "name",
                    "username",
                    "cpu_percent",
                    "memory_percent",
                    "status",
                    "create_time"
                ]
            ):

                try:

                    info = proc.info

                    criado = "N/A"

                    if info.get("create_time"):

                        criado = datetime.fromtimestamp(
                            info["create_time"]
                        ).strftime(
                            "%d/%m/%Y %H:%M:%S"
                        )

                    processos.append(
                        {
                            "pid": info.get("pid"),
                            "nome": info.get("name"),
                            "usuario": info.get("username"),
                            "cpu_percent": round(
                                info.get("cpu_percent", 0.0),
                                2
                            ),
                            "memoria_percent": round(
                                info.get("memory_percent", 0.0),
                                2
                            ),
                            "status": info.get("status"),
                            "criado_em": criado
                        }
                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

        except Exception as erro:

            return [
                {
                    "erro": str(erro)
                }
            ]

        processos.sort(
            key=lambda x: x.get(
                "memoria_percent",
                0
            ),
            reverse=True
        )

        return processos[:limit]

    @staticmethod
    def get_info_formatado(limit: int = 200) -> str:

        linhas = []

        try:

            processos = []

            for proc in psutil.process_iter(
                [
                    "pid",
                    "name",
                    "username",
                    "cpu_percent",
                    "memory_percent",
                    "status",
                    "create_time"
                ]
            ):

                try:

                    info = proc.info

                    processos.append(
                        {
                            "pid": info.get("pid"),
                            "nome": info.get("name"),
                            "usuario": info.get("username"),
                            "cpu_percent": round(
                                info.get("cpu_percent", 0.0),
                                2
                            ),
                            "memoria_percent": round(
                                info.get("memory_percent", 0.0),
                                2
                            ),
                            "status": info.get("status")
                        }
                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

            processos.sort(
                key=lambda x: x.get(
                    "memoria_percent",
                    0
                ),
                reverse=True
            )

            for proc in processos[:limit]:
                linhas.append([
                    proc["pid"],
                    proc["nome"],
                    proc["usuario"] or "N/A",
                    proc["cpu_percent"],
                    proc["memoria_percent"],
                    proc["status"]
                ])

        except Exception as erro:
            linhas.append(["Erro", str(erro), "-", "-", "-", "-"])

        return tabulate.tabulate(
            linhas,
            headers=["PID", "Nome", "Usuário", "CPU%", "Memória%", "Status"],
            tablefmt="grid"
        )

    @staticmethod
    def get_top_cpu(limit: int = 20) -> list:

        processos = []

        try:

            for proc in psutil.process_iter():

                try:

                    processos.append(
                        {
                            "pid": proc.pid,
                            "nome": proc.name(),
                            "cpu_percent": proc.cpu_percent()
                        }
                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

            processos.sort(
                key=lambda x: x["cpu_percent"],
                reverse=True
            )

            return processos[:limit]

        except Exception as erro:

            return [
                {
                    "erro": str(erro)
                }
            ]

    @staticmethod
    def get_top_cpu_formatado(limit: int = 20) -> str:

        linhas = []

        try:

            processos = []

            for proc in psutil.process_iter():

                try:

                    processos.append(
                        {
                            "pid": proc.pid,
                            "nome": proc.name(),
                            "cpu_percent": proc.cpu_percent()
                        }
                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

            processos.sort(
                key=lambda x: x["cpu_percent"],
                reverse=True
            )

            for proc in processos[:limit]:
                linhas.append([
                    proc["pid"],
                    proc["nome"],
                    f"{proc['cpu_percent']:.2f}%"
                ])

        except Exception as erro:
            linhas.append(["Erro", str(erro), "-"])

        return tabulate.tabulate(
            linhas,
            headers=["PID", "Nome", "CPU%"],
            tablefmt="grid"
        )

    @staticmethod
    def get_top_memory(limit: int = 20) -> list:

        processos = []

        try:

            for proc in psutil.process_iter():

                try:

                    processos.append(
                        {
                            "pid": proc.pid,
                            "nome": proc.name(),
                            "memoria_percent": round(
                                proc.memory_percent(),
                                2
                            )
                        }
                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

            processos.sort(
                key=lambda x: x["memoria_percent"],
                reverse=True
            )

            return processos[:limit]

        except Exception as erro:

            return [
                {
                    "erro": str(erro)
                }
            ]

    @staticmethod
    def get_top_memory_formatado(limit: int = 20) -> str:

        linhas = []

        try:

            processos = []

            for proc in psutil.process_iter():

                try:

                    processos.append(
                        {
                            "pid": proc.pid,
                            "nome": proc.name(),
                            "memoria_percent": round(
                                proc.memory_percent(),
                                2
                            )
                        }
                    )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

            processos.sort(
                key=lambda x: x["memoria_percent"],
                reverse=True
            )

            for proc in processos[:limit]:
                linhas.append([
                    proc["pid"],
                    proc["nome"],
                    f"{proc['memoria_percent']:.2f}%"
                ])

        except Exception as erro:
            linhas.append(["Erro", str(erro), "-"])

        return tabulate.tabulate(
            linhas,
            headers=["PID", "Nome", "Memória%"],
            tablefmt="grid"
        )

    @staticmethod
    def buscar(nome: str) -> list:

        resultado = []

        try:

            termo = nome.lower()

            for proc in psutil.process_iter():

                try:

                    nome_proc = proc.name()

                    if termo in nome_proc.lower():

                        resultado.append(
                            {
                                "pid": proc.pid,
                                "nome": nome_proc,
                                "status": proc.status()
                            }
                        )

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

        except Exception as erro:

            return [
                {
                    "erro": str(erro)
                }
            ]

        return resultado

    @staticmethod
    def buscar_formatado(nome: str) -> str:

        linhas = []

        try:

            termo = nome.lower()

            for proc in psutil.process_iter():

                try:

                    nome_proc = proc.name()

                    if termo in nome_proc.lower():

                        linhas.append([
                            proc.pid,
                            nome_proc,
                            proc.status()
                        ])

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    continue

        except Exception as erro:
            linhas.append(["Erro", str(erro), "-"])

        return tabulate.tabulate(
            linhas,
            headers=["PID", "Nome", "Status"],
            tablefmt="grid"
        )

    @staticmethod
    def obter_por_pid(pid: int) -> dict:

        try:

            proc = psutil.Process(pid)

            return {
                "pid": proc.pid,
                "nome": proc.name(),
                "usuario": proc.username(),
                "cpu_percent": proc.cpu_percent(),
                "memoria_percent": round(
                    proc.memory_percent(),
                    2
                ),
                "status": proc.status(),
                "threads": proc.num_threads(),
                "executavel": proc.exe(),
                "diretorio": proc.cwd()
            }

        except Exception as erro:

            return {
                "erro": str(erro)
            }