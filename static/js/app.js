document.addEventListener(
    "DOMContentLoaded",
    function () {

        const input = document.getElementById("procSearch");
        const resultado = document.getElementById("procResult");

        if (!input || !resultado) {
            return;
        }

        const atualizarBusca = () => {
            const filtro = input.value.trim().toLowerCase();
            const linhas = document.querySelectorAll("#processTable tbody tr");
            let visiveis = 0;

            linhas.forEach((linha) => {
                const texto = linha.innerText.toLowerCase();
                const corresponde = texto.includes(filtro);
                linha.style.display = corresponde ? "" : "none";
                if (corresponde) {
                    visiveis += 1;
                }
            });

            if (!filtro) {
                resultado.textContent = "Digite para filtrar os processos.";
            } else if (visiveis === 0) {
                resultado.textContent = "Nenhum processo encontrado.";
            } else {
                resultado.textContent = `${visiveis} processo(s) encontrado(s).`;
            }
        };

        input.addEventListener("input", atualizarBusca);
        atualizarBusca();
    }
);