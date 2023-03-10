from django.urls import path, include
from .views import UsersAPIView

urlpatterns = [
    path('', UsersAPIView.as_view()),
]