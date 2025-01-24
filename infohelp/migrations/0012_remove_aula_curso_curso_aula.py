# Generated by Django 5.1.3 on 2025-01-24 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0011_remove_curso_aula_aula_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='curso',
        ),
        migrations.AddField(
            model_name='curso',
            name='aula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='infohelp.aula'),
        ),
    ]
