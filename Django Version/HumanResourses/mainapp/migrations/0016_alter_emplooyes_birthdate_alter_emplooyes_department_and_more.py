# Generated by Django 4.1.7 on 2023-06-01 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_emplooyes_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplooyes',
            name='Birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='emplooyes',
            name='Department',
            field=models.TextField(default='Genral'),
        ),
        migrations.AlterField(
            model_name='emplooyes',
            name='Email',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='emplooyes',
            name='Gender',
            field=models.TextField(default='Male'),
        ),
        migrations.AlterField(
            model_name='emplooyes',
            name='Mstatue',
            field=models.TextField(default='Single'),
        ),
        migrations.AlterField(
            model_name='emplooyes',
            name='Username',
            field=models.TextField(default='None'),
        ),
    ]
