from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .pagination import CustomPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter

# Create your views here.
def home(request):
    return HttpResponse("<h2>Todo API</h2>")

# class TodoView(ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def get_queryset(self):
#         param = self.request.query_params.get("completed")
#         if param == "true":
#             return Todo.objects.filter(done=True)
#         return super().get_queryset()
    
#     def get_serializer(self, *args, **kwargs):
#         print("place your additional coding here!!!!")
#         return super().get_serializer(*args, **kwargs)
    
    
#     def perform_create(self, serializer):
#         print("If you want to todo sthg just before save update here!")
#         serializer.save(priority="L", task=serializer.validated_data.get("task").upper())


# class TodoDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     lookup_field = "id"

class TodoCRUD(ModelViewSet):
    # queryset = Todo.objects.all()
    queryset = Todo.objects.filter(done=False)
    serializer_class = TodoSerializer
    # pagination_class=CustomPageNumberPagination
    # pagination_class=MyLimitOffsetPagination 
    # pagination_class=MyCursorPagination 
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = ('task', 'done', 'priority')
    search_fields = ['task', 'description', ]
    
    def get_queryset(self):
        param = self.request.query_params.get("completed")
        if param == "yes":
            return Todo.objects.filter(done=False)
        elif param == "no":
            return Todo.objects.filter(done=True)
        return super().get_queryset()