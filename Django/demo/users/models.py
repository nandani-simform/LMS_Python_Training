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


class MyNewModel(models.Model):
    my_field = models.CharField("Field Name",max_length=50, db_column='custom_column_name')
    name = models.CharField(max_length=50, null=True, verbose_name='naam') #verbose name dono trh se likh skte h
    class Meta:
        db_table = '"naya_model"' #table ka naam in database
        # verbose_name = 'hii'
        verbose_name_plural = 'my name' #model name