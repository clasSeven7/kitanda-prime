# Generated by Django 5.0.4 on 2024-05-07 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_cartitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.product')),
            ],
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
    ]
