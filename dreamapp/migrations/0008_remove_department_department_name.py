# Generated by Django 4.1.3 on 2022-11-09 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0007_rename_department_id_department_department_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='department_name',
        ),
    ]
