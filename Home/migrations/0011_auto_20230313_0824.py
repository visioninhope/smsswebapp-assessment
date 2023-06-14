# Generated by Django 2.2 on 2023-03-13 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0008_students_pin_and_id_student_password'),
        ('Home', '0010_auto_20230313_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='Facebook_link',
            new_name='teachers_id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='Instagram_link',
            new_name='teachers_password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Twitter_link',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Classes_assigned',
        ),
        migrations.AddField(
            model_name='teacher',
            name='Classes_assigned',
            field=models.ManyToManyField(to='Result_portal.Class'),
        ),
    ]