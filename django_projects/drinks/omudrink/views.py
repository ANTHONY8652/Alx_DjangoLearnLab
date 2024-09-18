from rest_framework import generics, viewsets
from .models import Drink
from .serializers import DrinkSerializer

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkList(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data}, safe=False)

class DrinkCreate(generics.CreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkDelete(generics.DestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkUpdate(generics.UpdateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkRetrieve(generics.RetrieveAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class DrinkRetrieveOrDestroy(generics.RetrieveDestroyAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
