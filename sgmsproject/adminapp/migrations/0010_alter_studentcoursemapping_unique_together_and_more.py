# Generated by Django 4.2.5 on 2023-11-04 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_alter_student_contact'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentcoursemapping',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='studentcoursemapping',
            name='course',
        ),
        migrations.RemoveField(
            model_name='studentcoursemapping',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='studentcoursemapping',
            name='student',
        ),
        migrations.DeleteModel(
            name='FacultyCourseMapping',
        ),
        migrations.DeleteModel(
            name='StudentCourseMapping',
        ),
    ]
