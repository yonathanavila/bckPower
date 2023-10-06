# Generated by Django 4.2.5 on 2023-10-03 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_alter_gamedetail_idplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('idMatch', models.BigAutoField(primary_key=True, serialize=False, verbose_name='idMatch')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('state', models.CharField(max_length=255, verbose_name='State')),
                ('mode', models.CharField(max_length=255, verbose_name='Mode')),
                ('strategy', models.CharField(max_length=255, verbose_name='Strategy')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Stage')),
                ('slug', models.CharField(max_length=255, verbose_name='Slug')),
                ('idTournament', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.tournament', verbose_name='Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Section')),
                ('idStage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.stage', verbose_name='Stage')),
            ],
        ),
        migrations.CreateModel(
            name='MatchDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchTeamIntegrants', models.BooleanField(default=False, verbose_name='Match Integrants')),
                ('win', models.BooleanField(verbose_name='Win Game?')),
                ('idMatch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.match', verbose_name='Match')),
                ('idTeam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.team', verbose_name='Team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='idSection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.section', verbose_name='Section Detail'),
        ),
    ]