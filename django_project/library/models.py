from django.db import models

# Create your models here.

class Library(models.Model):
	libraryID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=50)
	streetAddress = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Patron(models.Model):
	patronID = models.AutoField(primary_key=True)
	libraryID = models.ForeignKey(Library, on_delete=models.CASCADE)
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	birthDate = models.DateField()
	phoneNumber = models.IntegerField(default=0)
	email = models.EmailField()
	def __str__(self):
		return (self.firstName+" "+self.lastName)

class Book(models.Model):
	isbn = models.IntegerField(default=0,primary_key=True)
	title = models.CharField(max_length=250)
	author = models.CharField(max_length=50)
	publishedDate = models.DateField()
	edition = models.IntegerField(default=0)
	deweyDecimalNumber = models.DecimalField(max_digits=10,decimal_places=5)
	ageGroups = models.CharField(max_length=50)
	def __str__(self):
		return self.title

class Holds(models.Model):
	patronID = models.ForeignKey(Patron, on_delete=models.CASCADE)
	ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
	libraryID = models.ForeignKey(Library, on_delete=models.CASCADE)
	datePlaced = models.DateField()
	holdID = models.AutoField(primary_key=True)
	def __str__(self):
		return self.holdID

class Copy(models.Model):
	ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
	copyNumber = models.IntegerField(default=0)
	libraryID = models.ForeignKey(Library, on_delete=models.CASCADE)
	purchaseDate = models.DateField()
	condition = models.CharField(max_length=250)
	status = models.CharField(max_length=250)
	copyID = models.AutoField(primary_key=True)
	def __str__(self):
		return self.copyID

class CheckedOut(models.Model):
	ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
	copyNumber = models.IntegerField(default=0)
	patronID = models.ForeignKey(Patron, on_delete=models.CASCADE)
	checkOutDate = models.DateField()
	dueDate = models.DateField()
	timesRenewed = models.IntegerField(default=0)
	overdueFee = models.DecimalField(max_digits=10,decimal_places=2)
	def __str__(self):
		return self.copyID
