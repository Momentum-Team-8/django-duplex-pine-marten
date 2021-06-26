from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Card


# Create your views here.
# def list_decks(request):
#     return render(request, "cards/list_decks.html")

def homepage(request):
    if request.user.is_authenticated:
        return redirect ("list_cards")
    return render(request, "cards/homepage.html")

@login_required
def list_cards(request):
    cards = Card.objects.all()
    return render(request, "cards/list_decks.html",
                {"cards": cards})
