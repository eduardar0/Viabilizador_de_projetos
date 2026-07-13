import os
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def train_or_predict(new_projects):
    model_path = "logistic_model.joblib"
    scaler_path = "logistic_model_scaler.joblib"
    metrics_path = "logistic_model_metrics.joblib"

    # Testa se o modelo existe localmente
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
    else:
        # Garante que o arquivo de treino existe antes de tentar ler
        if not os.path.exists("projects_data.csv"):
            raise FileNotFoundError(
                "O arquivo 'projects_data.csv' é necessário para treinar o modelo pela primeira vez."
            )

        df_projects = pd.read_csv("projects_data.csv")

        # Separa variáveis
        X = df_projects[["investment", "expected_return", "impact_score"]]
        y = df_projects["viability"]

        # Normaliza
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Divide em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.3, random_state=42
        )

        # Treina
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Avalia
        y_pred = model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)

        # Salva modelo, scaler e métricas em disco
        joblib.dump(model, model_path)
        joblib.dump(scaler, scaler_path)
        joblib.dump(report, metrics_path)

    # Previsão
    if new_projects:
        df_new_projects = pd.DataFrame(new_projects)
        X_new_scaled = scaler.transform(df_new_projects)

        predictions = model.predict(X_new_scaled)
        probabilities = model.predict_proba(X_new_scaled)[:, 1]

        df_new_projects["probability"] = probabilities
        df_new_projects["viability"] = predictions

        return df_new_projects, joblib.load(metrics_path)

    return None, joblib.load(metrics_path)


if __name__ == "__main__":
    # Dados de teste para novos projetos
    new_projects = [
        {"investment": 40000, "expected_return": 60000, "impact_score": 6}
    ]

    try:
        predictions, metrics = train_or_predict(new_projects)

        if predictions is not None:
            print("\n--- Novos Projetos e Viabilidade ---")
            print(predictions)

        print("\n--- Métricas do Modelo ---")
        print(f"Acurácia Geral: {metrics['accuracy']:.2f}")

    except FileNotFoundError as e:
        print(f"Erro: {e}")