from django.db import models

# Create your models here.

class admin_registration_tb(models.Model):
	username=models.CharField(max_length=30,default='')
	email=models.CharField(max_length=50,default='')
	password=models.CharField(max_length=30,default='')

class stud_registration_tb(models.Model):
	username=models.CharField(max_length=30,default='')
	email=models.CharField(max_length=50,default='')
	password=models.CharField(max_length=30,default='')

class books_tb(models.Model):
	
	bookname=models.CharField(max_length=100,default='')
	author=models.CharField(max_length=30,default='')
	description=models.CharField(max_length=100,default='')
	file=models.ImageField(upload_to = 'files')
	