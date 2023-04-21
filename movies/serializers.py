from rest_framework import serializers
from .models import Movie, Actor, Review

class MovieTitle(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)
        
class ActorSerializer(serializers.ModelSerializer):
    movie = MovieTitle(many=True, read_only=True, source='movie_set')
    class Meta:
        model = Actor
        fields = '__all__' 
         

class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)

           
        
class MovieSerializer(serializers.ModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('actors',)
        

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


              
        
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview')
 

class ReviewSerializer(serializers.ModelSerializer):   
    movie = MovieTitle(many=False, read_only=True)
    class Meta:
        model = Review
        fields = '__all__'



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')
        read_only_fields = ('movie',)