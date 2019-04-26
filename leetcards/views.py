from datetime import datetime

from django.shortcuts import render, HttpResponseRedirect

from leetcards.forms import DeckCreateForm, FlashcardCreateForm
from leetcards.models import Deck, Flashcard


def deck_view(request, deck_id):
    """
    Return a context containing the deck and the related flashcards.
    """

    deck = Deck.objects.get(id=deck_id)
    context = {'deck': deck,
               'flashcards': deck.flashcards.all()}
    return render(request, 'deck_show.html', context)


def deck_create_view(request):
    """
    Adds a deck to the database if request.method is POST, otherwise returns a render for the form.
    """

    if request.method == 'POST':
        form = DeckCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            new_deck = Deck(name=name, date_created=datetime.now())
            new_deck.save()
            return HttpResponseRedirect('/decks/')
    return render(request, 'deck_create.html', {'form': DeckCreateForm()})


def flashcard_create_view(request):
    """
    Adds a flashcard to the database if request.method is POST, otherwise returns a render for the form.
    """

    if request.method == 'POST':
        form = FlashcardCreateForm(request.POST)
        if form.is_valid():
            text_prompt = form.cleaned_data['text_prompt']
            answer = form.cleaned_data['answer']
            decks = form.cleaned_data['decks']

            if text_prompt and answer and decks:  # All arguments were provided
                new_flashcard = Flashcard(text_prompt=text_prompt, answer=answer)
                # https://stackoverflow.com/questions/18048172/django-forms-many-to-many-relationships
                new_flashcard.save()  # To generate ID beforehand
                # https://stackoverflow.com/questions/11315010/what-do-and-before-a-variable-name-mean-in-a-function-signature
                new_flashcard.decks.add(*decks)
                new_flashcard.save()
                return HttpResponseRedirect('/decks/')
    return render(request, 'flashcard_create.html', {'form': FlashcardCreateForm()})
