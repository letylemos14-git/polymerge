import sys
import os
import heapq
import math

menor = -math.inf


def gerar_sequencias_iniciais(m, entrada_nome):
    k = m - 1
    fitas = [open(f"F{i}.txt", "w") for i in range(k)]
    entrada = open(entrada_nome, "r")

    heap = []
    congelados = []

    proc = 0
    total = 0


    for _ in range(k):
        linha = entrada.readline()
        if not linha:
            break
        heapq.heappush(heap, int(linha.strip()))
        proc += 1
        total += 1

    fita_atual = 0
    ultimo = menor
    seq_por_fita = [0] * m
    seq_por_fita[fita_atual] = 1

    while heap:
        valor = heapq.heappop(heap)
        proc += 1

        if valor < ultimo:
            fitas[fita_atual].write("\n")
            fita_atual = (fita_atual + 1) % k
            seq_por_fita[fita_atual] += 1
            ultimo = menor

        fitas[fita_atual].write(f"{valor}\n")
        proc += 1
        ultimo = valor

        linha = entrada.readline()
        if linha:
            v = int(linha.strip())
            proc += 1
            total += 1
            if v >= ultimo:
                heapq.heappush(heap, v)
            else:
                congelados.append(v)

        if not heap and congelados:
            heap = congelados
            heapq.heapify(heap)
            congelados = []
            fitas[fita_atual].write("\n")
            fita_atual = (fita_atual + 1) % k
            seq_por_fita[fita_atual] += 1
            ultimo = menor

    entrada.close()
    for f in fitas:
        f.close()

    return seq_por_fita, proc, total


def intercalar_polifasico(m, seq_por_fita):
    fitas = [f"F{i}.txt" for i in range(m)]
    proc = 0
    fases = []
    
    while max(seq_por_fita) > 1:
        saida = seq_por_fita.index(0)
        entradas = [i for i in range(m) if i != saida and seq_por_fita[i] > 0]

        runs = min(seq_por_fita[i] for i in entradas)
        fases.append(runs)

        arqs_in = [open(fitas[i], "r") for i in entradas]
        arq_out = open(fitas[saida], "w")

        for _ in range(runs):
            heap = []

            for idx, arq in enumerate(arqs_in):
                linha = arq.readline()
                if linha and linha.strip() != "":
                    heapq.heappush(heap, (int(linha.strip()), idx))
                    proc += 1

            while heap:
                valor, idx = heapq.heappop(heap)
                arq_out.write(f"{valor}\n")
                proc += 1

                linha = arqs_in[idx].readline()
                if linha and linha.strip() != "":
                    heapq.heappush(heap, (int(linha.strip()), idx))
                    proc += 1

            arq_out.write("\n")

        seq_por_fita[saida] = runs
        for i in entradas:
            seq_por_fita[i] -= runs

        for arq in arqs_in:
            arq.close()
        arq_out.close()

    fita_final = seq_por_fita.index(max(seq_por_fita))
    return fitas[fita_final], proc, fases


def main():
    if len(sys.argv) != 4:
        print("Uso: polymerge m entrada.txt saida.txt")
        sys.exit(1)

    m = int(sys.argv[1])
    entrada = sys.argv[2]
    saida = sys.argv[3]

    if m < 3:
        print("Erro: m deve ser >= 3")
        sys.exit(1)

    seq_por_fita, p1, total = gerar_sequencias_iniciais(m, entrada)

    if total == 0:
        print("Arquivo vazio.")
        sys.exit(0)

    fita_final, p2, fases = intercalar_polifasico(m, seq_por_fita)

    if os.path.exists(saida):
        os.remove(saida)
    os.rename(fita_final, saida)

    for f in os.listdir():
        if f.startswith("F") and f != saida:
            os.remove(f)

    print("#seq", *fases)
    print(f"tx {(p1 + p2) / total:.1f}")


if __name__ == "__main__":
    main()
