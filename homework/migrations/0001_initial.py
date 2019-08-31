# Generated by Django 2.2.2 on 2019-08-16 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=256)),
                ('task_id', models.CharField(max_length=32)),
                ('value', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=32)),
                ('question_id', models.CharField(max_length=32)),
                ('answer', models.ImageField(upload_to='%Y/%m/%d/answer/')),
                ('time', models.CharField(max_length=32)),
                ('grade', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=1)),
                ('postil', models.CharField(max_length=16384)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('student_class', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('teacher_id', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=32)),
                ('time', models.CharField(max_length=32)),
                ('task_title', models.CharField(max_length=256)),
                ('value', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Task_Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=32)),
                ('task_id', models.CharField(max_length=32)),
                ('grade', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]