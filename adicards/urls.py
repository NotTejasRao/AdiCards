from django.urls import re_path, include, path
from django.views.generic import ListView, DetailView
from adicards.models import Deck

urlpatterns = [re_path(r'^decks$',
                       ListView.as_view(queryset=Deck.objects.all().order_by('-date_created'),
                                        template_name='decks.html')),
               re_path(r'^decks/(?P<pk>\d+)$',
                       DetailView.as_view(model=Deck,
                                          template_name='deck.html'))]
