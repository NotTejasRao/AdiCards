from django.forms import Form, CharField


class DeckForm(Form):
    deck_name = CharField(label='Deck Name', max_length=124)
