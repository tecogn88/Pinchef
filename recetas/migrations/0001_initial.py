# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(unique=True)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to=b'recetas')),
                ('calorias', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pedido',
            name='recetas',
            field=models.ManyToManyField(related_name='recetas', to='recetas.Receta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(related_name='usuarios', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
