# Generated by Django 2.0.8 on 2018-09-15 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpusdata',
            name='key',
            field=models.CharField(max_length=256, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='corpusdata',
            name='value',
            field=models.BigIntegerField(),
        ),
    ]