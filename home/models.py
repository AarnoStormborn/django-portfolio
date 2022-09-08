from datetime import date
from django.db import models

class SpecialSkills(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Special Skills"


class Project(models.Model):
    name = models.CharField(max_length=100)
    techStack = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    link = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'project_images', default='image4.jpg')
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message= models.TextField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"

class WorkExp(models.Model):
    cmpName = models.CharField(max_length=100)
    position= models.CharField(max_length=100)
    shortDesc= models.TextField(max_length=100)
    startDate = models.DateField(default=date.today)
    endDate = models.DateField(default=date.today)
    updatedAt = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cmpName

    class Meta:
        verbose_name_plural = "Work Experience"

class Education(models.Model):
    edChoices = [
        ('Junior School', 'Junior'),
        ('Senior School', 'Senior'),
        ('Graduate School', 'Graduate'),
    ]
    schName = models.CharField(max_length=100)
    hist = models.CharField(choices=edChoices, max_length=50, default='Junior')
    startDate = models.DateField(default=date.today)
    endDate = models.DateField(default=date.today)

    def __str__(self):
        return self.schName

    class Meta:
        verbose_name_plural = "Education"

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_percent = models.CharField(max_length=10)

    def __str__(self):
        return self.skill_name 

    class Meta:
        verbose_name_plural = "Skills"
