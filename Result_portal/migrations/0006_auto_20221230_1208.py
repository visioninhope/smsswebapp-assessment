# Generated by Django 2.2 on 2022-12-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Result_portal', '0005_auto_20221230_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_pin_and_id',
            name='student_pin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
