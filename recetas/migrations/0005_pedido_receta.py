# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_ingrediente_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='receta',
            field=models.ForeignKey(related_name='recetas', default=1, to='recetas.Receta'),
            preserve_default=False,
        ),
    ]
