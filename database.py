from peewee import SqliteDatabase, Model, CharField
from pydantic import BaseModel

db = SqliteDatabase("database.db")

class Book(Model):
    title = CharField()
    author = CharField()

    class Meta:
        database = db

class BookInput(BaseModel):
    title: str
    author: str

db.connect()
db.create_tables([Book])
