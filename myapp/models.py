from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    profile = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree_year = models.CharField(max_length=4)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    organization = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    exp_year = models.CharField(max_length=4)

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)

class Tool(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='tools')
    tool_name = models.CharField(max_length=100, blank=True, null=True)
