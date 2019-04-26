from django.urls import path
from django.views.generic import ListView, TemplateView

import adicards.views as views
from adicards.models import Deck

urlpatterns = [path('', TemplateView.as_view(template_name="index.html")),
               path('decks/',
                    ListView.as_view(queryset=Deck.objects.all().order_by('-date_created'),
                                     template_name='deck_list.html')),
               path('decks/<int:deck_id>/',
                    views.deck_view),
               path('create/deck/',
                    views.deck_create_view),
               path('create/flashcard/',
                    views.flashcard_create_view)]
