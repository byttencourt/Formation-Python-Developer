# Generated by Django 4.1.7 on 2023-04-01 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.TextField(blank=True, null=True),
        ),
    ]