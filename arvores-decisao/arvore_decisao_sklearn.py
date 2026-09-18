from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Dataset do exemplo-calculo.txt (mesmo do arquivo manual)
X_raw = [
    ["Ensolarado", "Alta",  "Fraco"],
    ["Ensolarado", "Alta",  "Forte"],
    ["Nublado",    "Alta",  "Fraco"],
    ["Chuvoso",    "Média", "Fraco"],
    ["Chuvoso",    "Fraca", "Forte"],
    ["Chuvoso",    "Forte", "Fraco"],
    ["Nublado",    "Média", "Forte"],
    ["Nublado",    "Média", "Fraco"],
]
y_raw = ["Não", "Não", "Sim", "Sim", "Não", "Sim", "Sim", "Sim"]

colunas = ["Clima", "Temperatura", "Vento"]

# Codifica strings em inteiros (necessário para o sklearn)
encoders = [LabelEncoder() for _ in colunas]
X = np.column_stack([enc.fit_transform(col) for enc, col in zip(encoders, zip(*X_raw))])

enc_alvo = LabelEncoder()
y = enc_alvo.fit_transform(y_raw)

# Treina a árvore usando critério de entropia (equivalente ao ID3)
modelo = DecisionTreeClassifier(criterion="entropy", random_state=42)
modelo.fit(X, y)

# Exibe a árvore em formato texto
print("=== Árvore de Decisão (scikit-learn, critério=entropia) ===\n")
print(export_text(modelo, feature_names=colunas))

# Avalia no conjunto de treino
y_pred = modelo.predict(X)
print("=== Avaliação nos dados de treino ===")
print(f"Acurácia: {accuracy_score(y, y_pred):.0%}\n")
print(classification_report(y, y_pred, target_names=enc_alvo.classes_))

# Importância dos atributos
print("=== Importância dos atributos ===")
for nome, imp in zip(colunas, modelo.feature_importances_):
    print(f"  {nome}: {imp:.4f}")

# Previsão para novo exemplo
print("\n=== Exemplo de previsão para novo dado ===")
novo_raw = [["Chuvoso", "Média", "Fraco"]]
novo_enc = np.column_stack([
    enc.transform([val]) for enc, val in zip(encoders, novo_raw[0])
])
pred = modelo.predict(novo_enc)
print(f"  Entrada: Clima=Chuvoso, Temperatura=Média, Vento=Fraco")
print(f"  Previsão: {enc_alvo.inverse_transform(pred)[0]}")
