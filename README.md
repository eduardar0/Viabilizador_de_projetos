# Viabilizador de Projetos com Machine Learning

Este projeto utiliza **Machine Learning** para prever a viabilidade de novos projetos com base em dados históricos. O modelo empregado é uma **Regressão Logística**, capaz de classificar um projeto como viável ou não, além de informar a probabilidade de sucesso da previsão.

O sistema realiza automaticamente o treinamento do modelo caso ele ainda não exista e reutiliza o modelo salvo nas próximas execuções, tornando as previsões mais rápidas.

---

# Funcionalidades

- Treinamento automático do modelo de Machine Learning.
- Normalização dos dados utilizando `StandardScaler`.
- Divisão automática dos dados em treino (70%) e teste (30%).
- Avaliação do modelo utilizando métricas de classificação.
- Salvamento do modelo treinado, do scaler e das métricas em arquivos `.joblib`.
- Predição da viabilidade de novos projetos.
- Cálculo da probabilidade de sucesso de cada projeto analisado.

---

# Estrutura do Projeto

```text
viabilidade-projetos/
│
├── main.py                      # Código principal
├── projects_data.csv            # Base de dados utilizada para treinamento
├── requirements.txt             # Dependências do projeto
├── README.md                    # Documentação
├── .gitignore                   # Arquivos ignorados pelo Git
│
├── logistic_model.joblib        # Modelo treinado (gerado automaticamente)
├── logistic_model_scaler.joblib # Scaler salvo automaticamente
└── logistic_model_metrics.joblib# Métricas do modelo
```

Os arquivos `.joblib` são criados automaticamente após a primeira execução e normalmente não devem ser enviados ao GitHub.

---

# Tecnologias Utilizadas

- Python 3
- Pandas
- NumPy
- Scikit-Learn
- Joblib

---

# Como Configurar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

cd viabilidade-projetos
```

---

## 2. Criar um ambiente virtual (opcional, mas recomendado)

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

# Como Executar

Execute o arquivo principal:

```bash
python main.py
```

Na primeira execução o sistema irá:

1. Ler o arquivo `projects_data.csv`;
2. Normalizar os dados;
3. Dividir os dados em treino e teste;
4. Treinar a Regressão Logística;
5. Avaliar o modelo;
6. Salvar os arquivos:

- `logistic_model.joblib`
- `logistic_model_scaler.joblib`
- `logistic_model_metrics.joblib`

Nas próximas execuções, esses arquivos serão carregados automaticamente, evitando um novo treinamento.

---

# Como Realizar Novas Previsões

Os projetos que serão analisados são definidos na variável `new_projects` dentro do arquivo `main.py`.

Exemplo:

```python
new_projects = [
    {
        "investment": 13000,
        "expected_return": 69000,
        "impact_score": 7
    },
    {
        "investment": 45000,
        "expected_return": 60000,
        "impact_score": 6
    },
    {
        "investment": 100000,
        "expected_return": 150000,
        "impact_score": 9
    }
]

predictions, metrics = train_or_predict(new_projects)

print(predictions)
print(metrics)
```

A saída apresenta:

- investimento;
- retorno esperado;
- impacto;
- probabilidade de sucesso;
- classificação de viabilidade (0 ou 1).

---

# Como Treinar Novamente

Caso o arquivo `projects_data.csv` seja atualizado com novos dados históricos, basta apagar os arquivos `.joblib`.

### Linux/macOS

```bash
rm *.joblib

python main.py
```

### Windows

```bash
del *.joblib

python main.py
```

Na próxima execução o modelo será treinado novamente utilizando os dados atualizados.

---

# Avaliação do Modelo

O modelo é avaliado utilizando:

- Accuracy
- Precision
- Recall
- F1-Score

As métricas completas ficam armazenadas em:

```text
logistic_model_metrics.joblib
```

e também podem ser exibidas durante a execução do programa.

---

# Tecnologias de Machine Learning Utilizadas

- Regressão Logística (`LogisticRegression`)
- StandardScaler
- Train/Test Split
- Classification Report

---

# Autor

Projeto desenvolvido para fins de estudo e prática de Machine Learning utilizando Python e Scikit-Learn.