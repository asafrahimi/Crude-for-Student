# Generated by Django 2.2 on 2021-06-19 06:26

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('num_home', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_profession', models.CharField(max_length=20)),
                ('second_profession', models.CharField(max_length=20)),
                ('thrid_profession', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('i_d', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studentarr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_d', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('student_details', models.ForeignKey(default=student.models.get_default_something, on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
