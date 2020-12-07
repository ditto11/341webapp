from django.db import models

# Create your models here.

class Library(models.Model):
	libraryid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	state = models.CharField(max_length=50)
	streetaddress = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Patron(models.Model):
	patronid = models.AutoField(primary_key=True)
	libraryid = models.ForeignKey(Library, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	birthdate = models.DateField()
	phonenumber = models.BigIntegerField(default=0)
	email = models.EmailField()
	def __str__(self):
		return (self.firstname+" "+self.lastname)

class Book(models.Model):
	isbn = models.BigIntegerField(default=0,primary_key=True)
	title = models.CharField(max_length=450)
	author = models.CharField(max_length=760)
	publisheddate = models.DateField()
	def __str__(self):
		return self.title

class Hold(models.Model):
	patronid = models.ForeignKey(Patron, on_delete=models.CASCADE)
	isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
	libraryid = models.ForeignKey(Library, on_delete=models.CASCADE)
	dateplaced = models.DateField()
	holdid = models.AutoField(primary_key=True)
	def __str__(self):
		return (self.patronid + " " + self.isbn)

class Copy(models.Model):
	isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
	libraryid = models.ForeignKey(Library, on_delete=models.CASCADE)
	purchasedate = models.DateField()
	condition = models.CharField(max_length=250)
	status = models.CharField(max_length=250)
	copyid = models.IntegerField(primary_key=True)
	def __str__(self):
		return (self.isbn + " " + self.copynumber)

class CheckedOut(models.Model):
	isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
	copyid = models.ForeignKey(Copy, on_delete=models.CASCADE,default=0)
	patronid = models.ForeignKey(Patron, on_delete=models.CASCADE)
	checkoutdate = models.DateField()
	duedate = models.DateField()
	timesrenewed = models.IntegerField(default=0)
	overduefee = models.DecimalField(max_digits=10,decimal_places=2)
	def __str__(self):
		return (self.isbn + " " + self.copyid)
