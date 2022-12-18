# Generated by Django 3.2.16 on 2022-12-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('talle', models.IntegerField(choices=[(1, 'ExtraChico'), (2, 'Chico'), (3, 'Mediano'), (4, 'Grande'), (5, 'ExtraGrande'), (6, 'DobleExtraGrande')], default=1)),
                ('color', models.CharField(max_length=50)),
                ('lisa', models.BooleanField(blank=True, null=True, verbose_name='Remera Lisa')),
                ('genero', models.IntegerField(choices=[(1, 'Hombre'), (2, 'Mujer'), (3, 'Unisex')], default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Remera',
        ),
    ]
