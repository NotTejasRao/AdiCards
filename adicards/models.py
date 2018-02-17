from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=124)
    date_created = models.DateTimeField()

    def __str__(self):
        return '#' + str(self.id) + ' ' + str(self.name)


class Flashcard(models.Model):
    url_prompt = models.URLField(default='#')
    text_prompt = models.TextField()
    answer = models.TextField()
    decks = models.ManyToManyField(Deck, related_name="flashcards")

# Implement LearnMetaDate containing User -> Flashcard learning level
