
# mata54-trab-2025-2 - polymerge

## Algoritmo de Intercalação Polifásica


## 1. Objetivo

O objetivo deste trabalho é implementar um algoritmo de ordenação externa, capaz de ordenar arquivos de dados que não cabem integralmente na memória principal, respeitando a limitação de memória definida pelo parâmetro `m`.

A solução utiliza seleção por substituição para geração das sequências iniciais e*intercalação polifásica para obtenção do arquivo final ordenado.


## 2. Fundamentação Teórica

O trabalho baseia-se nos conceitos apresentados em aula:

### 2.1 Arquivos Sequenciais

Os dados são armazenados e acessados em arquivos sequenciais, sendo permitidas apenas operações de leitura e escrita sequencial, sem acesso aleatório aos registros.

### 2.2 Memória Limitada

O algoritmo considera que apenas `m − 1` registros podem permanecer simultaneamente na memória, reservando uma posição para escrita, conforme o modelo de ordenação externa.

### 2.3 Heap Mínima

A heap mínima é utilizada para selecionar eficientemente o menor registro entre os dados carregados em memória, tanto na geração das sequências iniciais quanto na fase de intercalação.

### 2.4 Seleção por Substituição

Durante a geração das sequências iniciais, registros que quebram a ordem crescente são congelados e utilizados apenas na próxima sequência, permitindo a criação de sequências maiores que o tamanho da memória.

### 2.5 Intercalação Polifásica

As sequências ordenadas são combinadas em múltiplas fases de intercalação, utilizando até `m − 1` arquivos de entrada e um arquivo de saída por fase, reduzindo progressivamente o número de sequências até restar apenas uma.


## 3. Metodologia e Implementação

O programa foi desenvolvido em Python 3, utilizando bibliotecas padrão da linguagem.

A implementação é dividida em duas fases principais:

### 3.1 Geração das Sequências Iniciais

* Leitura sequencial do arquivo de entrada
* Uso de heap mínima com tamanho máximo `m − 1`
* Aplicação da seleção por substituição
* Geração de arquivos temporários no formato `seq_0_i.txt`

### 3.2 Intercalação das Sequências

* Abertura de até `m − 1` sequências por fase
* Uso de heap mínima para manter a ordenação global
* Geração de novas sequências maiores
* Repetição até restar uma única sequência ordenada


## 4. Funções

* class Registro

Representa um registro do arquivo sequencial, armazenando a chave de ordenação (valor).
A classe define o critério de comparação necessário para o uso da heap mínima durante a ordenação.

* abrir_arquivo_leitura(nome)

Abre um arquivo em modo de leitura sequencial.
Foi criada para centralizar a operação de abertura de arquivos e melhorar a legibilidade do código.

* abrir_arquivo_escrita(nome)

Abre um arquivo em modo de escrita sequencial, utilizado para criação das sequências ordenadas temporárias e do arquivo final.

* gerar_sequencias_iniciais(m, arquivo_entrada)

Implementa a primeira fase da ordenação externa, responsável pela geração das sequências iniciais ordenadas.
Utiliza uma heap mínima com tamanho limitado a m − 1 registros e aplica a técnica de seleção por substituição, congelando registros que quebram a ordenação.

Ao final, retorna:
o número de sequências geradas,
o total de processamentos realizados,
o número total de registros lidos.

* intercalar(m, fase, sequencias)

Realiza a intercalação das sequências ordenadas geradas nas fases anteriores.
Em cada fase, abre até m − 1 arquivos de entrada e utiliza uma heap mínima para produzir uma nova sequência ordenada, reduzindo progressivamente o número de arquivos.

Retorna a lista de novas sequências geradas e o custo da fase em termos de processamentos.

*limpar_arquivos_temporarios(arquivo_final)

Remove todos os arquivos temporários gerados durante a execução do algoritmo, preservando apenas o arquivo final ordenado.
Essa função não altera o algoritmo, apenas organiza o ambiente de execução.

* main()

Função principal responsável por coordenar toda a execução do programa.
Realiza a leitura dos parâmetros de entrada, valida o valor de m, executa a geração das sequências iniciais, controla as fases de intercalação e exibe as métricas finais.


## 5. Execução do Programa

### 5.1 Requisitos

* Sistema operacional Linux
* Python 3.10 ou superior

### 5.2 Forma de Execução

```bash
python3 polymerge.py m input.txt output.txt
```

* `m` é o número máximo de registros em memória
* `input.txt` é o arquivo de entrada não ordenado
* `output.txt` é o arquivo final ordenado

### Exemplo:

```bash
python3 polymerge.py 7 entrada.txt saida.txt
```

## 6. Resultados e Métricas

Ao final da execução, o programa apresenta duas métricas:

### 6.1 Número de Sequências (`#seq`)

Indica a quantidade de sequências existentes em cada fase da ordenação.

Exemplo:

```
#seq 6 3 1
```

### 6.2 Taxa de Processamento (`tx`)

Corresponde à razão entre o número total de processamentos realizados e o número total de registros.

Exemplo:

```
tx 3.2
```

Essas métricas tem o objetivo de analisar o comportamento e a eficiência do algoritmo.


## 7. Organização dos Arquivos

Durante a execução, são criados arquivos temporários no formato:

```
seq_fase_indice.txt
```

Todos os arquivos intermediários são removidos automaticamente ao final da execução, permanecendo apenas o arquivo de saída final.


## 8. Considerações Finais

O trabalho implementa um algoritmo de ordenação externa, seguindo os conceitos apresentados em aula. A solução respeita as restrições de memória, utiliza acesso sequencial aos dados e aplica técnicas de seleção por substituição e intercalação polifásica.


## 9. Observações

* O programa pode ser executado diretamente no terminal Linux.
* Não utiliza bibliotecas externas.
* Está preparado para lidar com arquivos de grande volume de dados.



