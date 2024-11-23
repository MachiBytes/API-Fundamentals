from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase("database.db")

class Book(Model):
    title = CharField()
    author = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Book])
