import os
import socket
import subprocess
import webbrowser
from pathlib import Path


class WebLauncher:

    HOST = "127.0.0.1"
    PORT = 1277

    django_process = None

    @classmethod
    def servidor_ativo(cls) -> bool:
        try:
            with socket.create_connection(
                (cls.HOST, cls.PORT),
                timeout=1
            ):
                return True
        except Exception:
            return False

    @classmethod
    def iniciar_servidor(cls) -> bool:

        if cls.servidor_ativo():
            return True

        projeto = Path.cwd()

        manage = projeto / "manage.py"

        if not manage.exists():
            print("\nmanage.py não encontrado.\n")
            return False

        try:

            comando = [
                "python",
                str(manage),
                "runserver",
                f"{cls.HOST}:{cls.PORT}"
            ]

            cls.django_process = subprocess.Popen(
                comando,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            return True

        except Exception as erro:
            print(f"\nErro ao iniciar Django: {erro}\n")
            return False

    @classmethod
    def abrir_web(cls):

        url = f"http://{cls.HOST}:{cls.PORT}"

        if cls.servidor_ativo():

            print()
            print("=" * 40)
            print("INTERFACE WEB JÁ ESTÁ ATIVA")
            print("=" * 40)
            print(url)
            print()

            opcao = input("[S] Sim | [N] Não: ").strip().upper()

            if opcao == "S":
                webbrowser.open(url)

            return

        iniciado = cls.iniciar_servidor()

        if not iniciado:
            return

        try:

            webbrowser.open(url)

            print()
            print("=" * 40)
            print("INTERFACE WEB INICIADA")
            print("=" * 40)
            print(url)
            print()

        except Exception:

            print()
            print("=" * 40)
            print("INTERFACE WEB INICIADA")
            print("=" * 40)
            print()
            print("Acesse:")
            print(url)
            print()

            input("Pressione ENTER para retornar.")

    @classmethod
    def encerrar_servidor(cls):

        if cls.django_process:

            try:
                cls.django_process.terminate()
                cls.django_process.wait(timeout=5)

            except Exception:
                pass