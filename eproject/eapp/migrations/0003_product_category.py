# Generated by Django 5.0.1 on 2024-01-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(1, 'mobile'), (2, 'shoes'), (3, 'watches')], default=1),
            preserve_default=False,
        ),
    ]
