# Generated by Django 4.2.2 on 2023-07-01 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='img'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('comentario', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='img')),
                ('id_usuario', models.ForeignKey(db_column='idUsuario', on_delete=django.db.models.deletion.CASCADE, to='noticias.usuario')),
            ],
        ),
    ]
