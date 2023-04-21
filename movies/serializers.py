from rest_framework import serializers
from .models import Movie, Actor, Review

        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        
class ActorSerializer(serializers.ModelSerializer):
    movie_set = MovieSerializer(many=True, read_only=True)
    class Meta(ActorListSerializer.Meta):
        model = Actor
        fields = '__all__'
    
    # title 필드만 가져오기
    # ?


    # movie_set 이름을 movies로 바꾸기
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     print(instance)
    #     rep['movies'] = rep.pop('movie_set', [])
    #     return rep


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)