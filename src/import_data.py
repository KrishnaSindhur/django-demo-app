"""
This script is run intial startup of app this will load all data from csv file
to the database of web_app
"""
import os,sys
import csv

cwd = os.getcwd()
project_dir = cwd+'/src/django_project/'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()

from web_app.models import CorpusData

try:
    path = cwd + '/src/data_files/Corpus.csv'
    with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                data = CorpusData.objects.create(key=row['key'], value=row['value'])
except Exception as e:
    raise(e)
