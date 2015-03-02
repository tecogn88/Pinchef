# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='receta-1', unique=True),
            preserve_default=False,
        ),
    ]
