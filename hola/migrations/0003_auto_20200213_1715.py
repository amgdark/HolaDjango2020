# Generated by Django 3.0.3 on 2020-02-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hola', '0002_auto_20200211_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulos', verbose_name='Imagen'),
        ),
    ]