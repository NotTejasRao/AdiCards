from django.shortcuts import render
from adicards.models import Deck


def deck_view(request, deck_id):
    """
    Return a context containing the deck and the related flashcards.
    """

    deck = Deck.objects.get(id=deck_id)
    context = {'deck': deck,
               'flashcard_set': deck.flashcard_set.all()}
    return render(request, 'deck.html', context)
