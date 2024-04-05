from django.urls import path
from .views import UserRegisterView, AuthenticationForm

urlpatterns = [
    path('members/', UserRegisterView.as_view(), name='register'),
]

