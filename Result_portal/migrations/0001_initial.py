# Generated by Django 2.2 on 2022-12-06 18:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(blank=True, max_length=100)),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Class', models.CharField(blank=True, max_length=100)),
                ('Subject', models.CharField(blank=True, max_length=100)),
                ('FirstTerm', models.CharField(blank=True, max_length=100)),
                ('SecondTerm', models.CharField(blank=True, max_length=100)),
                ('ThirdTerm', models.CharField(blank=True, max_length=100)),
                ('Total', models.CharField(blank=True, max_length=100)),
                ('Average', models.CharField(blank=True, max_length=100)),
                ('Grade', models.CharField(blank=True, max_length=100)),
                ('SubjectPosition', models.CharField(blank=True, max_length=100)),
                ('Remark', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AnnualStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Class', models.CharField(blank=True, max_length=100)),
                ('TotalScore', models.CharField(blank=True, max_length=100)),
                ('Totalnumber', models.CharField(blank=True, max_length=100)),
                ('Average', models.CharField(blank=True, max_length=100)),
                ('Position', models.CharField(blank=True, max_length=100)),
                ('Term', models.CharField(blank=True, max_length=100)),
                ('Academicsession', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Excelfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Excel', models.FileField(blank=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(blank=True, max_length=100)),
                ('pin', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(blank=True, max_length=100)),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Class', models.CharField(blank=True, max_length=100)),
                ('Subject', models.CharField(blank=True, max_length=100)),
                ('FirstTest', models.CharField(blank=True, max_length=100)),
                ('SecondTest', models.CharField(blank=True, max_length=100)),
                ('Project', models.CharField(blank=True, max_length=100)),
                ('MidTermTest', models.CharField(blank=True, max_length=100)),
                ('FirstAss', models.CharField(blank=True, max_length=100)),
                ('SecondAss', models.CharField(blank=True, max_length=100)),
                ('CA', models.CharField(blank=True, max_length=100)),
                ('Exam', models.CharField(blank=True, max_length=100)),
                ('Total', models.CharField(blank=True, max_length=100)),
                ('Grade', models.CharField(blank=True, max_length=100)),
                ('SubjectPosition', models.CharField(blank=True, max_length=100)),
                ('Remark', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Class', models.CharField(blank=True, max_length=100)),
                ('TotalScore', models.CharField(blank=True, max_length=100)),
                ('Totalnumber', models.CharField(blank=True, max_length=100)),
                ('Average', models.CharField(blank=True, max_length=100)),
                ('Position', models.CharField(blank=True, max_length=100)),
                ('Term', models.CharField(blank=True, max_length=100)),
                ('Academicsession', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('file', models.FileField(blank=True, upload_to='media')),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='Result_portal.Class')),
            ],
        ),
    ]
