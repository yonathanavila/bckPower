# Generated by Django 4.2.5 on 2023-10-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0047_remove_gamedetail_id_gamedetail_idgamedetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamedetail',
            name='idGameDetail',
        ),
        migrations.AddField(
            model_name='gamedetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
