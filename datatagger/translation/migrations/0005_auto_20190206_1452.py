# Generated by Django 2.1.5 on 2019-02-06 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0004_translatedtext_lanuguage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partiallytranslated',
            old_name='lanuguage',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='partiallytranslated',
            old_name='partially_tranlated_text',
            new_name='partially_translated_text',
        ),
        migrations.RenameField(
            model_name='translatedtext',
            old_name='lanuguage',
            new_name='language',
        ),
    ]
