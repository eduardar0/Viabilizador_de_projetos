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



## Tecnologias Utilizadas

- Python 3
- Pandas: Manipulacao e analise de dados.
- Scikit-Learn: Criacao do modelo de Machine Learning, divisao de dados e metricas de avaliacao.
- NumPy: Operacoes matematicas e suporte a arrays.
- Joblib: Salvamento e carregamento eficiente de modelos preditivos.

## Como Configurar e Executar o Projeto

Siga os passos abaixo para preparar o ambiente na sua maquina:

### 1. Clonar o repositorio

```git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd viabilidade-projetos```


### 2. Configurar o Ambiente Virtual (Recomendado)

### No Linux/macOS:

``` python3 -m venv venv
source venv/bin/activate  ```


### No Windows:

``` python -m venv venv
venv\Scripts\activate  ```      


### 3. Instalar as Dependencias


``` pip install -r requirements.txt  ```      



## Execucao e Treinamento do Modelo

O script main.py foi projetado para ser inteligente e evitar reprocessamento desnecessario. O comportamento do treino e da execucao funciona da seguinte forma:

### Como Rodar as Previsoes

Para executar o projeto e obter a analise de viabilidade dos novos projetos configurados no codigo, mude para o seu ambiente virtual e execute:

```python main.py```   


### Como Funciona o Treinamento

- Treino Automatico: Ao rodar o comando acima pela primeira vez, o script notara a ausencia do arquivo logistic_model.joblib. Ele lera automaticamente o arquivo projects_data.csv, treinara o modelo, exibira as metricas no terminal e salvara o progresso em disco.

- Uso do Modelo Pre-treinado: Nas execucoes seguintes, o script carregara o modelo diretamente do disco em menos de um segundo, sem precisar ler o arquivo CSV novamente.

### Como Forcar um Novo Treinamento

Se voce atualizou o arquivo projects_data.csv com novos dados historicos e precisa retreinar o modelo do zero, basta deletar os arquivos binarios gerados antes de rodar o script:

No Linux/macOS:

```rm *.joblib
python main.py```  


No Windows (Prompt de Comando):

```del *.joblib
python main.py```


## Resultados do Modelo

O modelo atual foi testado e avaliado com dados divididos na proporcao de 70% para treino e 30% para teste, alcancando excelentes metricas de assertividade:

- Acuracia Geral: 86%
- Precisao (Classe 1 - Viavel): 82%
- Recall (Classe 1 - Viavel): 76%

Nota: Os arquivos binarios .joblib gerados apos a primeira execucao sao ignorados pelo Git para manter o repositorio leve e focado apenas no codigo-fonte.