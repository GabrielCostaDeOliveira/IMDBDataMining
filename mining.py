import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sqlalchemy import create_engine, text

engine = create_engine("mysql+mysqlconnector://root:1597@localhost:3306/imdb_ijs")

command = """
SELECT * FROM movies;
"""

with engine.connect() as connection: 
    movies = connection.execute(text(command))

colors = {0: "red", 5: "yellow", 10: "green"}
fig, ax = plt.subplots()

X = []
for row in movies:
    if row.id and row.year and row.rank:
        X.append([row.id, row.year, row.rank])

# Executando o algoritmo K-means
kmeans = KMeans(n_clusters=4, max_iter=2000, algorithm='lloyd',  n_init=10)
x = kmeans.fit_predict(X)

# Obtendo as etiquetas dos clusters e os centróides
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

 #Exibindo os resultados
for row in movies: 
    print(row)
for i, row in enumerate(X):
    print("Cluster label:", labels[i])


plt.scatter(
    X[x == 0, 0], X[x == 0, 1],
    s=50, c='lightgreen',
    marker='s', edgecolor='black',
    label='cluster 1'
)

plt.scatter(
    X[x == 1, 0], X[x == 1, 1],
    s=50, c='orange',
    marker='o', edgecolor='black',
    label='cluster 2'
)

plt.scatter(
    X[x == 2, 0], X[x == 2, 1],
    s=50, c='lightblue',
    marker='v', edgecolor='black',
    label='cluster 3'
)

# plot the centroids
plt.scatter(
    km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
    s=250, marker='*',
    c='red', edgecolor='black',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()
plt.show()
 #Fechando a conexão com o banco de dados
engine.dispose()



