from django.db import models

# Create your models here.

class Library(models.Model):
	libraryID = models.AutoField()
	name = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=50)
	streetAddress = models.CharField(max_length=100)

class Patron(models.Model):
	patronID = models.AutoField()
	libraryID = models.ForeignKey(Location, on_delete=models.CASCADE)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	birthDate = models.DateField()
	phoneNumber = models.IntegerField(default=0)
	email = models.EmailField()

class Book(models.Model):
	isbn = models.IntegerField(default=0)
	title = models.CharField(max_length=250)
	author = models.CharField(max_length=50)
	publishedDate = models.DateField()
	edition = models.IntegerField(default=0)
	deweyDecimalNumber = models.DecimalField(max_digits=10,decimal_places=5)
	ageGroups = models.CharField(max_length=50)


