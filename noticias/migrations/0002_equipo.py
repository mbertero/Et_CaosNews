# Generated by Django 4.2.2 on 2023-07-01 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_funcionario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]
