# Projeto de Dados IC2024: Dashboards

## Foram disponibilizados 3 databases, cada uma contendo dados da área de uma companhia, e o desafio é extrair o máximo de insights possíveis e criar dashboards interativas.

### Estrutura
- Realizei a curadoria dos dados .csv com Python via pandas (a terceira database possuía quebras de leitura que impossibilitavam a leitura no gerenciador do banco de dados; identifiquei os erros e os corrigi).
- Fiz a extração e realizei o upload via Google Drive.
- A modelagem e preparação dos dados foram realizadas via BigQuery.

### Metodologia
- A modelagem e preparação dos dados foram realizadas via BigQuery.
- Aplicação das dashboards via Looker Studio.

#### Base de Dados 1: Chamados no SAC Marketplace
- Organizei um mapeamento de todo o trajeto da abertura dos chamados, quais foram os maiores agravantes e motivos de maior abertura.
- Busquei idealizar uma tabela simples e organizada, porém com filtros que ampliam muito a captura de informações.

#### Base de Dados 2: Malha logística e transporte
- Busquei entender e compreender a dimensão da logística nos pedidos apresentados; fiz a junção e intercalei por malha, tipo de entrega e grupo de transporte.
- Tabela focada em análise exploratória, de fácil entendimento com evidências cruciais.

#### Base de Dados 3: Controle de vendas
- Apliquei uma visão técnica ao projeto, visando ter um mapa geral da venda geral.
- Elaborei uma tabela com dados financeiros, separados por parceiros, estados, índice de venda por trimestre, média de gasto e filtros elaborados com diversas possibilidades e informações.

#### Link Dashboards interativas. *Só pode ser utilizada por membros da companhia.


- Dash com foco sobre abertura de Atendimento Giba, com foco nos cancelamentos.
https://lookerstudio.google.com/reporting/60d92e73-1b70-4a8d-aba3-e7e38ec298d8

- Dash com foco na Malha Logística, mostrando de ponta a ponta o trajeto e eficiência. 
https://lookerstudio.google.com/reporting/8418beb7-ae3e-41c7-9dad-a252d937cd7a

- Dash financeira focada nas vendas, porcentagem de venda e estabilidade de cada estado.
https://lookerstudio.google.com/reporting/19fef6bb-88bd-417a-bba1-bd3d63b2742f
##
#### Foi um projeto intenso e gratificante.

### Agradeço a todos!


