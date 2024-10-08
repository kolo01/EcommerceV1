# Generated by Django 5.1.1 on 2024-09-19 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('paiement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('total_amount', models.FloatField()),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart_ids', to='cart.cartmodel')),
                ('payment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_ids', to='paiement.paiementmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
