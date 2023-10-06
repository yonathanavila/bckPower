# Generated by Django 4.2.5 on 2023-10-03 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0065_remove_matchdetail_idmatch_remove_matchdetail_idteam_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('mode', models.CharField(max_length=255, verbose_name='Mode')),
                ('strategy', models.CharField(max_length=255, verbose_name='Strategy')),
                ('idSection', models.ForeignKey(db_column='idSection', on_delete=django.db.models.deletion.DO_NOTHING, to='base.section', verbose_name='Section Detail')),
            ],
        ),
        migrations.CreateModel(
            name='MatchDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchTeamIntegrants', models.BooleanField(default=False, verbose_name='Match Integrants')),
                ('win', models.BooleanField(verbose_name='Win Game?')),
                ('idMatch', models.ForeignKey(db_column='idMatch', on_delete=django.db.models.deletion.DO_NOTHING, to='base.match', verbose_name='Match')),
                ('idTeam', models.ForeignKey(db_column='idTeam', on_delete=django.db.models.deletion.DO_NOTHING, to='base.team', verbose_name='Team')),
            ],
        ),
    ]