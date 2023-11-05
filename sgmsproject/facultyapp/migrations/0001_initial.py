# Generated by Django 4.2.5 on 2023-11-04 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0012_studentcoursemapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyStudentMapping',
            fields=[
                ('mappingid', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_course_mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.facultycoursemapping')),
                ('student_course_mapping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.studentcoursemapping')),
            ],
            options={
                'db_table': 'facultystudentmapping_table',
            },
        ),
    ]
