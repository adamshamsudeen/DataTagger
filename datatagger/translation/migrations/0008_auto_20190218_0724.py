# Generated by Django 2.1.5 on 2019-02-18 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0007_auto_20190215_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partiallytranslated',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.LanguageText'),
        ),
        migrations.AlterField(
            model_name='translatedtext',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.LanguageText'),
        ),
        migrations.AlterField(
            model_name='translateorigin',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.LanguageText'),
        ),
        migrations.DeleteModel(
            name='LanguageText',
        ),
    ]