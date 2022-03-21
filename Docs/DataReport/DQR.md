# Data Quality Report

- Para fazer o envio dos dados para a AWS, é necessário a tradução dos dados para JSON
  - Nossos dados vem de um CSV, porém a AWS compreende mensagens apenas no formato JSON
  - Para atender a necessidade, passamos os dados do CSV para o formato do Python de Dictonary e então traduzimos ele para JSON
- Essa mudança é feita em Code/Operationalization/ScriptAWS.py
