import math
from collections import Counter


# Dataset do exemplo-calculo.txt
dados = [
    {"Clima": "Ensolarado", "Temperatura": "Alta",  "Vento": "Fraco", "Jogar": "Não"},
    {"Clima": "Ensolarado", "Temperatura": "Alta",  "Vento": "Forte", "Jogar": "Não"},
    {"Clima": "Nublado",    "Temperatura": "Alta",  "Vento": "Fraco", "Jogar": "Sim"},
    {"Clima": "Chuvoso",    "Temperatura": "Média", "Vento": "Fraco", "Jogar": "Sim"},
    {"Clima": "Chuvoso",    "Temperatura": "Fraca", "Vento": "Forte", "Jogar": "Não"},
    {"Clima": "Chuvoso",    "Temperatura": "Forte", "Vento": "Fraco", "Jogar": "Sim"},
    {"Clima": "Nublado",    "Temperatura": "Média", "Vento": "Forte", "Jogar": "Sim"},
    {"Clima": "Nublado",    "Temperatura": "Média", "Vento": "Fraco", "Jogar": "Sim"},
]

ALVO = "Jogar"


def entropia(subconjunto):
    if not subconjunto:
        return 0
    contagem = Counter(ex[ALVO] for ex in subconjunto)
    total = len(subconjunto)
    return -sum(
        (c / total) * math.log2(c / total)
        for c in contagem.values()
        if c > 0
    )


def ganho_informacao(subconjunto, atributo):
    total = len(subconjunto)
    valores = {}
    for ex in subconjunto:
        v = ex[atributo]
        valores.setdefault(v, []).append(ex)

    entropia_apos = sum(
        (len(sub) / total) * entropia(sub)
        for sub in valores.values()
    )
    return entropia(subconjunto) - entropia_apos


def melhor_atributo(subconjunto, atributos):
    return max(atributos, key=lambda a: ganho_informacao(subconjunto, a))


def classe_majoritaria(subconjunto):
    contagem = Counter(ex[ALVO] for ex in subconjunto)
    return contagem.most_common(1)[0][0]


def construir_arvore(subconjunto, atributos):
    classes = [ex[ALVO] for ex in subconjunto]

    # Todos os exemplos têm a mesma classe → folha
    if len(set(classes)) == 1:
        return classes[0]

    # Sem atributos para dividir → folha com classe majoritária
    if not atributos:
        return classe_majoritaria(subconjunto)

    melhor = melhor_atributo(subconjunto, atributos)
    arvore = {melhor: {}}

    valores = set(ex[melhor] for ex in subconjunto)
    restantes = [a for a in atributos if a != melhor]

    for valor in valores:
        sub = [ex for ex in subconjunto if ex[melhor] == valor]
        if not sub:
            arvore[melhor][valor] = classe_majoritaria(subconjunto)
        else:
            arvore[melhor][valor] = construir_arvore(sub, restantes)

    return arvore


def prever(arvore, exemplo):
    if not isinstance(arvore, dict):
        return arvore
    atributo = next(iter(arvore))
    valor = exemplo.get(atributo)
    ramo = arvore[atributo].get(valor)
    if ramo is None:
        return None
    return prever(ramo, exemplo)


def imprimir_arvore(arvore, indent=0):
    prefixo = "  " * indent
    if not isinstance(arvore, dict):
        print(f"{prefixo}→ {arvore}")
        return
    atributo = next(iter(arvore))
    print(f"{prefixo}[{atributo}]")
    for valor, sub in arvore[atributo].items():
        print(f"{prefixo}  {valor}:")
        imprimir_arvore(sub, indent + 2)


if __name__ == "__main__":
    atributos = [k for k in dados[0] if k != ALVO]
    arvore = construir_arvore(dados, atributos)

    print("=== Árvore de Decisão (ID3 manual) ===\n")
    imprimir_arvore(arvore)

    print("\n=== Previsões nos dados de treino ===")
    acertos = 0
    for ex in dados:
        pred = prever(arvore, ex)
        real = ex[ALVO]
        status = "✓" if pred == real else "✗"
        print(f"  {status} Previsto: {pred:3s}  Real: {real:3s}  | {ex}")
        if pred == real:
            acertos += 1
    print(f"\nAcurácia: {acertos}/{len(dados)} = {acertos/len(dados):.0%}")

    print("\n=== Exemplo de previsão para novo dado ===")
    novo = {"Clima": "Chuvoso", "Temperatura": "Média", "Vento": "Fraco"}
    print(f"  Entrada: {novo}")
    print(f"  Previsão: {prever(arvore, novo)}")
