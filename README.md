
# IMDB Data Mining

Este é o trabalho final da disciplina de Sistemas de Bancos de Dados 2 da Universidade de Brasília (FGA), que envolve a mineração de dados de uma base de dados SQL relacionada ao IMDb. A base de dados está disponível em [IMDb](https://relational.fit.cvut.cz/dataset/IMDb) e utiliza o MariaDB como sistema de gerenciamento de banco de dados.

## Base de Dados

A base de dados IMDb contém uma riqueza de informações sobre filmes, diretores, atores, tornando-a ideal para a realização deste projeto.

## Objetivo do Projeto

O objetivo principal deste projeto é realizar a mineração de dados na base de dados IMDb para identificar as características que tornam um filme recomendado. Um filme recomendado é aquele com uma nota acima de 7 no IMDb. Para atingir esse objetivo, estamos utilizando o algoritmo de clusterização de Floresta Aleatória.

## Documentação

A documentação do projeto inclui o Diagrama de Entidade-Relacionamento (DER) e o Diagrama Lógico de Dados (DLD). Esses diagramas descrevem a estrutura da base de dados e como as entidades estão relacionadas entre si.

- Diagrama de Entidade-Relacionamento (DER):

![Diagrama Conceitual](https://github.com/GabrielCostaDeOliveira/IMDBDataMining/tree/main/docs/Conceitual_sbd2_tf.png)

- Diagrama Lógico de Dados (DLD):

![Diagrama Lógico](https://github.com/GabrielCostaDeOliveira/IMDBDataMining/blob/main/docs/TF_Logico.png)

## Resultados da Mineração

Os resultados da mineração de dados estão representados na imagem a seguir:

![Resultados da Mineração](https://github.com/GabrielCostaDeOliveira/IMDBDataMining/blob/main/results/results.png)

características que comtribuirm

Com base na análise dos resultados, identificamos as características que influenciam a recomendação de um filme (nota acima de 7 no IMDb):

**Características que Contribuem:**

1. **Média das avaliações dos filmes dirigidos pelos diretores daquele filme antes da realização:** Diretores com histórico de filmes bem avaliados tendem a produzir filmes recomendados.

2. **Média das avaliações dos filmes em que os atores daquele filme atuaram antes da realização:** A atuação em filmes bem avaliados pelos atores contribui para a recomendação.

**Características que não Contribuem Significativamente:**

1. **Quantidade média de filmes dirigidos pelos diretores que fizeram aquele filme:** O número de filmes dirigidos pelos diretores não tem forte correlação com a qualidade.

2. **Quantidade média de filmes feitos pelos atores que fizeram aquele filme:** O histórico de atuações dos atores não é um fator-chave na recomendação.

Essas descobertas podem guiar futuras produções cinematográficas, enfatizando a importância da qualidade da direção e das atuações para obter filmes bem avaliados.
