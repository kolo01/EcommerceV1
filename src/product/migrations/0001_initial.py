# Generated by Django 5.1.1 on 2024-09-19 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=180)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_ids', to='category.categorymodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
