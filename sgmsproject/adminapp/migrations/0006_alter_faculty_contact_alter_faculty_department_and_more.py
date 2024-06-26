# Generated by Django 4.2.5 on 2023-11-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_studentcoursemapping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='contact',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(blank=True, choices=[('CSE-R', 'CSE(Regular)'), ('CSE-H', 'CSE(Honors)'), ('CSIT', 'CS&IT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(blank=True, choices=[('Prof.', 'Professor'), ('Assoc. Prof.', 'Associate Proffesor'), ('Asst. prof', 'Assistant Professor')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='fullname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=20),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(blank=True, choices=[('Ph.d', 'Ph.d'), ('M.Tech', 'M.Tech')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='semester',
            field=models.CharField(blank=True, choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]
