# Generated by Django 4.1.3 on 2022-11-06 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0003_doctor_doctor_fees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='number_of_integers',
            new_name='number_of_doctors',
        ),
    ]
