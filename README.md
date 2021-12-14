# Definição do projeto

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

## Fontes de dados brutos

| Dataset Name | Original Location | Destination Location | Data Movement Tools / Scripts | Link to Report  |
|--------------|-------------------|----------------------|-------------------------------|-----------------|
| Steps    | Dados vindos de 5 anos de atividades de um usuário | Ajudará na predição de futuros usuários | [01_Steps.csv](/Data/Raw/01_Steps.csv) | [Steps Report](/Docs/DataReport/) |
| Sleeps    | Dados vindos de 5 anos de sono de um usuário | Ajudará na predição de sono de futuros usuários | [02_Sleep.csv](/Data/Raw/01_Sleep.csv) | [Sleep Report](/Docs/DataReport) |

- Steps, <Provide brief summary of the data, such as how to access the data. More Detailed information should be in the Dataset1 Report>
- Sleeps, <Provide brief summary of th edata, such as how to access the data. More Detailed information should be in the Dataset2 Report>

## Dados processados

| Processed Dataset Name | Input Dataset(s) | Data Movement Tools / Scripts | Link to Report  |
|------------------------|------------------|-------------------------------|-----------------|
| DataSetConcatAt | [01_Steps.csv](/Data/Raw/01_Steps.csv) [02_Sleep.csv](/Data/Raw/01_Sleep.csv) | [ConcatTabelas.py](/Code/DataPrep/ConcatTabelas.py) | [Processed Dataset 1 Report](/Docs/DataReport/) |

- DataSetConcatAt, <Provide brief summary of the data, such as how to access the processed data. More Detailed information should be in the Processed Dataset1 Report>

## Conjunto de recursos

| Feature Set Name | Input Dataset(s) | Data Movement Tools / Scripts | Link to Report  |
|------------------|------------------|-------------------------------|-----------------|
| ConcatTabelas | [01_Steps.csv](/Data/Raw/01_Steps.csv) [02_Sleep.csv](/Data/Raw/01_Sleep.csv) | [ConcatTabelas.py](/Code/DataPrep/ConcatTabelas.py) | [Processed Dataset 1 Report](/Docs/DataReport/) |

- ConcatTabelas, <Provide brief summary of th edata, such as how to access the feature set. More Detailed information should be in the Feature Set Report>
