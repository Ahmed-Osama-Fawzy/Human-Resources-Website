# Generated by Django 4.1.7 on 2023-06-01 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_emplooyes_birthdate_alter_emplooyes_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplooyes',
            name='Address',
            field=models.TextField(default='None'),
        ),
    ]