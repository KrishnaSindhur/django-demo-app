from rest_framework import serializers
from .models import CorpusData

class CorpusDataSerializer(serializers.ModelSerializer):
    """
    In Serializer key and value are the data fields 
    """
    class Meta:
        model = CorpusData
        fields = (
            'key', 'value')
