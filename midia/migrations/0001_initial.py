# Generated by Django 4.2.7 on 2023-11-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Midia',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Categoria', models.CharField(choices=[('Eventos', 'Eventos'), ('Viagens', 'Viagens'), ('Happy Hour', 'Happy Hour')], max_length=50)),
                ('Legenda', models.TextField()),
                ('Imagem', models.ImageField(upload_to='')),
                ('Data_de_publicação', models.DateTimeField(auto_now_add=True)),
                ('Autor', models.CharField(max_length=75)),
                ('Curtidas', models.IntegerField(default=0)),
            ],
        ),
    ]