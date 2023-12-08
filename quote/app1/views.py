from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer
import requests
# Create your views here.

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get(self, request, *args, **kwargs):
        # Fetch a random quote from ZenQuotes API
        response = requests.get('https://zenquotes.io/api/random')
        data = response.json()

        # Create a Quote instance from the API response
        quote = Quote(text=data[0]['q'], author=data[0]['a'])
        quote.save()

        serializer = self.get_serializer(quote)
        return Response(serializer.data)
