# mata54-trab-2025-2 - polymerge

Aluna: Elis Marcela de Souza Alcantara

## 1. Objetivo

Este trabalho tem como objetivo implementar um algoritmo de ordenação externa, conforme especificado no projeto, utilizando o método de ordenação polifásica (polymerge), respeitando as restrições:
	•	Limitação da memória principal a m − 1 registros simultâneos;
	•	Uso exclusivo de arquivos temporários para entrada e saída;
	•	Não utilização de métodos de ordenação em memória interna para o arquivo completo;
	•	Capacidade de lidar com arquivos de entrada grandes, sem restrição no número de registros;
	•	Execução correta em ambiente Linux, utilizando Python 3.12.

## 2. Método de Ordenação Utilizado

A ordenação implementada baseia-se na ordenação externa, em que os dados que serão ordenados não podem ser inteiramente carregados em memória principal devido a limitações de espaço na memória. O arquivo de entrada é processado de forma incremental, com o auxílio de arquivos temporários (fitas), utilizando técnicas de geração de sequências e intercalação.

O método implementado é composto por duas etapas principais:
	1.	Geração das sequências iniciais ordenadas;
	2.	Intercalação das sequências

1. Geração das Sequências Iniciais

A geração das sequências iniciais é realizada através do algoritmo de seleção por substituição, técnica utilizada em ordenação externa para produzir sequências significativamente maiores do que a quantidade de registros que cabem em memória.

Funcionamento:
	•	São lidos até m − 1 registros do arquivo de entrada, que são inseridos em uma heap mínima;
	•	O menor elemento da heap é removido e gravado na fita correspondente à sequência atual;
	•	A cada remoção, um novo registro é lido do arquivo de entrada:
	•	Se o valor lido for maior ou igual ao último valor gravado, ele é inserido normalmente na heap;
	•	Caso contrário, o registro é congelado, sendo reservado para a próxima sequência;
	•	Quando a heap se esvazia, a sequência corrente é encerrada e inicia-se uma nova sequência com os registros congelados.

Vantagens da seleção por substituição
	•	Permite gerar sequências iniciais maiores do que o tamanho da memória disponível;
	•	Reduz o número total de fases de intercalação necessárias;
	•	Explora de forma eficiente a heap para manter a ordenação local.

2. Intercalação das Sequências

Após a geração das sequências iniciais, inicia-se a fase de intercalação, que combina as sequências ordenadas até a obtenção de um único arquivo final ordenado.

Neste trabalho, foram consideradas duas estratégias de intercalação: polifásica (polymerge.py) e balanceada (balanceada.py).

2.1 Intercalação Polifásica (polymerge.py)

A intercalação polifásica é uma técnica avançada de ordenação externa cujo principal objetivo é minimizar o número de leituras e escritas em disco, reduzindo o custo de E/S.

Princípios do método
	•	As sequências iniciais são distribuídas de forma desigual entre as fitas, geralmente seguindo uma lógica baseada na sequência de Fibonacci;
	•	Em cada fase:
	 •	m − 1 fitas atuam como entrada;
	 •	uma fita permanece vazia e é utilizada como saída;
	 •	Ao final de cada fase, ocorre a alternância dos papéis das fitas, mantendo sempre uma fita vazia.

Dificuldades práticas encontradas

Embora o método esteja implementado conceitualmente, a aplicação prática apresentou dificuldades consideráveis:
	1.	Distribuição inicial das sequências
A distribuição correta das sequências iniciais entre as fitas é comprometida. Pequenas alterações comprometem toda a lógica das fases posteriores.
	2.	Controle do fim das sequências
Diferenciar corretamente entre:
	•	fim de uma sequência,
	•	e fim de um arquivo
mostrou-se um ponto de dificuldade, podendo levar à intercalação incorreta dos registros.
	3.	Alternância dinâmica de fitas
A troca correta entre fitas de entrada e saída a cada fase exige um controle rigoroso de estado, o que aumenta significativamente a complexidade da implementação.

Apesar da implementação estrutural do algoritmo, o método de intercalação polifásica não garante a correta ordenação do arquivo final em todos os casos. Por conta disso, também foi criado o código com implementação da intercalação balanceada.

2.2 Intercalação Balanceada (balanceada.py)

Como forma de validação do restante do algoritmo, foi implementada também a intercalação balanceada, uma abordagem mais simples e robusta com garantia de ordenação em todos os casos.

Características do método
	•	As sequências iniciais são distribuídas de forma equilibrada entre as fitas;
	•	Em cada fase, as sequências são intercaladas de maneira simétrica;
	•	Uma heap mínima é utilizada para selecionar o menor elemento disponível entre todas as fitas de entrada.

Vantagens
	•	Implementação mais simples e menos suscetível a erros;
	•	Controle direto do fim das sequências;
	•	Produz corretamente o arquivo final ordenado em todos os testes realizados.
  
