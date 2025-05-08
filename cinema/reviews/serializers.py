from rest_framework import serializers
from .models import Review
from movies.models import Movie

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','movie','rating','comment','created_at']
        read_only_fields = ['created_at']

    def validate(self,data):
        user = self.context['request'].user
        movie = data['movie']

        if Review.objects.filter(user=user,movie=movie).exists():
            raise serializers.ValidationError('شما قبلا برای این فیلم نظر داده اید')
        return data    