# Generated by Django 4.1.2 on 2022-12-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaginaAutos', '0003_auto_imagen_delete_imagenauto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=150)),
            ],
        ),
    ]
