
# mata54-trab-2025-2 - polymerge

## 1. Objetivo

Este trabalho tem como objetivo implementar um algoritmo de ordenação externa, considerando restrições de memória e número de arquivos manipulados simultaneamente. O programa ordena um arquivo de entrada contendo números inteiros, utilizando seleção por substituição para geração das sequências iniciais e intercalação polifásica para obtenção do arquivo final ordenado.


## 2. Modelo Considerado

- A memória principal comporta, no máximo, m − 1 registros simultaneamente.
- O parâmetro m representa também o número máximo de arquivos manipulados ao mesmo tempo:
  - m − 1 arquivos de entrada
  - 1 arquivo de saída
- O acesso aos dados é exclusivamente sequencial.
- Todas as etapas utilizam uma heap mínima.


## 3. Geração das Sequências Iniciais

A geração das sequências iniciais é realizada por meio do algoritmo de seleção por substituição:

- São carregados até m − 1 registros do arquivo de entrada em uma heap mínima.
- Registros que mantêm a ordem crescente continuam na sequência corrente.
- Registros que quebram a ordenação são congelados e utilizados apenas na próxima sequência.
- As sequências ordenadas são distribuídas ciclicamente entre m − 1 arquivos temporários, separados por linhas em branco.


## 4. Intercalação Polifásica

A intercalação das sequências é feita utilizando o método de ordenação polifásica:

- Em cada fase, uma fita sem sequências é escolhida como saída.
- As demais fitas atuam como entrada.
- O número de sequências intercaladas em cada fase é o mínimo entre as fitas de entrada.
- O processo se repete até restar apenas uma sequência totalmente ordenada.

A intercalação foi implementada com foco em correção lógica, mesmo ao custo de maior verbosidade. Cada decisão foi tomada para evitar erros comuns, como:

- Misturar registros de runs diferentes;
- Criar mais de uma fita vazia por fase;
- Perder o controle do número real de sequências.
- 
O uso de uma heap durante a intercalação garante:
- Ordenação correta entre registros de diferentes fitas;
- Complexidade adequada;
- Comportamento previsível.

Sobre Ausência de Distribuição Fibonacci Explícita

O projeto permite (e prioriza) a intercalação polifásica funcional, não apresentando uma distribuição inicial perfeita baseada em Fibonacci.


## 5. Execução do Programa

O programa deve ser executado em linha de comando, recebendo três parâmetros:

```bash
python3 polymerge.py m input.txt output.txt
```
Onde:
- m é o número máximo de registros em memória (m ≥ 3)
- input.txt é o arquivo de entrada contendo números inteiros (um por linha)
- output.txt é o arquivo de saída ordenado
- 
Exemplo
```bash
python3 polymerge.py 5 input.txt output.txt
```
## 6. Saída e Métricas

Além de gerar o arquivo ordenado, o programa exibe as seguintes estatísticas:
- Número de Sequências (#seq)
- Indica o número de sequências processadas em cada fase da ordenação.
```text
#seq 65 33 17 9 5 1
```
Taxa Média de Processamento (tx)
Corresponde ao número médio de vezes que cada registro foi processado:
```text
tx 3.2
```

## 7. Organização dos Arquivos

Durante a execução, são criados arquivos temporários:

```text
F0.txt, F1.txt, ..., Fk.txt
```
Ao final da execução, todos os arquivos temporários são removidos automaticamente, permanecendo apenas o arquivo de saída final.


## 8. Considerações Finais

O trabalho implementa um algoritmo de ordenação externa, seguindo os conceitos apresentados na aula. A respeito das restrições de memória, utiliza acesso sequencial aos dados e aplica técnicas de seleção por substituição e intercalação polifásica.


## 9. Observações

- O programa pode ser executado diretamente no terminal Linux.
- Não utiliza bibliotecas externas.
- Está preparado para lidar com arquivos de grande volume de dados.
