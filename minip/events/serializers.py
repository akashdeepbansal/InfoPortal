from rest_framework import serializers
from .models import event_details
from .models import news_details

class event_details_serializer(serializers.ModelSerializer):

    class Meta:
        model = event_details
        # fields = ('title' , 'details')
        fields = '__all__'

class news_details_serializer(serializers.ModelSerializer):

    class Meta:
        model = news_details
        fields = '__all__'
