# Generated by Django 2.1.5 on 2019-02-07 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0005_auto_20190206_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_owner',
        ),
        migrations.AlterField(
            model_name='partiallytranslated',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.Project'),
        ),
        migrations.AlterField(
            model_name='translatedtext',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.Project'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]