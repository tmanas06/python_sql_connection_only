from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
import pymysql

# MySQL example
db_username = 'root'
db_password = 'manas'
db_host = 'localhost'
db_name = 'a1'  # Updated database name
db_port = '3306'  # MySQL default port

connection_str = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)

metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String(50)),
              Column('email', String(100)))

Session = sessionmaker(bind=engine)
session = Session()

# Create a database connection
connection = engine.connect()

# Describe a table
desc_statement = text("DESC aoop;")
result = connection.execute(desc_statement)
for row in result:
    print(row)

# Select all from a table
select_statement = text("SELECT * FROM aoop;")
result = connection.execute(select_statement)
for row in result:
    print(row)

# Close the connection
connection.close()

# Close the session
session.close()
