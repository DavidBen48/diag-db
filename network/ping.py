import platform
import re
import subprocess
import tabulate


class Ping:
    @staticmethod
    def executar(destino: str) -> str:
        try:
            sistema = platform.system()
            if sistema == "Windows":
                comando = ["ping", "-n", "4", destino]

            else:
                comando = ["ping", "-c", "4", destino]

            resultado = subprocess.run(comando, capture_output=True, text=True)
            saida = resultado.stdout

            return tabulate.tabulate(
                [
                    ["Destino", destino],
                    ["Sucesso", "Sim" if resultado.returncode == 0 else "Não"],
                    ["Latência média", Ping._extrair_latencia(saida)],
                    ["Perda de pacotes", Ping._extrair_perda(saida)]
                ],
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
    def ping_google() -> str:

        return Ping.executar("8.8.8.8")

    @staticmethod
    def _extrair_latencia(texto):
        try:
            numeros = re.findall(r"(\d+)ms", texto)
            if not numeros:
                return "Indisponível"

            valores = [int(x) for x in numeros]
            media = sum(valores) / len(valores)

            return f"{media:.2f} ms"

        except Exception:
            return "Indisponível"

    @staticmethod
    def _extrair_perda(texto):
        try:
            if "%" in texto:
                match = re.search(
                    r"(\d+)%.*perd",
                    texto,
                    re.IGNORECASE
                )
                if match:
                    return f"{match.group(1)}%"

        except Exception:
            pass

        return "Indisponível"