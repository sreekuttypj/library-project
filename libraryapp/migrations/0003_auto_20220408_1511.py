# Generated by Django 3.1.2 on 2022-04-08 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_books_tb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books_tb',
            name='admin_id',
        ),
        migrations.RemoveField(
            model_name='books_tb',
            name='stud_id',
        ),
    ]