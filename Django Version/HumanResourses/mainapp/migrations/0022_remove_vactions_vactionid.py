# Generated by Django 4.1.7 on 2023-06-01 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_rename_id_vactions_vactionid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vactions',
            name='VactionId',
        ),
    ]
