# Generated by Django 4.0.7 on 2022-12-01 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0005_shelter_total_alter_shelter_vagas'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='ocupação',
            field=models.IntegerField(default=0),
        ),
    ]
