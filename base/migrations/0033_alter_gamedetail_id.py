# Generated by Django 4.2.5 on 2023-09-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_rename_idparticipant_gamedetail_idplayer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
