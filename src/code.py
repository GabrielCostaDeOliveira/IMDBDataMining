from sqlalchemy import create_engine, text
from database_credentials import db_url
import pandas as pd;
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt

engine = create_engine(db_url)

#Extract the selected attributes from the database 

## get all movies
with engine.connect() as connection:
    query = """
SELECT m.*, 
    (
        SELECT COUNT(DISTINCT sub_md.director_id)
        FROM movies_directors sub_md 
        WHERE sub_md.movie_id = m.id
    ) AS director_count,
    (
        SELECT COUNT(*) 
        FROM movies_directors sub_md 
        WHERE sub_md.director_id IN (
            SELECT director_id
            FROM movies_directors
            WHERE movie_id = m.id
        )
        AND sub_md.movie_id <> m.id
        AND (
            SELECT year
            FROM movies
            WHERE id = sub_md.movie_id
        ) <= m.year
    ) AS director_count_movie
FROM movies m
WHERE m.`rank` IS NOT NULL;
"""

    movies = connection.execute(text(query))
    rows = movies.fetchall()
    movies = pd.DataFrame(rows, columns=movies.keys()).set_index('id')


movies['class'] = movies['rank'].apply(
    lambda x: 'Recomendado' if x >= 7 else 'Não Recomendado'
)

## get genre for movies

with engine.connect() as connection:
    query = """
            SELECT movie_id, GROUP_CONCAT(genre SEPARATOR ',') AS genres
                FROM movies_genres
            GROUP BY movie_id;
            """

    result = connection.execute(text(query))
    rows = result.fetchall()

    genres = pd.DataFrame(rows, columns=['movie_id', 'genre']).set_index('movie_id')


# Add genre in movies and remove movies that no have genre
movies = movies.join(genres, how='inner')

# make a dummies
dummies = movies['genre'].str.get_dummies(sep=',')

# Concatenate the dummies with the original dataframe
movies = pd.concat([movies, dummies], axis=1)

# Drop unnecessary columns for this analisy
movies = movies.drop(['name', 'rank', 'genre'], axis= 1)


# 
movies['year'] = ((movies['year'] // 1000)%10 - 1) * 10 + (movies['year'] // 10) % 10

# 
#movies = movies.drop(['year'], axis = 1)

#
x = movies.drop('class', axis=1)
y = movies['class']

#Step Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state = 43)

#Create an instance of the RandomForestClassifier/RandomForestRegressor
florest = RandomForestClassifier(n_estimators=10, random_state= 10)  # or RandomForestRegressor

#Fit the model to the training data
florest.fit(x_train, y_train)

#Make predictions on the testing data

y_predicted = florest.predict(x_test)
precision = metrics.accuracy_score(y_test, y_predicted)
print("Acurácia:",precision)

# plot results

feature_imp = pd.Series(florest.feature_importances_,index=x_train.columns).sort_values(ascending=False)
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.title("Acurácia: " + str(precision))
plt.xlabel('Relevância da característica')
plt.ylabel('Características')
plt.savefig('./sum_directores')
