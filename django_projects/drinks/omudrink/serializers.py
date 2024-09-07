from .models import Drink
from rest_framework import serializers

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description', 'created_at']
        
    def validate_name(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Name must be at least 8 characters long")
        return value
    
    def validate_description(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Description must be at leat 15 characters long")
        return value