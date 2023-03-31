# Generated by Django 4.1.7 on 2023-03-31 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='tituto',
            new_name='titulo',
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(verbose_name='Data do evento'),
        ),
    ]