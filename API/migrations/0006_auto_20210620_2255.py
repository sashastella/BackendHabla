# Generated by Django 3.1.7 on 2021-06-21 02:55
from django.contrib.postgres.operations import TrigramExtension, UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20210620_2127'),
    ]

    operations = [
        UnaccentExtension(),
        TrigramExtension()
    ]
