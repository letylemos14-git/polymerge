import sys
import os
import heapq
import math
from collections import deque


class Registro:
    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, other):
        return self.valor < other.valor


def abrir_arquivo_leitura(nome):
    return open(nome, "r")


def abrir_arquivo_escrita(nome):
    return open(nome, "w")


def gerar_sequencias_iniciais(m, arquivo_entrada):
    heap = []
    congelados = []
    arquivos_seq = []

    total_registros = 0
    processamentos = 0

    entrada = abrir_arquivo_leitura(arquivo_entrada)

    for _ in range(m - 1):
        linha = entrada.readline()
        if not linha:
            break
        heapq.heappush(heap, Registro(int(linha.strip())))
        total_registros += 1
        processamentos += 1

    seq_atual = 0
    ultimo_valor = -math.inf

    while heap:
        registro = heapq.heappop(heap)
        processamentos += 1

        if registro.valor < ultimo_valor:
            seq_atual += 1
            ultimo_valor = -math.inf

        if seq_atual == len(arquivos_seq):
            arquivos_seq.append(
                abrir_arquivo_escrita(f"seq_0_{seq_atual}.txt")
            )

        arquivos_seq[seq_atual].write(f"{registro.valor}\n")
        ultimo_valor = registro.valor

        linha = entrada.readline()
        if linha:
            linha = linha.strip()
            if not linha:
                continue
            valor = int(linha)

            total_registros += 1
            processamentos += 1

            if valor >= ultimo_valor:
                heapq.heappush(heap, Registro(valor))
            else:
                congelados.append(Registro(valor))

        if not heap and congelados:
            heap = congelados
            heapq.heapify(heap)
            congelados = []
            ultimo_valor = -math.inf
            seq_atual += 1

    entrada.close()
    for arq in arquivos_seq:
        arq.close()

    return seq_atual + 1, processamentos, total_registros


def intercalar(m, fase, sequencias):
    fila = deque(sequencias)
    novas_sequencias = []
    processamentos = 0
    indice_saida = 0

    while len(fila) > 1:
        entradas = [
            abrir_arquivo_leitura(fila.popleft())
            for _ in range(min(m - 1, len(fila)))
        ]

        nome_saida = f"seq_{fase}_{indice_saida}.txt"
        saida = abrir_arquivo_escrita(nome_saida)
        heap = []

        for i, arq in enumerate(entradas):
            linha = arq.readline()
            if linha:
                linha = linha.strip()
                if not linha:
                    continue
                heapq.heappush(heap, (int(linha), i))
                processamentos += 1
        while heap:
            valor, idx = heapq.heappop(heap)
            processamentos += 1
            saida.write(f"{valor}\n")

            linha = entradas[idx].readline()
            if linha:
                linha = linha.strip()
                if not linha:
                    continue
                heapq.heappush(heap, (int(linha), idx))
                processamentos += 1

        for arq in entradas:
            arq.close()
        saida.close()

        novas_sequencias.append(nome_saida)
        indice_saida += 1

    return novas_sequencias, processamentos


def limpar_arquivos_temporarios(arquivo_final):
    for nome in os.listdir():
        if nome.startswith("seq_") and nome != arquivo_final:
            try:
                os.remove(nome)
            except:
                pass


def main():
    if len(sys.argv) != 4:
        print("Uso: polymerge m input.txt output.txt")
        sys.exit(1)

    m = int(sys.argv[1])
    entrada = sys.argv[2]
    saida_final = sys.argv[3]

    if m < 3:
        print("Erro: m deve ser >= 3")
        sys.exit(1)

    total_processamentos = 0
    historico_seq = []

    qtd_seq, proc, total_registros = gerar_sequencias_iniciais(m, entrada)
    total_processamentos += proc
    historico_seq.append(qtd_seq)

    sequencias = [f"seq_0_{i}.txt" for i in range(qtd_seq)]
    fase = 1

    while len(sequencias) > 1:
        sequencias, proc = intercalar(m, fase, sequencias)
        total_processamentos += proc
        historico_seq.append(len(sequencias))
        fase += 1

    os.rename(sequencias[0], saida_final)
    limpar_arquivos_temporarios(saida_final)

    print("#seq", " ".join(map(str, historico_seq)))
    print(f"tx {total_processamentos / total_registros:.1f}")


if __name__ == "__main__":
    main()
