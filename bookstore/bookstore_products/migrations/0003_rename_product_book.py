# Generated by Django 4.1.1 on 2022-11-07 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_products', '0002_product_publisher'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='book',
        ),
    ]
