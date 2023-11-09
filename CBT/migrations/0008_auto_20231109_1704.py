# Generated by Django 2.2 on 2023-11-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CBT', '0007_questionsetgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='ExamClass',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='questionset',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='questionsetgroup',
            name='questionsets',
        ),
        migrations.RemoveField(
            model_name='questionsetgroup',
            name='test',
        ),
        migrations.RemoveField(
            model_name='testquestionset',
            name='testSetGroup',
        ),
        migrations.RemoveField(
            model_name='testquestionset',
            name='testSubject',
        ),
        migrations.RemoveField(
            model_name='testsetgroup',
            name='student',
        ),
        migrations.RemoveField(
            model_name='testsetgroup',
            name='test',
        ),
        migrations.RemoveField(
            model_name='testsetgroup',
            name='testClass',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionSet',
        ),
        migrations.DeleteModel(
            name='QuestionSetGroup',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='TestQuestionSet',
        ),
        migrations.DeleteModel(
            name='TestSetGroup',
        ),
    ]
