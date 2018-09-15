from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CorpusDataSerializer
from django.views import View
from django.http import JsonResponse
from .models import CorpusData

class DetailView(View):
    """
    Here it passes key to filter database and gets it corresponding values value
    """
    def get(self, request, key):
        query = CorpusData.objects.filter(key__iexact=key).first()
        serializer = CorpusDataSerializer(query)
        return JsonResponse(serializer.data, safe=False)
