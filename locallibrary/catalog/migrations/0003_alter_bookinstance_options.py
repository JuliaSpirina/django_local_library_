# Generated by Django 4.1.1 on 2022-09-16 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_book_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('Librarian', 'Set book as returned'),)},
        ),
    ]