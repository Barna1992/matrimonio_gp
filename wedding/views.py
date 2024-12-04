from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

def index(request):
    return render(request, 'wedding/index.html')

def rsvp(request):
    return render(request, 'wedding/rsvp.html')

def gift_list(request):
    return render(request, 'wedding/gift_list.html')



def cart(request):
    return render(request, 'wedding/cart-page.html')

def summary(request):
    return render(request, 'wedding/summary-page.html')

def thanks(request):
    return render(request, 'wedding/thanks.html')


def survey(request):
    return render(request, 'wedding/survey.html')


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer