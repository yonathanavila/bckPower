# Generated by Django 4.2.5 on 2023-10-01 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_gamedetail_playermatch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedetail',
            name='idPlayer',
            field=models.BigIntegerField(db_column='IdPlayer', verbose_name='Player'),
        ),
    ]