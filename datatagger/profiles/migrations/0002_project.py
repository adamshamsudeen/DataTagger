# Generated by Django 2.1.5 on 2019-02-07 18:09

from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=120, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('project_owner', models.ForeignKey(default=profiles.models.default_user, on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.Profile')),
            ],
        ),
    ]
