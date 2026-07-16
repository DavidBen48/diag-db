# DIAG-DB

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Django](https://img.shields.io/badge/Django-5.x-green) ![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey) ![License](https://img.shields.io/badge/License-Em%20defini%C3%A7%C3%A3o-yellow)

DIAG-DB é uma aplicação local de diagnóstico de sistema desenvolvida em Python, com foco em reunir informações úteis sobre hardware, rede, sistema operacional, processos e gerar relatórios em formatos estruturados. O projeto oferece duas interfaces principais: uma linha de comando interativa e uma dashboard web baseada em Django.

## Visão Geral

O objetivo do projeto é fornecer uma visão rápida e organizada do ambiente local do computador, permitindo:

- consultar detalhes de hardware e configuração do sistema;
- inspecionar informações de rede, IPs, gateway, DNS e portas;
- visualizar processos em execução;
- exportar relatórios em TXT ou JSON para análise posterior.

A aplicação foi pensada para uso local e offline, sem depender de serviços externos para coleta das informações.

## Funcionalidades Principais

- Dashboard web com navegação por páginas temáticas;
- Menu interativo em terminal para diagnóstico rápido;
- Coleta de dados de:
  - equipamento;
  - CPU;
  - memória;
  - BIOS;
  - discos;
  - placa-mãe;
  - interfaces de rede;
  - IPs e gateway;
  - DNS;
  - portas;
  - sistema operacional;
  - processos;
- Exportação de relatórios em TXT e JSON;
- Armazenamento dos relatórios gerados na pasta relatorios/.

## Stack Tecnológica

- Python 3.10+
- Django 5.x
- psutil
- py-cpuinfo
- WMI
- tabulate
- pyinstaller

## Estrutura do Projeto

- cli/: interface de linha de comando;
- dashboard/: views, URLs e lógica da aplicação web;
- hardware/: coleta de dados de hardware;
- network/: coleta de dados de rede;
- processes/: listagem e resumo de processos;
- reports/: geração de relatórios;
- system/: informações do sistema operacional;
- templates/ e static/: interface web;
- utils/: funções auxiliares e utilidades gerais.

## Capturas de Tela

A interface web possui uma estética voltada para diagnóstico técnico e visualização rápida de informações. Futuras capturas podem ser adicionadas aqui para ilustrar:

- dashboard inicial;
- páginas de hardware e rede;
- tela de relatórios exportados.

Exemplo de espaço para imagem:

```md
![Dashboard DIAG-DB](docs/screenshots/dashboard.png)
```

## Requisitos

- Python 3.10 ou superior;
- pip atualizado;
- Ambiente Windows recomendado para pleno funcionamento, especialmente pela integração com WMI e informações do sistema.

## Instalação

1. Acesse a pasta do projeto:

```bash
cd diag-db
```

2. Crie um ambiente virtual:

```bash
python -m venv .venv
```

3. Ative o ambiente virtual:

No PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

### Interface de linha de comando

Execute:

```bash
python main.py
```

O menu permitirá acessar as seções de hardware, rede, sistema, processos e relatórios.

### Interface web

Inicie o servidor Django:

```bash
python manage.py runserver 0.0.0.0:8000
```

Depois abra no navegador:

```text
http://127.0.0.1:8000/
```

## Geração de Relatórios

Na interface web ou no menu de terminal, é possível gerar relatórios em:

- TXT: ideal para leitura humana;
- JSON: ideal para integração ou processamento automatizado.

Os arquivos são salvos na pasta relatorios/ com nome baseado no hostname e data/hora.

## Exemplos de Saída

### Exemplo de saída no terminal

```text
[1] Hardware
[2] Network
[3] Sistema Operacional
[4] Processos
[5] Relatórios
[6] Web
[0] Sair
```

### Exemplo de conteúdo de relatório

```text
[ EQUIPAMENTO ]
Fabricante: Dell
Modelo: Latitude 7420

[ CPU ]
Fabricante: GenuineIntel
Modelo: Intel Core i7
```

### Exemplo de JSON gerado

```json
{
  "equipamento": {
    "Fabricante": "Dell",
    "Modelo": "Latitude 7420"
  },
  "cpu": {
    "Fabricante": "GenuineIntel",
    "Modelo": "Intel Core i7"
  }
}
```

## Como Usar

1. Execute a aplicação;
2. Escolha a seção desejada;
3. Consulte os dados coletados;
4. Gere relatórios quando necessário.

## Observações

- Algumas informações podem depender de permissões do sistema operacional e da disponibilidade de recursos do ambiente;
- O projeto foi desenvolvido com foco em diagnóstico local e não envia dados para servidores externos;
- A interface web é destinada principalmente para uso local em desenvolvimento ou ambientes internos.

## Contribuição

Contribuições são bem-vindas. Para participar do projeto:

1. faça um fork;
2. crie uma branch para sua alteração;
3. envie um pull request com descrição clara das mudanças.

## Licença

Nenhuma licença foi definida até o momento.
