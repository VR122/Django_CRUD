from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path('inventory/items', ItemList.as_view()),
    path('inventory/items/<int:pk>', ItemDetail.as_view()),
    path('inventory/items/query/<str:category>', ItemDetail.as_view())
]