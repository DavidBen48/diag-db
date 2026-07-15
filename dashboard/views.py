from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from pathlib import Path

from utils.helpers import parse_display_data

from hardware.equipment import Equipment
from hardware.cpu import CPU
from hardware.memory import Memory
from hardware.bios import BIOS
from hardware.disk import Disk
from hardware.motherboard import Motherboard

from network.interfaces import Interfaces
from network.ip import IPAddress
from network.gateway import Gateway
from network.dns import DNS
from network.ports import Ports

from system.os_info import OSInfo

from processes.process_list import ProcessList

from reports.exporter import ReportExporter


def index(request):

    equipamento = Equipment.get_info()
    cpu = CPU.get_info()
    memoria = Memory.get_info()
    sistema = OSInfo.get_info()

    context = {
        "equipamento": parse_display_data(equipamento),
        "cpu": parse_display_data(cpu),
        "memoria": parse_display_data(memoria),
        "sistema": parse_display_data(sistema),
    }

    return render(
        request,
        "index.html",
        context
    )


def hardware_view(request):

    context = {

        "equipamento":
            parse_display_data(Equipment.get_info()),

        "cpu":
            parse_display_data(CPU.get_info()),

        "memoria":
            parse_display_data(Memory.get_info()),

        "bios":
            parse_display_data(BIOS.get_info()),

        "discos":
            parse_display_data(Disk.get_info()),

        "placa_mae":
            parse_display_data(Motherboard.get_info())

    }

    return render(
        request,
        "hardware.html",
        context
    )


def network_view(request):

    context = {

        "interfaces":
            parse_display_data(Interfaces.get_info()),

        "ips":
            parse_display_data(IPAddress.get_info()),

        "gateway":
            parse_display_data(Gateway.get_info()),

        "dns":
            parse_display_data(DNS.get_info()),

        "portas":
            parse_display_data(Ports.get_info())

    }

    return render(
        request,
        "network.html",
        context
    )


def system_view(request):

    return render(
        request,
        "system.html",
        {
            "sistema":
                parse_display_data(OSInfo.get_info())
        }
    )


def processes_view(request):

    context = {

        "resumo":
            ProcessList.resumo(),

        "processos":
            ProcessList.get_info(
                limit=300
            )

    }

    return render(
        request,
        "processes.html",
        context
    )


@require_http_methods(["GET", "POST"])
def relatorios_view(request):

    if request.method == "POST":
        formato = request.POST.get("formato", "txt")
        
        try:
            if formato == "json":
                arquivo = ReportExporter.exportar_json()
            else:
                arquivo = ReportExporter.exportar_txt()
            
            return JsonResponse({
                "sucesso": True,
                "arquivo": arquivo,
                "nome": Path(arquivo).name
            })
        except Exception as erro:
            return JsonResponse({
                "sucesso": False,
                "erro": str(erro)
            }, status=500)

    relatorios = []
    relatorio_dir = Path("relatorios")
    
    if relatorio_dir.exists():
        for arquivo in sorted(relatorio_dir.glob("*"), reverse=True):
            if arquivo.is_file():
                relatorios.append({
                    "nome": arquivo.name,
                    "tamanho": arquivo.stat().st_size,
                    "data": arquivo.stat().st_mtime
                })

    return render(
        request,
        "relatorios.html",
        {"relatorios": relatorios}
    )


@require_http_methods(["GET"])
def download_relatorio(request, nome_arquivo):

    relatorio_dir = Path("relatorios")
    arquivo = relatorio_dir / nome_arquivo

    if not arquivo.exists() or not arquivo.is_file():
        return JsonResponse({
            "erro": "Arquivo não encontrado"
        }, status=404)

    if not str(arquivo.resolve()).startswith(str(relatorio_dir.resolve())):
        return JsonResponse({
            "erro": "Acesso negado"
        }, status=403)

    return FileResponse(
        open(arquivo, "rb"),
        as_attachment=True,
        filename=arquivo.name
    )