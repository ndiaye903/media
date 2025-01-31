# Generated by Django 5.0.6 on 2024-07-03 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_alter_presses_enattente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisations',
            name='enAttente',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='autrePrecision',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='autrePrecisionCharge',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='biographie',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='dateDepart',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='dateRetour',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='deuxiemeprenom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='enAttente',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='photo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='villeDepart',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='participants',
            name='villeRetour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='autrePrecision',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='autrePrecisionCharge',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='dateDepart',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='dateRetour',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='deuxiemeprenom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='passport',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='villeDepart',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='presses',
            name='villeRetour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
