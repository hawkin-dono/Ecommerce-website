# Generated by Django 5.0.3 on 2024-05-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_product_tiki_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tiki_product_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
