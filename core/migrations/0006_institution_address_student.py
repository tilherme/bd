# Generated by Django 4.0.5 on 2022-06-13 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_class_class_school_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='Address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.adress'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('sex', models.CharField(max_length=255, null=True)),
                ('cpf', models.CharField(max_length=255, null=True)),
                ('registration', models.CharField(max_length=255, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('specialization', models.CharField(max_length=255, null=True)),
                ('class_school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.class_school')),
            ],
        ),
    ]
