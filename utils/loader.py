import time


class Loader:

    @staticmethod
    def executar():
        etapas = [0, 12, 28, 51, 83, 100]

        inicio = time.time()

        for porcentagem in etapas:
            decorrido = time.time() - inicio
            print(f"{porcentagem}% | {decorrido:.1f}s")
            time.sleep(0.3)

        total = time.time() - inicio

        print()
        print(f"Tempo total da coleta: {total:.2f}s")
        print()