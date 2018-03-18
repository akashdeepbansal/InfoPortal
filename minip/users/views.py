from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import user_details
from serializers import user_details_serializer


# Create your views here.

# def index(request):
#     template = loader.get_template('users/index.html')
#     return HttpResponse(template.render(request))
class userList(APIView):

    def get(self, request):
        userss = user_details.objects.all()
        serializer = user_details_serializer(userss, many=True)
        return Response(serializer.data)


    def post(self):
        pass
