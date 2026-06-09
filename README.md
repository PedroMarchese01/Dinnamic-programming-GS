# AgroSphere

Sistema desenvolvido para monitoramento e análise de telemetria agrícola em ambientes espaciais, aplicando conceitos de estruturas de dados, algoritmos de busca e recursividade para auxiliar na gestão de cultivos em operações da economia espacial.

---

# Sumário

- [Integrantes](#integrantes)
- [Contexto](#contexto)
- [Problema](#problema)
- [Solução Proposta](#solução-proposta)
- [Relação com a Economia Espacial](#relação-com-a-economia-espacial)
- [Como o Sistema Funciona](#como-o-sistema-funciona)
- [Estruturas de Dados](#estruturas-de-dados)
- [Busca Binária e Recursividade](#busca-binária-e-recursividade)
- [Manipulação dos Dados](#manipulação-dos-dados)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar](#como-executar)
- [Aplicação dos Requisitos da Atividade](#aplicação-dos-requisitos-da-atividade)
- [Conclusão](#conclusão)

---

# Integrantes

| Nome | RM |
|--------|--------|
| Pedro Marchese | RM563339 |
| Augusto Valério | RM562185 |
| Jonas Esteves França | RM564143 |
| Vitor Rodrigues Tigre | RM561746 |
| Mariana Silva Oliveira | RM564241 |

---

# Contexto

A economia espacial vem se tornando um dos setores mais promissores da atualidade. Tecnologias desenvolvidas para operações espaciais já são utilizadas em diversas áreas da sociedade, incluindo monitoramento climático, agricultura de precisão, comunicação, logística e prevenção de desastres.

Com o avanço de projetos voltados para permanência humana no espaço, torna-se necessário desenvolver soluções capazes de monitorar e controlar sistemas agrícolas responsáveis pela produção de alimentos em ambientes remotos, como estações espaciais, bases lunares e futuras colônias em Marte.

Dentro desse cenário foi desenvolvido o AgroSphere, um sistema capaz de processar e analisar dados de telemetria agrícola para auxiliar no acompanhamento das condições operacionais de cultivo.

---

# Problema

Em ambientes agrícolas altamente controlados, pequenas variações em fatores como temperatura, umidade, oxigênio, dióxido de carbono ou disponibilidade de água podem comprometer a produção de alimentos.

Quando essas operações acontecem em locais remotos ou no espaço, a necessidade de monitoramento se torna ainda mais crítica, pois falhas podem impactar diretamente a sobrevivência da missão.

Dessa forma, surge a necessidade de uma solução capaz de:

- Receber dados continuamente;
- Organizar essas informações para processamento;
- Permitir consultas rápidas de registros específicos;
- Auxiliar na identificação de situações que exijam atenção.

---

# Solução Proposta

O AgroSphere realiza o carregamento de dados de telemetria agrícola armazenados em um arquivo JSON contendo mais de 30 registros contínuos.

Esses dados são processados pelo sistema para simular o monitoramento de uma fazenda espacial automatizada.

Durante o processamento, os registros são organizados utilizando uma estrutura de Fila (Queue), permitindo que sejam analisados na mesma ordem em que foram recebidos.

Além disso, o sistema disponibiliza uma funcionalidade de busca que permite localizar registros específicos através de seu identificador, utilizando Busca Binária implementada com Recursividade.

Ao final da execução são gerados relatórios e estatísticas que auxiliam no acompanhamento do ambiente monitorado.

---

# Relação com a Economia Espacial

A produção de alimentos é considerada um dos principais desafios para futuras missões espaciais de longa duração.

Ambientes como estações espaciais, bases lunares e colônias em Marte dependerão de sistemas agrícolas capazes de operar de forma autônoma e eficiente.

O AgroSphere foi idealizado para representar esse cenário, simulando a coleta e análise de dados provenientes de sensores agrícolas.

Embora seja uma aplicação acadêmica, o projeto demonstra como conceitos de programação, estruturas de dados e processamento de informações podem contribuir para a construção de soluções voltadas ao setor espacial.

---

# Como o Sistema Funciona

<details>
<summary><strong>Visualizar funcionamento completo</strong></summary>

<br>

1. O sistema realiza a leitura dos registros presentes no arquivo JSON.

2. Os dados são carregados para a memória.

3. Cada registro é inserido em uma estrutura de Fila (Queue).

4. Os registros são processados na ordem de chegada.

5. Informações relevantes são analisadas.

6. Os registros podem ser localizados através da Busca Binária.

7. A Busca Binária é executada utilizando Recursividade.

8. Relatórios estatísticos e análises são gerados ao final da execução.

</details>

---

# Estruturas de Dados

<details>
<summary><strong>Fila (Queue)</strong></summary>

<br>

A estrutura de Fila foi utilizada para representar o fluxo natural de chegada dos dados de telemetria.

O conceito utilizado é FIFO (First In, First Out), onde o primeiro registro recebido é também o primeiro registro processado.

Essa abordagem simula o funcionamento real de sistemas de monitoramento contínuo, nos quais os dados são recebidos e tratados sequencialmente.

</details>

---

# Busca Binária e Recursividade

<details>
<summary><strong>Busca Binária</strong></summary>

<br>

A busca de registros é realizada através do identificador único de cada telemetria.

Para tornar a localização eficiente, os dados são organizados e pesquisados utilizando o algoritmo de Busca Binária.

Complexidade:

```text
O(log n)
```

Isso reduz significativamente a quantidade de comparações necessárias para localizar um registro.

</details>

<br>

<details>
<summary><strong>Recursividade</strong></summary>

<br>

A implementação da Busca Binária foi realizada utilizando Recursividade.

A função realiza chamadas para si mesma até encontrar o registro desejado ou determinar que ele não está presente na base de dados.

Essa implementação atende diretamente aos requisitos definidos na atividade.

</details>

---

# Manipulação dos Dados

<details>
<summary><strong>Fonte dos Dados</strong></summary>

<br>

Os dados utilizados pelo sistema são carregados a partir de um arquivo JSON.

Arquivo utilizado:

```text
data/agrosphere_telemetry.json
```

A base contém mais de 30 registros contínuos para processamento.

Cada registro contém informações como:

- ID
- Timestamp
- Setor monitorado
- Oxigênio (%)
- CO₂ (ppm)
- Temperatura (°C)
- Umidade (%)
- Reserva de água (L)
- Energia solar (kW)
- Saúde das plantas (%)

</details>

---

# Funcionalidades

<details>
<summary><strong>Visualizar funcionalidades</strong></summary>

<br>

- Leitura de arquivos JSON
- Processamento de telemetria
- Organização dos registros em Fila
- Consulta de registros específicos
- Busca Binária Recursiva
- Geração de relatórios
- Geração de estatísticas
- Exportação de resultados
- Criação automática de bases para testes

</details>

---

# Estrutura do Projeto

```text
Dn_gs/
│
├── controller/
│   └── telemetry_controller.py
│
├── services/
│   ├── data_repository.py
│   ├── queue_manager.py
│   ├── recursive_binary_search.py
│   ├── report_manager.py
│   └── table_formatter.py
│
├── data/
│   ├── agrosphere_telemetry.json
│   └── analyzed_telemetry.json
│
├── reports/
│   ├── status_operacional.png
│   └── tipos_de_alerta.png
│
└── README.md
```

---

# Tecnologias Utilizadas

- Python
- JSON
- Estruturas de Dados (Queue)
- Busca Binária
- Recursividade
- Matplotlib
- Git
- GitHub

---

# Como Executar

### Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/agrosphere.git
```

### Acessar a pasta do projeto

```bash
cd Dn_gs
```

### Executar o sistema

```bash
python controller/telemetry_controller.py
```

---

# Aplicação dos Requisitos da Atividade

| Requisito Exigido | Implementação no AgroSphere |
|-------------------|-----------------------------|
| Definição de um problema relacionado à Indústria Espacial | Monitoramento de telemetria agrícola em ambientes espaciais |
| Utilização de dados externos | Leitura de dados através de arquivo JSON |
| Base contendo no mínimo 30 registros | Arquivo contendo mais de 30 registros contínuos |
| Utilização de Estrutura de Dados | Implementação de Fila (Queue) |
| Busca de registros específicos | Implementação de Busca Binária |
| Utilização de Recursividade | Busca Binária implementada de forma recursiva |
| Organização utilizando funções | Sistema modularizado em múltiplos módulos e funções |
| Versionamento e documentação | Projeto estruturado e documentado no GitHub |

---

# Conclusão

O AgroSphere foi desenvolvido com o objetivo de demonstrar a aplicação prática de conceitos fundamentais de programação no contexto da economia espacial. A solução simula o monitoramento de uma operação agrícola automatizada, realizando o processamento de dados de telemetria através de estruturas de dados adequadas e algoritmos eficientes.

Durante o desenvolvimento foram aplicados conceitos de manipulação de arquivos, filas, busca binária, recursividade e modularização de código. O sistema foi capaz de processar os registros da base de dados, organizar as informações, realizar consultas eficientes e gerar resultados de forma estruturada.

Ao final do projeto, todos os requisitos propostos pela atividade foram atendidos com sucesso, resultando em uma solução funcional, organizada e alinhada ao tema da Indústria Espacial.