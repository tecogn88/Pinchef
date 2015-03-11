# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20150310_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='alimentacion',
            field=models.CharField(default=b'ninguno', max_length=100, choices=[(b'vegetariano', b'Vegetariano'), (b'vegano', b'Vegano'), (b'ninguno', b'Ninguno de los Anteriores')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='cerdo',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfComes Carne de Cerdo?:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='cordero',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfComes Cordero?:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='mariscos',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfComes Mariscos:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='pescado',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfComes Pescado?:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='pollo',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfComes Pollo/Aves?:'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='res',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfComes Carne de Res?:'),
            preserve_default=True,
        ),
    ]
