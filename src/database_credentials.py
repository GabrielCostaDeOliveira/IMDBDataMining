db_user = 'root'
db_password = 'cosmo'

db_host = 'localhost'
db_port = '3306'
db_name = 'imdb_ijs'

# Create a connection string
db_url = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