A intercalação balanceada funciona de forma correta e produz o arquivo final totalmente ordenado, comprovando que:
	•	a geração das sequências iniciais está correta;
	•	o uso de heaps e arquivos externos foi implementado adequadamente;
	•	as dificuldades observadas estão concentradas exclusivamente na intercalação polifásica.

3. Considerações Sobre o Método

A implementação torna evidente que embora a intercalação polifásica seja teoricamente mais eficiente, sua complexidade de implementação é significativamente maior quando comparada à intercalação balanceada.

## 3. Interface de Entrada e Saída

A interface de entrada e saída do programa foi pensada para ser compatível com ambientes Linux, conforme exigido na especificação do projeto. Toda a interação com o usuário ocorre exclusivamente por meio da linha de comando (shell), não havendo qualquer interface gráfica.

1. Parâmetros de Entrada

O programa recebe três parâmetros obrigatórios no momento da execução:

```bash
python polymerge.py m input.txt output.txt
```
Onde:
	•	<m>
Número máximo de arquivos que podem ser manipulados simultaneamente pelo algoritmo.
Esse parâmetro também define:
	•	o tamanho da heap utilizada na geração das sequências iniciais;
	•	o número de fitas disponíveis durante as fases de intercalação.
Por restrição, valores m < 3 não são válidos, já que o algoritmo necessita de pelo menos dois arquivos de entrada e um de saída.
	•	<input.txt>
Arquivo texto contendo os registros para serem ordenados.
Cada linha do arquivo deve conter exatamente um número inteiro.
Não há limitação quanto ao número de registros no arquivo.
	•	<output.txt>
Arquivo texto onde é armazenado o resultado final da ordenação.
Caso o arquivo já exista, o conteúdo é sobrescrito.

2. Formato do Arquivo de Entrada

O arquivo de entrada deve obedecer ao seguinte formato:
	•	Texto simples (.txt);
	•	Um número inteiro por linha;
	•	Sem cabeçalhos, separadores adicionais ou linhas em branco.

Exemplo de input.txt:

```bash
42
-7
15
3
99
1
```

3. Formato do Arquivo de Saída

O arquivo de saída contém os mesmos registros do arquivo de entrada, porém organizados em ordem crescente, com um valor por linha:

```bash
-7
1
3
15
42
99
```

Esse arquivo é gerado no final do processo de intercalação (balanceada.py).

4. Saída no Terminal

Além do arquivo de saída ordenado, o programa exibe informações no terminal. Essas informações tem como objetivo analisar o comportamento do algoritmo durante a ordenação externa.

4.1 Número de Sequências Ordenadas
O programa exibe uma linha iniciada por #seq, seguida pelos números de sequências ordenadas geradas em cada fase do algoritmo.

Exemplo:

```text
#seq 65 33 17 9 5 1
```

Cada valor representa a quantidade de sequências existentes ao final de uma fase da ordenação externa.

4.2 Número Médio de Processamentos (tx)
Também é exibido o valor tx, que representa o número médio de vezes que cada registro foi processado ao longo da execução do algoritmo.

Exemplo:

```text
tx 3.2
```

Esse valor é para avaliar o custo do algoritmo em termos de leituras, escritas e movimentações de registros entre os arquivos temporários.


5. Tratamento de Erros

O programa realiza validações básicas sobre os parâmetros de entrada, incluindo:
	•	verificação do valor de m;
	•	existência e permissão de leitura do arquivo de entrada;
	•	possibilidade de criação ou sobrescrita do arquivo de saída.

Em caso de erro, o programa interrompe a execução e exibe uma mensage no terminal.

## 4. Considerações Finais

Este trabalho demonstra, na prática, a complexidade da intercalação polifásica, que vai além da intercalação balanceada tradicional. Embora o método polifásico seja teoricamente mais eficiente em termos de número de leituras e escritas, a implementação correta exige um controle rigoroso das sequências e das fitas.

## Considerações Finais

Este trabalho possibilitou a aplicação prática dos conceitos de ordenação externa, destacando as dificuldades nas restrições de memória e no uso intensivo de arquivos externos. A geração das sequências iniciais por seleção por substituição mostrou-se eficiente, reduzindo o número de fases de intercalação.

A implementação da intercalação polifásica (polymerge) foi etapa mais complexa do projeto. Apesar de estar conceitualmente implementada, dificuldades no controle das sequências e na alternância entre fitas impedem a obtenção correta do output final em todos os casos.

Em contrapartida, a intercalação balanceada apresentou funcionamento correto em todos os testes realizados, validando a geração das sequências iniciais e o controle dos arquivos externos.

De forma geral, o trabalho atingiu seus objetivos ao fortalecer os conceitos de ordenação externa, demonstrando na prática a diferença entre a eficiência teórica e a complexidade de implementação dos algoritmos estudados em sala.
