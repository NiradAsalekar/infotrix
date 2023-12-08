from django.urls import path
from .views import QuoteListCreateView
from . import views

urlpatterns = [
    path('', QuoteListCreateView.as_view(), name='quote-list-create'),
]
