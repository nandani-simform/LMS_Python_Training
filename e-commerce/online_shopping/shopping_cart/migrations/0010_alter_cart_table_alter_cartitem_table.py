# Generated by Django 4.2.5 on 2023-12-01 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0009_remove_cart_cart_item_remove_cartitem_usercart_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='cartitem',
            table='cartitem',
        ),
    ]
