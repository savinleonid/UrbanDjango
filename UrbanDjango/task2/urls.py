from django.urls import path
from .views import class_based_view, function_based_view

urlpatterns = [
   path('class/', class_based_view, name='class_view'),
   path('function/', function_based_view, name='function_view'),
]