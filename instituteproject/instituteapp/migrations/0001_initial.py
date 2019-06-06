# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-27 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.BigIntegerField()),
                ('courses', multiselectfield.db.fields.MultiSelectField(choices=[('py', 'python'), ('dj', 'django'), ('ui', 'UI'), ('rest', 'RESTAPI')], max_length=200)),
                ('shifts', multiselectfield.db.fields.MultiSelectField(choices=[('mrg', 'morning'), ('aftrn', 'afternoon'), ('evng', 'evening'), ('night', 'night')], max_length=200)),
                ('locations', multiselectfield.db.fields.MultiSelectField(choices=[('hyd', 'hyderabad'), ('bang', 'banglaore'), ('chennai', 'chennai'), ('pune', 'pune')], max_length=200)),
                ('gender', models.CharField(max_length=50)),
                ('start_date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.CharField(max_length=200)),
                ('course_dur', models.IntegerField()),
                ('course_fee', models.IntegerField()),
                ('start_date', models.DateField(max_length=100)),
                ('start_time', models.TimeField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_exp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
                ('feedback', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
