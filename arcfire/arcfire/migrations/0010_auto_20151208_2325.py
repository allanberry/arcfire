# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcfire', '0009_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('scale', models.PositiveIntegerField(blank=True, default=0, help_text='The magnitude of a thing, in whole numbers.  0 is average/medium/normal/default/human-sized.  e.g.: -2=XS, -1=S, 0=M, 1=L, 2=XL, 3=2XL and so on.', null=True)),
                ('text', models.TextField(blank=True, help_text='This is a container for long-form prose, or whatever other type of content this card should have.', null=True)),
                ('text_format', models.CharField(choices=[('md', 'Markdown (Git)'), ('html', 'HTML')], default='md', max_length=10)),
                ('sort_order', models.DecimalField(decimal_places=6, help_text='Order in which this card appears (at its scale).  Lower numbers come first; negative numbers OK.  To slip a card between two other cards, use a decimal.', max_digits=12)),
                ('keywords', models.ManyToManyField(blank=True, to='arcfire.Keyword')),
                ('locations', models.ManyToManyField(blank=True, to='arcfire.Location')),
                ('pictures', models.ManyToManyField(blank=True, to='arcfire.Picture')),
                ('plans', models.ManyToManyField(blank=True, to='arcfire.Plan')),
                ('properties', models.ManyToManyField(blank=True, to='arcfire.Property')),
                ('relations', models.ManyToManyField(through='arcfire.Relation', to='arcfire.Card')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='collection',
            name='thing_ptr',
        ),
        migrations.RemoveField(
            model_name='group',
            name='person_ptr',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
