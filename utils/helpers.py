import os
import re


def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pausar() -> None:
    input("\nPressione ENTER para continuar...")


def cabecalho(titulo: str) -> None:
    print("=" * 45)
    print(titulo)
    print("=" * 45)


def parse_wmic_saida(saida: str) -> str | None:
    """Extrai o valor de uma consulta WMIC ignorando linhas vazias."""
    linhas = [
        linha.strip()
        for linha in saida.splitlines()
        if linha.strip()
    ]

    if len(linhas) >= 2:
        return linhas[1]

    return None


def parse_display_data(dados) -> dict:
    """Converte saídas tabulares em uma estrutura legível para templates web."""
    if isinstance(dados, dict):
        return {
            "kind": "table",
            "headers": ["Campo", "Valor"],
            "rows": [[chave, valor] for chave, valor in dados.items()]
        }

    if isinstance(dados, list):
        if dados and isinstance(dados[0], dict):
            return {
                "kind": "table",
                "headers": list(dados[0].keys()),
                "rows": [
                    [item.get(chave, "") for chave in dados[0].keys()]
                    for item in dados
                ],
            }

        return {
            "kind": "text",
            "text": "\n".join(str(item) for item in dados),
        }

    if not isinstance(dados, str):
        return {"kind": "text", "text": str(dados)}

    texto = dados.strip()
    if not texto:
        return {"kind": "text", "text": ""}

    linhas = [linha.rstrip() for linha in texto.splitlines() if linha.strip()]

    if not linhas:
        return {"kind": "text", "text": ""}

    if any(re.match(r"^Disco\s+\d+$", linha) for linha in linhas):
        secoes = []
        atual = None
        linhas_secoes = []

        for linha in linhas:
            if re.match(r"^Disco\s+\d+$", linha):
                if atual is not None:
                    secoes.append({"title": atual, "rows": parse_display_data("\n".join(linhas_secoes))})
                atual = linha
                linhas_secoes = []
            else:
                linhas_secoes.append(linha)

        if atual is not None:
            secoes.append({"title": atual, "rows": parse_display_data("\n".join(linhas_secoes))})

        return {"kind": "sections", "sections": secoes}

    celulas_por_linha = []
    for linha in linhas:
        if "|" not in linha:
            continue
        if linha.startswith("+") or linha.startswith("=") or linha.startswith("-"):
            continue
        partes = [parte.strip() for parte in linha.strip().strip("|").split("|")]
        partes = [parte for parte in partes if parte]
        if partes:
            celulas_por_linha.append(partes)

    if not celulas_por_linha:
        return {"kind": "text", "text": texto}

    if len(celulas_por_linha[0]) == 2 and all(len(linha) == 2 for linha in celulas_por_linha):
        # Remover primeira linha se for duplicata de headers "Campo" / "Valor"
        if celulas_por_linha[0][0].lower() == "campo" and celulas_por_linha[0][1].lower() == "valor":
            celulas_por_linha = celulas_por_linha[1:]
        
        if not celulas_por_linha:
            return {"kind": "text", "text": ""}
        
        return {
            "kind": "table",
            "headers": ["Campo", "Valor"],
            "rows": [[linha[0], linha[1]] for linha in celulas_por_linha]
        }

    if len(celulas_por_linha[0]) > 2 and len(celulas_por_linha) >= 2:
        return {
            "kind": "table",
            "headers": celulas_por_linha[0],
            "rows": celulas_por_linha[1:],
        }

    return {"kind": "text", "text": texto}