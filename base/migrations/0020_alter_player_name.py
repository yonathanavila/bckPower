# Generated by Django 4.2.5 on 2023-09-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_player_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=35, verbose_name='Name'),
        ),
    ]
