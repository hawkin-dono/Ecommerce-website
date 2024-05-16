# Generated by Django 5.0.3 on 2024-05-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_alter_order_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
