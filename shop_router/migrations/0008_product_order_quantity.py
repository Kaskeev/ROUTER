# Generated by Django 3.0.2 on 2020-10-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_router', '0007_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
