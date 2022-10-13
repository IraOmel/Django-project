# Generated by Django 4.0.6 on 2022-08-02 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_empdetails_alter_app_options_alter_app_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('app_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.app')),
            ],
            bases=('main.app',),
        ),
        migrations.AlterField(
            model_name='empdetails',
            name='Email',
            field=models.EmailField(max_length=254, verbose_name='Поштова адреса'),
        ),
        migrations.AlterField(
            model_name='empdetails',
            name='Message',
            field=models.CharField(max_length=300, verbose_name='Повідомлення'),
        ),
        migrations.AlterField(
            model_name='empdetails',
            name='Name',
            field=models.CharField(max_length=150, verbose_name='Користувач'),
        ),
    ]
