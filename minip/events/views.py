from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import event_details
from .models import news_details
from serializers import event_details_serializer
from serializers import news_details_serializer
from django.http import HttpResponse
from django.template import loader




# Create your views here.

# def event(request):
#     template = loader.get_template('events/event.html')
#     return HttpResponse(template.render(request))

class eventList(APIView):

    def get(self, request):
        eventss = event_details.objects.all()
        serializer = event_details_serializer(eventss, many=True)
        return Response(serializer.data)


    def post(self):
        serializer = event_details_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class newsList(APIView):

    def get(self, request):
        newss = news_details.objects.all()
        serializer = news_details_serializer(newss , many=True)
        return Response(serializer.data)

    def post(self):
        pass
