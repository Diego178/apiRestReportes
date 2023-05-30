# Generated by Django 3.2.18 on 2023-05-16 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esp32', models.CharField(max_length=10)),
                ('mensaje', models.CharField(max_length=250)),
                ('fecha', models.CharField(max_length=15)),
                ('hora', models.CharField(max_length=10)),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
    ]