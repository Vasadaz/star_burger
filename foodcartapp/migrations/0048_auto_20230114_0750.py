# Generated by Django 3.2.15 on 2023-01-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0047_data_order_restaurants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderrestaurants',
            options={'ordering': ['distance_to_client'], 'verbose_name': 'ресторан приготовит продукт из заказа', 'verbose_name_plural': 'рестораны приготовят продукты из заказа'},
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1 not processed', 'Необработан'), ('2 cooking', 'Готовится'), ('3 on way', 'В пути'), ('4 delivered', 'Доставлен')], db_index=True, default='not processed', max_length=15, verbose_name='статус'),
        ),
    ]
