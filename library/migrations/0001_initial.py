# Generated by Django 4.2.9 on 2024-01-31 14:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13, unique=True, validators=[library.models.validate_isbn, django.core.validators.RegexValidator(regex='^\\d{10,13}$')])),
                ('published_date', models.DateField()),
                ('genre', models.CharField(choices=[('fantasy', 'fantasy'), ('historical', 'historical'), ('journal', 'journal')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.IntegerField()),
                ('publisher', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('borrow_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_by', to='library.book')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
