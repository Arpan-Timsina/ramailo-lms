# Generated by Django 5.0.1 on 2024-01-31 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_isbn'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookDetails',
            new_name='BookDetail',
        ),
        migrations.RenameModel(
            old_name='BorrowedBooks',
            new_name='BorrowedBook',
        ),
    ]