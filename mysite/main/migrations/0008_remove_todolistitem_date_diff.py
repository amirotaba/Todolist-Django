# Generated by Django 4.0.1 on 2022-02-05 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_todolistitem_date_diff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolistitem',
            name='date_diff',
        ),
    ]
