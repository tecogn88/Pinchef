# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20150302_2315'),
        ('recetas', '0006_auto_20150302_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(related_name='usuarios', default=1, to='usuarios.Usuario'),
            preserve_default=False,
        ),
    ]
