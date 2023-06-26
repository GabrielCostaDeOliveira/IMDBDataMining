db_user = 'your_username'
db_password = 'your_password'

db_host = 'localhost'
db_port = '3306'
db_name = 'your_database_name'

# Create a connection string
db_url = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
