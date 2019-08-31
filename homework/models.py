from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class Student(models.Model):
    student_id = models.CharField(max_length=32, primary_key=True)
    student_class = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    teacher_id = models.CharField(max_length=32)


class Task(models.Model):
    teacher_id = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    task_title = models.CharField(max_length=256)
    value = models.CharField(max_length=4)


class Question(models.Model):
    question_title = models.CharField(max_length=256)
    task_id = models.CharField(max_length=32)
    value = models.CharField(max_length=4)


class Question_Grade(models.Model):
    student_id = models.CharField(max_length=32)
    question_id = models.CharField(max_length=32)
    answer = models.ImageField(upload_to="%Y/%m/%d/answer/")
    time = models.CharField(max_length=32)
    grade = models.CharField(max_length=3)
    status = models.CharField(max_length=1)
    postil = models.CharField(max_length=16384)


class Task_Grade(models.Model):
    student_id = models.CharField(max_length=32)
    task_id = models.CharField(max_length=32)
    grade = models.CharField(max_length=3)
    status = models.CharField(max_length=1)
