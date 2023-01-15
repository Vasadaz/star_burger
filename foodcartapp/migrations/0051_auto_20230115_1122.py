# Generated by Django 3.2.15 on 2023-01-15 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0050_auto_20230114_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='restaurants',
        ),
        migrations.AlterField(
            model_name='orderrestaurants',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='foodcartapp.order', verbose_name='заказ'),
        ),
    ]
