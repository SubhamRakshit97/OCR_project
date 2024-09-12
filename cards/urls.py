from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_card, name='upload_card'),
    path('cards/', views.list_cards, name='list_cards'),
]