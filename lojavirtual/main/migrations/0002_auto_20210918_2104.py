# Generated by Django 3.2 on 2021-09-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('nome',), 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ('nome',)},
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens-produtos/'),
        ),
        migrations.AlterIndexTogether(
            name='produto',
            index_together={('id', 'slug')},
        ),
    ]
