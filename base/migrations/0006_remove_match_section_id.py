# Generated by Django 4.2.6 on 2023-10-22 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_sectionname_stagename_stageslug_stagetype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='section_id',
        ),
    ]
