from rest_framework import generics
from .models import items
from .serializer import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = items.objects.all()
        key = self.request.content_params.get('key')
        if key is not None:
            queryset = queryset.filter(key=key)
        return queryset

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = items.objects.all()
