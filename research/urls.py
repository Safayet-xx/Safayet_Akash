# research/urls.py

from django.urls import path
from . import views
#from .views import ResearchPaperListAPI

urlpatterns = [
    path('', views.rehome, name='rehome'),
    #path('api/research/', ResearchPaperListAPI.as_view(), name='research-api'),
]



