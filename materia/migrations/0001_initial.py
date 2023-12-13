# Generated by Django 4.0 on 2023-12-12 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrera.carrera')),
            ],
        ),
    ]