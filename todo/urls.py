from django.urls import path
from .views import TodoCRUD
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", TodoCRUD)

urlpatterns = [
    
] + router.urls