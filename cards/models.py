from django.db import models

# Create your models here.
class Card(models.Model):
    # deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.CharField(max_length=256)
    answer = models.CharField(max_length=256)

    def __str__(self):
        return "(" + self.question + ")"