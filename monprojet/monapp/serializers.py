from rest_framework import serializers
from .models import Personnes, Dog

class PersonnesSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Personnes
        fields = '__all__'
        
        
class DogSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Dog
        fields = '__all__'