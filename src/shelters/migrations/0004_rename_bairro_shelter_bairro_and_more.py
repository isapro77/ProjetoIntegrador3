# Generated by Django 4.0.7 on 2022-12-01 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0003_rename_postal_device_cep_rename_city_device_bairro_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shelter',
            old_name='Bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='shelter',
            old_name='Cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='shelter',
            old_name='Vagas',
            new_name='vagas',
        ),
    ]
