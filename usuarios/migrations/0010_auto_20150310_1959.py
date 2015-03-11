# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20150310_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='alimentacion',
            field=models.CharField(default=b'ninguno', max_length=100, choices=[(b'vegetariano', b'Vegetariano(a)'), (b'vegano', b'Vegano(a)'), (b'ninguno', b'Ninguno de los Anteriores')]),
            preserve_default=True,
        ),
    ]
