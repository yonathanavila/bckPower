# Generated by Django 4.2.5 on 2023-09-23 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLeague', models.IntegerField(verbose_name='Id League')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.CharField(max_length=255, verbose_name='Slug')),
                ('sport', models.CharField(max_length=6, verbose_name='Sport')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('lightImage', models.ImageField(upload_to='', verbose_name='Light Image')),
                ('darkImage', models.ImageField(upload_to='', verbose_name='Dark Image')),
                ('region', models.CharField(max_length=255, verbose_name='Region')),
                ('priority', models.IntegerField(verbose_name='Priority')),
                ('displayPriorityPosition', models.IntegerField(verbose_name='Display Priority Position')),
                ('displayPriorityStatus', models.BooleanField(verbose_name='Display Priority Status')),
            ],
        ),
    ]
