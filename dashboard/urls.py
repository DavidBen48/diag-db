from django.urls import path

from .views import (
    index,
    hardware_view,
    network_view,
    system_view,
    processes_view,
    relatorios_view,
    download_relatorio
)


urlpatterns = [

    path(
        "",
        index,
        name="index"
    ),

    path(
        "hardware/",
        hardware_view,
        name="hardware"
    ),

    path(
        "network/",
        network_view,
        name="network"
    ),

    path(
        "system/",
        system_view,
        name="system"
    ),

    path(
        "processes/",
        processes_view,
        name="processes"
    ),

    path(
        "relatorios/",
        relatorios_view,
        name="relatorios"
    ),

    path(
        "relatorios/download/<str:nome_arquivo>",
        download_relatorio,
        name="download_relatorio"
    )

]