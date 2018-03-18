from rest_framework import serializers
from .models import user_details

class user_details_serializer(serializers.ModelSerializer):

    class Meta:
        model = user_details
        # fields = ('title' , 'details')
        fields = '__all__'
