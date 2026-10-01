from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

dados_cancer = load_breast_cancer()
X = dados_cancer.data
Y = dados_cancer.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
modelo = GradientBoostingClassifier()
modelo.fit(X_train, y_train)
print("Acurácia %0f" % modelo.score(X_test, y_test))