from django.urls import path
from . import views

urlpatterns = [
    path('spiderman/',views.spiderman),
    path('ironman/',views.ironman),
    path('villian/',views.villian),

]
