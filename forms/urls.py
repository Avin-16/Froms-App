
from django.urls import path,include
from .views import *
urlpatterns=[

    path('questions/', Question.as_view()), #get,post
    path('choice/',Choice.as_view()),#post

]