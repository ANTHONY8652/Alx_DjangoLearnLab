from rest_framework import serializers
from .models import Book, Comment
from datetime import date

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'updated_at','is_flagged']

class BookSerializer(serializers.ModelSerializer):
    days_since_creation = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'published_date', 'created_at', 'days_since_creation']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long")
        return value
    
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long")
        return value
    
    def validate_author(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Author name must be at least 8 characters long")
        return value

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Publish date cannot be in the future")
        return value

    def get_days_since_creation(self, obj):
        if obj.created_at:
            return (date.today() - obj.created_at.date()).days
        return None
    
    def get_days_since_its_creation(self, obj):
        from datetime import datetime, timezone
        return (datetime.now(timezone.utc) - obj.created_at).days
    