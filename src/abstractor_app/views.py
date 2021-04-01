from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import User, Document, Abstraction
from .serializers import UserSerializer, DocumentSerializer, AbstractionSerializer
from django.views import View
from django.http import HttpResponse
from script.environment import execute_web_program
from time import sleep

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]


class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class AbstractionView(viewsets.ModelViewSet):
    queryset = Abstraction.objects.all()
    serializer_class = AbstractionSerializer


class ExecuteView(GenericAPIView):
    queryset = Abstraction.objects.all()
    serializer_class = AbstractionSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data["abstraction"])
        county = request.data["abstraction"]["countyInformation"]
        client = request.data["abstraction"]["clientInformation"]
        legal = request.data["abstraction"]["legalDescription"]
        upload_file = request.data["abstraction"]["uploadFile"].split('\\')[-1]
        # print(request.data["abstraction"]["uploadFile"])
        # print(county)
        # print(client)
        # print(legal)
        # print(upload_file)
        dictionary_object = execute_web_program(county, client, legal, upload_file[:-5])
        return Response(data=dictionary_object, status=status.HTTP_200_OK)


class ProfileView(viewsets.ViewSet):
    queryset = User.objects.all()
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)