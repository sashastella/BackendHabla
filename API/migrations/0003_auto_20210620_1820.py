# Generated by Django 3.1.7 on 2021-06-20 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20210620_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roles',
            field=models.ManyToManyField(related_name='profile_role', to='API.Role'),
        ),
    ]
