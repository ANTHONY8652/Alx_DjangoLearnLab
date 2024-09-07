from rest_framework import viewsets
from .models import Drink
from .serializers import DrinkSerializer

class DrinkList(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
# Create your views here.
