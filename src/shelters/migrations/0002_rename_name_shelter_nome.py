# Generated by Django 4.0.7 on 2022-12-01 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shelter',
            old_name='name',
            new_name='nome',
        ),
    ]
