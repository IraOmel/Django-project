# Generated by Django 4.0.6 on 2022-08-02 20:14

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_empdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=150, verbose_name='Користувач'),
        ),
    ]
