# Generated by Django 5.0.6 on 2024-06-07 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_rename_data_nascimento_aluno_data_nasc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='curso_id',
            new_name='cod_curso',
        ),
    ]
