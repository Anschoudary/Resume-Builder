from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    profile = models.TextField()
    about = models.TextField()
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree_year = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    exp_year = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    desc = models.TextField()
    skill = models.TextField()
    tool = models.TextField()

    def __str__(self):
        return self.name
    