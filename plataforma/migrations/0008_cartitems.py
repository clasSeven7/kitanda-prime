# Generated by Django 5.0.4 on 2024-05-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0007_alter_comment_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('products', models.ManyToManyField(to='plataforma.product')),
            ],
        ),
    ]
