from django.forms import ModelForm
from .models import Card, Deck


class CustomCard(ModelForm):

    class Meta:
        model = Card
        fields = [
            'question',
            'answer',
            'deck',
        ]

class CustomDeck(ModelForm):

    class Meta:
        model = Deck
        fields = [
            'name',
        ]