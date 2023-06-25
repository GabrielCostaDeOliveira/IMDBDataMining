from pandas.core.common import random_state
from sqlalchemy import create_engine, text
from database_credentials import db_url
from sklearn.preprocessing import OneHotEncoder;
import pandas as pd;
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

engine = create_engine(db_url)

#Extract the selected attributes from the database 

## get all movies
with engine.connect() as connection:
    movies = connection.execute(text("SELECT * FROM movies where rank is not null"))
    rows = movies.fetchall()
    movies = pd.DataFrame(rows, columns=movies.keys()).set_index('id')

## create a classe with rank

movies['class'] = movies['rank'].apply(
        lambda x: 'Very Bad' if 0 <= x < 2 else
                  'Bad' if 2 <= x < 4 else
                  'Average' if 4 <= x < 7 else
                  'Good' if 7 <= x < 9 else
                  'Excellent' if 9 <= x <= 10 else 'Unknown'
)

print(movies)

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

    print(genres)

# Add genre in movies and remove movies that no have genre
movies = movies.join(genres, how='inner')

print(movies)

# make a dummies
dummies = movies['genre'].str.get_dummies(sep=',')

# Concatenate the dummies with the original dataframe
movies = pd.concat([movies, dummies], axis=1)

# Drop unnecessary columns for this analisy
movies = movies.drop(['name', 'rank', 'genre'], axis= 1)

print(movies)

#
x = movies.drop('class', axis=1)
y = movies['class']

#Step Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

#Create an instance of the RandomForestClassifier/RandomForestRegressor
florest = RandomForestClassifier(n_estimators=100, random_state= 100)  # or RandomForestRegressor

#Fit the model to the training data
florest.fit(x_train, y_train)

#Make predictions on the testing data

y_predicted = florest.predict(x_test)
print("Acurácia:",metrics.accuracy_score(y_test, y_predicted))
