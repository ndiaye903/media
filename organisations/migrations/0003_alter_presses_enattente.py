# Generated by Django 5.0.6 on 2024-06-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_auto_20240525_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presses',
            name='enAttente',
            field=models.BooleanField(default=True),
        ),
    ]
