# Generated by Django 5.0.4 on 2024-04-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='Total_Price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
