# Generated by Django 4.2.5 on 2023-09-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('idGame', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Game')),
                ('idPlatform', models.CharField(max_length=255, verbose_name='Platform')),
                ('year', models.IntegerField(default=2023, verbose_name='Year')),
            ],
        ),
    ]
