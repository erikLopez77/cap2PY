#
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