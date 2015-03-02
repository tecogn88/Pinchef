# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0005_pedido_receta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='receta',
        ),
        migrations.AddField(
            model_name='pedido',
            name='recetas',
            field=models.ManyToManyField(related_name='recetas', to='recetas.Receta'),
            preserve_default=True,
        ),
    ]
