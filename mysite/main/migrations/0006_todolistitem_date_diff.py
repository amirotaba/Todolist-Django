# Generated by Django 4.0.1 on 2022-02-05 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_date_todolistitem_sub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitem',
            name='date_diff',
            field=models.IntegerField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
