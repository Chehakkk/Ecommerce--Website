# Generated by Django 5.0.1 on 2024-01-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, 'mobile'), (2, 'shoes'), (3, 'clothes')]),
        ),
    ]