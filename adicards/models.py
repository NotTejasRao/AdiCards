from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=124)
    date_created = models.DateTimeField()


class FlashCard(models.Model):
    prompt = models.TextField()
    answer = models.TextField()
    deck = models.ManyToManyField(Deck)

# Implement LearnMetaDate containing User -> FlashCard learning level
