from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255)


class Book(models.Model):
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    copy_num = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT)


