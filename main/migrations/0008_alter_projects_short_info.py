# Generated by Django 4.0.6 on 2022-08-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='short_info',
            field=models.CharField(blank=True, max_length=50, verbose_name='Короткий опис'),
        ),
    ]