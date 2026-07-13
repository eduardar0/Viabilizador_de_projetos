# Viabilizador de Projetos com Machine Learning

Este é um projeto prático de Inteligência Artificial que utiliza um modelo de Regressão Logística para prever a viabilidade financeira e de impacto de novos projetos. O script analisa dados históricos, treina o modelo preditivo automaticamente (caso ele ainda não exista) e exporta os arquivos binários para previsões futuras rápidas.

---

## Funcionalidades

* **Treinamento Automatizado:** Identifica se o modelo preditivo já foi treinado; caso contrário, realiza o treinamento na hora usando dados históricos.
* **Normalização de Dados:** Aplica o `StandardScaler` para garantir que as escalas de investimento e retorno não distorçam as previsões do modelo.
* **Persistência de Objetos:** Salva o modelo, o normalizador (scaler) e as métricas em disco utilizando a biblioteca `joblib`.
* **Cálculo de Probabilidade:** Além de classificar se o projeto é viável ou não (1 ou 0), o modelo retorna a porcentagem exata de chance de sucesso do projeto.

---

## Estrutura do Projeto

```text
viabilidade-projetos/
│
├── main.py                 # Código principal (Treino, avaliação e predição)
├── projects_data.csv       # Base de dados histórica para o treino do modelo
├── requirements.txt        # Dependências do projeto (Bibliotecas Python)
└── .gitignore              # Filtro para evitar o envio de arquivos desnecessários ao GitHub