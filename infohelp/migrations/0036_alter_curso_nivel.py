# Generated by Django 5.1.3 on 2025-02-19 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0035_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Difícil', 'Difícil'), ('Médio', 'Médio'), ('Fácil', 'Fácil')], default='Fácil', max_length=30),
        ),
    ]
