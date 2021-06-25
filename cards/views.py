from django.shortcuts import render

# Create your views here.
def list_decks(request):
    return render(request, "cards/list_decks.html")