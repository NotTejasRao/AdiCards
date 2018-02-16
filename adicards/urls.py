from django.urls import re_path, include, path
from django.views.generic import ListView, DetailView
from adicards.models import Deck, FlashCard
from . import views

urlpatterns = [re_path(r'^decks$',
                       ListView.as_view(queryset=Deck.objects.all().order_by('-date_created'),
                                        template_name='decks.html')),
               path('decks/<int:deck_id>/',
                    views.deck_view)]
