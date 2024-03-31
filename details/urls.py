from django.urls import path
#from . import views
from .views import HomeView

#urlpatterns = [
#    path('', views.home, name="home"),
#]

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]