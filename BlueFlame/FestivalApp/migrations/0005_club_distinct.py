# Generated by Django 4.2.1 on 2023-05-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FestivalApp', '0004_club_belong'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='distinct',
            field=models.IntegerField(blank=True, null=True, verbose_name='DIS'),
        ),
    ]
