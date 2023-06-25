from sqlalchemy import create_engine, text
from database_credentials import db_url

engine = create_engine(db_url)

sql_script = """
    -- 
    SELECT * FROM movies;
"""

with engine.connect() as connection:
    result = connection.execute(text(sql_script))

    # Process the result
    for row in result:
        print(row)
