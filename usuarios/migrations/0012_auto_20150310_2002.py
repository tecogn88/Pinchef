# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0011_auto_20150310_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='cerdo',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfCome Carne de Cerdo?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='cordero',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfCome Cordero?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='mariscos',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfCome Mariscos'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='pescado',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfCome Pescado?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='pollo',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfCome Pollo/Aves?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='res',
            field=models.BooleanField(default=False, verbose_name=b'\xc2\xbfCome Carne de Res?'),
            preserve_default=True,
        ),
    ]
