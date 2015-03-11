# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_usuario_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='birthdate',
        ),
    ]
