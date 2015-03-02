# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='cp',
            field=models.CharField(max_length=255, verbose_name=b'C\xc3\xb3digo postal'),
            preserve_default=True,
        ),
    ]
