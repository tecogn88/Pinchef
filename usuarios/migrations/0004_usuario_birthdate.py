# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_membresia'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='birthdate',
            field=models.DateField(null=True,blank=True),
            preserve_default=False,
        ),
    ]
