from django.test import TestCase
from .models import CorpusData

class CorpusTestCase(TestCase):
    def setUp(self):
         CorpusData.objects.create(key='ten', value=10)
         CorpusData.objects.create(key ='thousand',value=1000)

    def test_corpus_data(self):
        key_value1 = CorpusData.objects.get(key='ten')
        key_value2 = CorpusData.objects.get(key='thousand')
        self.assertEqual(key_value1.value, 10)
        self.assertEqual(key_value2.value, 1000)
        
