from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Cat(models.Model):
    name = models.CharField(max_length=200)
    food = models.TextField()
    birthdate = models.DateTimeField()
    adoptdate = models.DateTimeField(
            blank=True, null=True)
    ownes = models.TextField();

    def adopt(self):
        self.adoptdate = timezone.now()
        self.save()

    def __str__(self):
        return self.ownes