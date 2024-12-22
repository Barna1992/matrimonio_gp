from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Item, RSVP, Friend
from .serializers import ItemSerializer, RSVPSerializer, FriendSerializer
from rest_framework.response import Response


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


def dashboard(request):
    rsvps = RSVP.objects.all()
    friends = Friend.objects.all()
    context = {
        'rsvps': rsvps,
        'friends': friends
    }
    return render(request, 'wedding/dashboard.html', context)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer

class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.pop('string_ids', [])
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for item in items:
                item_id, item_quantity = item.split('-')
                current = Item.objects.get(id=item_id)
                current.quantity -= int(item_quantity)
                current.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
