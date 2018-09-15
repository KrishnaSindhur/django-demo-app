from django.db import models

class CorpusData(models.Model):
    """
    Corpus data model where key and value are two columns defined in web_app db
    """
    key = models.CharField(max_length=256,primary_key=True)
    value = models.BigIntegerField()


    class Meta:
        ordering = ('key',)

    def __str__(self):
        return "{}".format(self.value)
