from rest_framework import serializers 
from certification.models import certification_model

class certificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = certification_model
        fields = ('id', 
                  'title', 
                  'description',
                  'bg_photo',
                  'user_name',
                  'date')