from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    publisher=models.CharField(max_length=50)
    ebook=models.BooleanField(default=True)
    covering=models.CharField(max_length=50)
    class Meta:
        db_table="books"

    def __str__(self):
        return "Title: {} Author: {} Price: {}".format(self.title,self.author,self.price)

class Teacher(models.Model):
    TeacherID=models.IntegerField(primary_key=True)
    name=models.EmailField(max_length=50)
    qualification=models.CharField(max_length=50)

class Subject(models.Model):
    Subjectcode=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    credits=models.IntegerField()
    teacher=models.ManyToManyField(Teacher)
