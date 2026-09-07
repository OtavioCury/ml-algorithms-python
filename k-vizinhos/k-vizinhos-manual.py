from scipy.spatial import distance
import statistics
import matplotlib.pyplot as plt
import numpy as np

def knn(x_trainamento, y_trainamento, x_teste, k):
    distancias = []
    x1 = x_teste
    for x2 in x_trainamento:
        dist = distance.euclidean(x1, x2)
        distancias.append(dist)
    indices = []
    c1 = []
    for i in range(0, k):
        ind = np.argmin(distancias)
        distancias[ind] = np.max(distancias)
        indices.append(ind)
        c1.append(y_trainamento[ind])
    print("Classes: ",c1)
    classificacao = statistics.mode(c1)
    return classificacao

k=3 # numero de vizinhos
x_trainamento = np.array([[1,0.5],[0.8,0.8],[1.2,1.4],[0.6,0.4],[0.4,1.2],[1.5,1]])
y_trainamento = np.array(['white','gray','white','gray','gray','white'], dtype = 'str')
x_teste = np.array([1,1])
# realiza a classificacao
cl = knn(x_trainamento, y_trainamento, x_teste, k)
print("Classification:", cl)
# mostra os dados
plt.scatter(x_trainamento[:,0],x_trainamento[:,1],c=y_trainamento, s=150, marker='o', edgecolor='black')
plt.plot(x_teste[0],x_teste[1], marker='s', markersize=15, color="black")
plt.xlim(0.2,1.6)
plt.ylim(0,1.6)
plt.savefig('knn.eps')

plt.show()