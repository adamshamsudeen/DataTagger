# Generated by Django 2.1.7 on 2019-03-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0012_auto_20190323_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translateorigin',
            name='text',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
