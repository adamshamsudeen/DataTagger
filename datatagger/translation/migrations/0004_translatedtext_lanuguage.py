# Generated by Django 2.1.5 on 2019-02-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0003_auto_20190206_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='translatedtext',
            name='lanuguage',
            field=models.CharField(default='ml', max_length=2),
            preserve_default=False,
        ),
    ]
