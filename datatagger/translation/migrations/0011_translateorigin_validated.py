# Generated by Django 2.1.5 on 2019-03-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0010_translateorigin_can_be_tagged'),
    ]

    operations = [
        migrations.AddField(
            model_name='translateorigin',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
