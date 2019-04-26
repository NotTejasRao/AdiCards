from django.forms import Form, CharField, ModelMultipleChoiceField, Textarea

from adicards.models import Deck


class DeckCreateForm(Form):
    name = CharField(label='Deck Name', max_length=124)


class FlashcardCreateForm(Form):
    text_prompt = CharField(label='Text Prompt Link', widget=Textarea)
    answer = CharField(label='Answer', widget=Textarea)
    decks = ModelMultipleChoiceField(queryset=Deck.objects.all())
