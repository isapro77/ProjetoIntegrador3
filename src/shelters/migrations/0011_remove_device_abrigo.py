# Generated by Django 4.0.7 on 2022-12-02 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0010_rename_endereço_device_endereço_dispositivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='abrigo',
        ),
    ]