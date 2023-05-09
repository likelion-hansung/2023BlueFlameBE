# Generated by Django 4.2.1 on 2023-05-09 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='NAME')),
                ('description', models.CharField(max_length=100, verbose_name='DESCRIPTION')),
                ('content', models.TextField(blank=True, null=True, verbose_name='CONTENT')),
                ('information', models.TextField(blank=True, null=True, verbose_name='INFORMATION')),
                ('location', models.CharField(max_length=50, verbose_name='LOCATION')),
                ('contact', models.CharField(blank=True, max_length=50, null=True, verbose_name='CONTACT')),
                ('image', models.ImageField(blank=True, null=True, upload_to='club/', verbose_name='IMAGE')),
                ('date', models.CharField(max_length=10, verbose_name='DATE')),
            ],
            options={
                'verbose_name': 'Club',
                'verbose_name_plural': 'Clubs',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='NAME')),
                ('decription', models.CharField(max_length=100, verbose_name='DESCRIPTION')),
                ('price', models.CharField(max_length=50, verbose_name='PRICE')),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='NAME')),
                ('description', models.CharField(max_length=100, verbose_name='DESCRIPTION')),
                ('content', models.TextField(blank=True, null=True, verbose_name='CONTENT')),
                ('belong', models.CharField(max_length=50, verbose_name='BELONG')),
                ('location', models.CharField(max_length=50, verbose_name='LOCATION')),
                ('contact', models.CharField(blank=True, max_length=50, null=True, verbose_name='CONTACT')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pub/', verbose_name='IMAGE')),
                ('date', models.CharField(max_length=10, verbose_name='DATE')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FestivalApp.menu')),
            ],
            options={
                'verbose_name': 'Pub',
                'verbose_name_plural': 'Pubs',
            },
        ),
    ]
