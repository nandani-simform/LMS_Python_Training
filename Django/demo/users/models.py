from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True, default="2014")

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

class Album(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.album_title

class Song(models.Model):
    song_title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    def __str__(self) -> str:
        return self.song_title

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.first_name
