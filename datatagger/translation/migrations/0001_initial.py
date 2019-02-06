# Generated by Django 2.1.5 on 2019-02-06 14:33

from django.db import migrations, models
import django.db.models.deletion
import translation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartiallyTranslated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lanuguage', models.CharField(max_length=2)),
                ('partially_tranlated_text', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project_owner', models.ForeignKey(default=translation.models.default_user, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='TranslatedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translated_text', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TranslateOrigin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('language', models.CharField(default='en', max_length=2)),
                ('project_name', models.CharField(max_length=50, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='translatedtext',
            name='origin_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translation.TranslateOrigin'),
        ),
        migrations.AddField(
            model_name='translatedtext',
            name='partially_correct_text',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='translation.PartiallyTranslated'),
        ),
        migrations.AddField(
            model_name='translatedtext',
            name='tagged_by',
            field=models.ForeignKey(default=translation.models.default_user, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='partiallytranslated',
            name='origin_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translation.TranslateOrigin'),
        ),
    ]
