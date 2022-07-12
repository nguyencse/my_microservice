import os
from databases import Database
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

# DATABASE_URI = "postgresql://nguyencse:1234abcd@localhost:5432/book_db"
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

books = Table("books", metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('author', String(100)),
    Column('publisher_id', Integer),
    Column('language', String(50)),
)

database = Database(DATABASE_URI)