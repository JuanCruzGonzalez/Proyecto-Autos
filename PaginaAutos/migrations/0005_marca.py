# Generated by Django 4.1.2 on 2022-12-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaAutos', '0004_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('historia', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('pais', models.CharField(max_length=100)),
            ],
        ),
    ]