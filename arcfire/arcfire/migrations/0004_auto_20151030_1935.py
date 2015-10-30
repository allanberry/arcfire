# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-10-30 19:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arcfire', '0003_auto_20151030_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='arcfire.Keyword'),
        ),
        migrations.AlterField(
            model_name='item',
            name='locations',
            field=models.ManyToManyField(blank=True, null=True, to='arcfire.Location'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='pictures',
            field=models.ManyToManyField(blank=True, null=True, to='arcfire.Picture'),
        ),
        migrations.AlterField(
            model_name='item',
            name='plans',
            field=models.ManyToManyField(blank=True, null=True, to='arcfire.Plan'),
        ),
        migrations.AlterField(
            model_name='item',
            name='properties',
            field=models.ManyToManyField(blank=True, null=True, to='arcfire.Property'),
        ),
        migrations.AlterField(
            model_name='item',
            name='scale',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='The magnitude of a thing, in whole numbers.  0 is average/medium/normal/default/human-sized.  e.g.: -2=XS, -1=S, 0=M, 1=L, 2=XL, 3=2XL and so on.', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='altitude',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='In meters.', max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='kind',
            field=models.CharField(blank=True, choices=[('begin', 'Begin'), ('change', 'Change'), ('end', 'End')], default='change', max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text='In meters.', max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, help_text='In decimal.', max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('none', 'None'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='ki',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.5, help_text='Choose a number between 0.0 and 1.0.  The default is 0.5, which represents the life-force of Joe the Plumber.  0.0 is empty space, somewhere past Pluto.  1.0 is God himself. See wiki/ki for more information.', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='person',
            name='name_secondary',
            field=models.CharField(blank=True, max_length=255, verbose_name='Given Name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='species',
            field=models.CharField(blank=True, help_text='TODO: Use controlled vocabulary.', max_length=255),
        ),
        migrations.AlterField(
            model_name='picture',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='height',
            field=models.PositiveIntegerField(blank=True, help_text='In pixels.', null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, height_field=models.PositiveIntegerField(blank=True, help_text='In pixels.', null=True), null=True, upload_to='', width_field=models.PositiveIntegerField(blank=True, help_text='In pixels.', null=True)),
        ),
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='picture',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='width',
            field=models.PositiveIntegerField(blank=True, help_text='In pixels.', null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male'), ('none', 'None'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='place',
            name='ki',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.5, help_text='Choose a number between 0.0 and 1.0.  The default is 0.5, which represents the life-force of Joe the Plumber.  0.0 is empty space, somewhere past Pluto.  1.0 is God himself. See wiki/ki for more information.', max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='place',
            name='species',
            field=models.CharField(blank=True, help_text='TODO: Use controlled vocabulary.', max_length=255),
        ),
        migrations.AlterField(
            model_name='plan',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='plan',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='property',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='relationjoin',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='arcfire.RelationJoin'),
        ),
        migrations.AlterField(
            model_name='relationjoin',
            name='target',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='arcfire.RelationJoin'),
        ),
        migrations.AlterField(
            model_name='thing',
            name='heading',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='In radians.  The angle between the direction the item is pointing and true North.', max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='In meters.', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='In meters.', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='mass',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='In kilograms.', max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='thing',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='In meters.', max_digits=12, null=True),
        ),
    ]