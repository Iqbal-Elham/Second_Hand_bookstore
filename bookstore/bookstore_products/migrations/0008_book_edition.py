# Generated by Django 3.2.15 on 2022-12-26 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_products', '0007_book_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
