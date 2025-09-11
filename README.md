# Projeto: Automação de fluxo end-to-end para acessos de banda larga fixa

## Descrição

Solução de engenharia de dados para automatizar o fluxo de coleta, armazenamento, transformação, carregamento e consulta aos dados de acesso a banda larga fixa no Brasil. Permitindo consulta via API Rest e consultas através de linguagem natural.

## Objetivos

1. Capturar automaticamente dados do dados.gov.br
2. Tratar, estruturar e organizar os dados em Data Lake
3. Automatizar o fluxo com agendamento via N8N
4. Disponibilizar API Rest permitindo consultas dos resultados no Data Lake
5. Permitir consultas em linguagem natural com suporte de LLM

## Tecnologias utilizadas

1. **Python** e **PySpark** para o processo de ETL
2. **AWS S3** utilizando um bucket como Data Lake
3. **N8N** para orquestração de workflows e integrações
4. **API REST** para disponibilização dos dados
5. **Firebase Studio** utilizando uma interface gráfica para processamento de linguagem natural

## Pontos de melhoria

1. Adicionar variáveis de ambiente para as credenciais e dados necessários
2. Otimizar o processo de transformação e carregamento para o S3
3. Aprimorar a UI para utilização dos usuários finais
4. Implementar teste de segurança e performance 
