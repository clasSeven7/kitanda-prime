# Generated by Django 5.0.4 on 2024-05-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0006_alter_comment_stars_alter_product_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.FloatField(),
        ),
    ]
