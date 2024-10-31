# Generated by Django 5.1.1 on 2024-09-11 20:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0010_participants_created_at_presses_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisations',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presses',
            name='typeWeb',
            field=models.BooleanField(default=False),
        ),
    ]
