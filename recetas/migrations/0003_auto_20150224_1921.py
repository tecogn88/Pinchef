# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0002_receta_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='tipo',
            new_name='calorias',
        ),
        migrations.RenameField(
            model_name='receta',
            old_name='pasos',
            new_name='descripcion',
        ),
    ]
