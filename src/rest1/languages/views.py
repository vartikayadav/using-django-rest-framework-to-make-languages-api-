from django.shortcuts import render
from languages.serailizers import LanguageSerializer,ParadigmSerializer,ProgrammerSerializer
from languages.models import Languages,Paradigm,Programmer
from rest_framework import viewsets,permissions
# Create your views here.
class LanguageView(viewsets.ModelViewSet):#any view name
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
class ParadigmView(viewsets.ModelViewSet):#any view name
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
class ProgrammerView(viewsets.ModelViewSet):#any view name
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
