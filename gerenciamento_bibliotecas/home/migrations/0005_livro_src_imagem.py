# Generated by Django 4.2.2 on 2023-06-19 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_livro_ano_publicacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='src_imagem',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]