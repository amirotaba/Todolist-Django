# Generated by Django 4.0.1 on 2022-02-05 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_todolistitem_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolistitem',
            old_name='date',
            new_name='sub_date',
        ),
    ]
