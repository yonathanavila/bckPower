# Generated by Django 4.2.5 on 2023-10-03 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0053_alter_stage_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='idTournament',
            field=models.ForeignKey(db_column='idTournament', on_delete=django.db.models.deletion.DO_NOTHING, to='base.tournament', verbose_name='Tournament'),
        ),
    ]
