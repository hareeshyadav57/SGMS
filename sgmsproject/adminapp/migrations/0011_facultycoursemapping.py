# Generated by Django 4.2.5 on 2023-11-04 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_alter_studentcoursemapping_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyCourseMapping',
            fields=[
                ('mappingid', models.AutoField(primary_key=True, serialize=False)),
                ('component', models.CharField(choices=[('L', 'Lecture'), ('T', 'Tutorial'), ('P', 'Practical'), ('S', 'Skill')], max_length=10)),
                ('type', models.BooleanField(verbose_name='Faculty_name')),
                ('section', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.faculty')),
            ],
            options={
                'db_table': 'facultycoursemapping_table',
            },
        ),
    ]
