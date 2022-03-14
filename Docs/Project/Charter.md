# Project Charter

## Área de atuação
Pessoas que buscam:
- melhorar seu condicionamento físico
- se manter ativas
- mudar seu estilo de vida para um padrão mais saudável

## Escopo
- Monitoramento das atividades diárias
- Predição de hábitos
- Sugestão de atividades regulares

## Equipe
- Igor Imperiali:
  - Data Sccientist(s)
  - Data administrator
- Bruno Verdan:
  - Data Sccientist(s)
  - Data administrator
- Fernando Ferreira
  - Business contact
  - Stackholder

## Metricas
- Aumentar a quantidade de exercicios feitos por dia
- Aumentar o deficit calorico do usuário
- Aumentar a massa magra e a diminuir porcentagem de gordura em 5% em um mês

## Planejamento
Phases (milestones), timeline, short description of what we'll do in each phase.

## Architecture
- Data

  - What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
- Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either

  - all the data,
  - after some pre-aggregation on-prem,
  - Sampled data enough for modeling
- What tools and data storage/analytics resources will be used in the solution e.g.,

  - ASA for stream aggregation
  - HDI/Hive/R/Python for feature construction, aggregation and sampling
  - AzureML for modeling and web service operationalization
- How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.

  - How will the customer use the model results to make decisions
  - Data movement pipeline in production
  - Make a 1 slide diagram showing the end to end data flow and decision architecture
    - If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.
## Communication
- How will we keep in touch? Weekly meetings?
- Who are the contact persons on both sides?