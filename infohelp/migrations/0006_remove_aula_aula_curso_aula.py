# Generated by Django 5.1.3 on 2025-01-24 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0005_aula_aula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='aula',
        ),
        migrations.AddField(
            model_name='curso',
            name='aula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='infohelp.aula'),
        ),
    ]
