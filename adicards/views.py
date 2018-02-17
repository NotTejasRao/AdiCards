from django.shortcuts import render, HttpResponseRedirect
from adicards.models import Deck
from adicards.forms import DeckForm
from datetime import datetime


def deck_view(request, deck_id):
    """
    Return a context containing the deck and the related flashcards.
    """

    deck = Deck.objects.get(id=deck_id)
    context = {'deck': deck,
               'flashcard_set': deck.flashcard_set.all()}
    return render(request, 'deck.html', context)


def deck_form(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck_name = form.cleaned_data['deck_name']
            new_deck = Deck(name=deck_name, date_created=datetime.now())
            new_deck.save()
            return HttpResponseRedirect('/adicards/decks')
    else:
        form = DeckForm()

    return render(request, 'create_deck.html', {'form': form})
