from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
class Card(models.Model):
    #  = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="cards")
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=256)
    categories = models.ManyToManyField("Category", related_name="cards")

    def __str__(self):
        return "(" + self.question + ")"

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75)

    def __repr__(self):
        return f"<Category name={self.name}>"

    def __str__(self):
        return self.name

