# Generated by Django 4.2.5 on 2023-10-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0049_alter_gamedetail_idgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='type',
            field=models.CharField(default=1, max_length=255, verbose_name='Type'),
            preserve_default=False,
        ),
    ]
