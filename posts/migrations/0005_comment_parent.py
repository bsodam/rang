# Generated by Django 2.1.5 on 2019-02-11 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190209_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
