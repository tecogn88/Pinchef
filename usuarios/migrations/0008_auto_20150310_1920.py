# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20150309_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='usuario',
            field=models.OneToOneField(to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
