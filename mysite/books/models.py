from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(maxlenght = 30)
	address = models.CharField(maxlenght = 50)
	city = models.CharField(maxlenght = 60)
	state_province = models.CharField(maxlenght = 30)
	country = models.CharField(maxlenght = 50)
	website = models.URLField()

class Author(models.Model):
	salutation = models.CharField(maxlenght = 10)
	first_name = models.CharField(maxlenght = 30)
	last_name = models.CharField(maxlenght = 40)
	email = models.EmailField()
	headshot = models.ImageField(upload_to = '/tmp')

class Book(models.Model):
	tittle = models.CharField(maxlenght = 100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeingKey(Publisher)
	publication_date = models.DateField() 