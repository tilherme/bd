# Generated by Django 4.0.5 on 2022-06-13 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_institution_address_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.CharField(choices=[('ESTUDANTE', 'ESTUDANTE'), ('PROFESSOR', 'PROFESSOR')], default='ESTUDANTE', max_length=255),
        ),
    ]
