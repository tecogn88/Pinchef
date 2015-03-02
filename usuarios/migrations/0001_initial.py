# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=255)),
                ('colonia', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('cp', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255, blank=True)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('status', models.IntegerField(max_length=11)),
                ('tipo', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
