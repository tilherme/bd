# Generated by Django 4.0.5 on 2022-06-13 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_class'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Class_school',
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('class_school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.class_school')),
            ],
        ),
    ]
