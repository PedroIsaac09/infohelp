# Generated by Django 5.1.3 on 2025-02-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0022_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('P', 'Fácil'), ('G', 'Difícil'), ('M', 'Médio')], default='M', max_length=30),
        ),
    ]
