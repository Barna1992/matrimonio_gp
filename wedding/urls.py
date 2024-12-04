from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('gift-list/', views.gift_list, name='gift_list'),
    path('gift-list/cart', views.cart, name='gift_list_cart'),
    path('gift-list/summary', views.summary, name='gift_list_summary'),
    path('gift-list/thanks', views.thanks, name='gift_list_thx'),
    path('api/', include(router.urls)),
]
