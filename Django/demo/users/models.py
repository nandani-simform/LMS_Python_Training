from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
class Category(models.Model):
    cname = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.cname

