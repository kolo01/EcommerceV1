# Generated by Django 5.1.1 on 2024-09-19 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='paiement',
        ),
    ]
