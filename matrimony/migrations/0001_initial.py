# Generated by Django 4.2.3 on 2023-09-12 17:19

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caste', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='father_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sects', to='matrimony.religion')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed', max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location=pathlib.PureWindowsPath('C:/Users/LENOVO/OneDrive/Desktop/django_web_developer/django_matrimony_app/media')), upload_to='')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('occupation', models.CharField(default='Not specified', max_length=100, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('is_married', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('caste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='matrimony.caste')),
                ('father', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dependent', to='matrimony.father_profile')),
                ('hobbies', models.ManyToManyField(null=True, related_name='profiles', to='matrimony.hobbies')),
                ('religion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='matrimony.religion')),
            ],
        ),
    ]
