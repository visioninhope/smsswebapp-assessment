# Generated by Django 2.2 on 2023-11-13 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CBT', '0009_answer_question_questionset_questionsetgroup_test_testquestionset_testsetgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['id']},
        ),
    ]