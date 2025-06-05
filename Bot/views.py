from django.shortcuts import render, redirect
from .models import Bot
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bot
from .serializers import BotSerializer
from django.shortcuts import get_object_or_404


class BotDetailView(APIView):
    def get(self, request, pk):
        bot = get_object_or_404(Bot, pk=pk)
        serializer = BotSerializer(bot)
        return Response(serializer.data, status=status.HTTP_200_OK)
