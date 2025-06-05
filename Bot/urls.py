from django.urls import path
from .views import BotDetailView

urlpatterns = [
    path('bots/<int:pk>/', BotDetailView.as_view(), name='bot-detail'),
]
