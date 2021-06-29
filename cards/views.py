from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Card, Category, Deck


# Create your views here.
# def list_decks(request):
#     return render(request, "cards/list_decks.html")

def homepage(request):
    if request.user.is_authenticated:
        return redirect ("list_decks")
    return render(request, "cards/homepage.html")

@login_required
def list_decks(request):
    decks = Deck.objects.all()
    return render(request, "cards/list_decks.html",
                {"decks": decks})

def categories_cards(request, slug):
    category = get_object_or_404(Category, slug=slug)
    cards = category.cards.all()

    return render(request, "cards/list_cards.html", {"category": category, "cards": cards})
