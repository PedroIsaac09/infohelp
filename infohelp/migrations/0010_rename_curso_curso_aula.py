# Generated by Django 5.1.3 on 2025-01-24 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0009_remove_aula_curso_curso_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='curso',
            new_name='aula',
        ),
    ]
