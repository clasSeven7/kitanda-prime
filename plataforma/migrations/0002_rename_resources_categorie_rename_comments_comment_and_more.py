# Generated by Django 5.0.4 on 2024-04-29 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resources',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Categories',
            new_name='Resource',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
