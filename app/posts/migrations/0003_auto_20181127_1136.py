# Generated by Django 2.1.3 on 2018-11-27 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181122_1217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pk'], 'verbose_name': '포스트', 'verbose_name_plural': '포스트 목록'},
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 9, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
