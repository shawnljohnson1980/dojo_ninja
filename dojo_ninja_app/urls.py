from . import views
from django.urls import path



urlpatterns=[
    path('',views.index),
    path('create_ninja',views.create_ninja),
    path('create_dojo',views.create_dojo),

]