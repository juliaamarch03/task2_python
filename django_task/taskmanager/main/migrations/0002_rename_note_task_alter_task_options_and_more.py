# Generated by Django 4.2.2 on 2023-06-06 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Task',
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Нотатка', 'verbose_name_plural': 'Нотатки'},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='note',
            new_name='task',
        ),
    ]
