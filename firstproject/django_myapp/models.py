#
from sqlite3 import connect

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Column,Integer,String

class Base(DeclarativeBase):
    pass
class Book(Base):
    __tablename__="Books"
    id=mapped_column(Integer,primary_key=True)
    title=mapped_column(String(50))
    author=mapped_column(String(50))
    price=mapped_column(Integer)
    publisher=mapped_column(String(50))
    year_of_pub=mapped_column(Integer)

from pymongo import MongoClient

uri ="mongodb+srv://ErikLopez:ErikLopez@django.13lskiw.mongodb.net/?appName=Django"
client = MongoClient(uri)
#name db (mydb) books is collection name
db = client.mydb
col = db['books']

from mongoengine import *
#con = connect(db='mydb',username='ErikLopez',password='ErikLopez', host=uri)

class Book(DynamicDocument):
    title = StringField(max_length=50)
    author = StringField(max_length=50)
    price = IntField()
    publisher = StringField(max_length=50)
    meta = {'collection': 'Books'}

#doc = Book(title="Beginning Django", author="Rubio ",
#price=3053, publisher="Apress", year=2017)
#doc.save()