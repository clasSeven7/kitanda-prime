# Generated by Django 5.0.4 on 2024-05-01 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_remove_categorie_url_remove_comment_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stars',
            field=models.IntegerField(),
        ),
    ]