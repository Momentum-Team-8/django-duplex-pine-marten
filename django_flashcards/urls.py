"""django_flashcards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from cards import views as decks_views
from cards import views as cards_views

urlpatterns = [
    path("", decks_views.homepage, name="home"),
    path('accounts/', include('registration.backends.default.urls')),
    path('cards/', decks_views.list_decks, name='list_decks'),
    path('cards/<int:pk>/list_cards/', cards_views.list_cards, name='list_cards'),
    path('category/<slug:slug>', cards_views.categories_cards, name="categories_cards"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        #   For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
