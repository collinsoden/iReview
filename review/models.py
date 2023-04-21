from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=45)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class Person(models.Model):
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255)

class Socials(models.Model):
    username = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    linkedin = models.CharField(max_length=30)