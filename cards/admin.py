from django.contrib import admin
from .models import Card, Category, User, Deck

# Register your models here.
admin.site.register(Card)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Deck)