from django.shortcuts import render
from . import models
import pandas as pd
from django.db.models import Q
import datetime


# 打开登录页面
def login(request):
    pass
    return render(request, 'homework/login.html')


# 登录
def login_action(request):
    username_input = request.POST.get('username', 'None')
    password_input = request.POST.get('password', 'None')
    if username_input and password_input:
        try:
            teacher = models.Teacher.objects.get(username=username_input)
            if teacher.password == password_input:
                return render(request, 'homework/index_teacher.html', {'teacher': teacher})
            else:
                message = "密码不正确"
                return render(request, 'homework/login.html', {'message': message})
        except:
            try:
                student = models.Student.objects.get(username=username_input)
                if student.password == password_input:
                    return render(request, 'homework/index_student.html', {'student': student})
                else:
                    message = "密码不正确"
                    return render(request, 'homework/login.html', {'message': message})
            except:
                message = "账号密码不正确"
                return render(request, 'homework/login.html', {'message': message})
    else:
        message = "账号密码不能为空"
        return render(request, 'homework/login.html', {'message': message})


# 打开教师主页
def index_teacher(request, teacher_id):
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/index_teacher.html', {'teacher': teacher})


# 打开上传学生名单页面
def upload_student_list(request, teacher_id):
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/upload_student_list.html', {'teacher': teacher})


# 上传学生名单
def upload_student_list_action(request, teacher_id):
    uploadedFile = request.FILES.get("myfile", None)
    file = pd.read_excel(uploadedFile)
    data = file.values
    lenth = int(data.size / 3)
    student_id = [0] * lenth
    student_class = [0] * lenth
    student_name = [0] * lenth
    for i in range(lenth):
        student_id[i] = data[i][0]
        student_class[i] = data[i][1]
        student_name[i] = data[i][2]
        student = models.Student.objects.create(student_id=data[i][0], student_class=data[i][1], name=data[i][2], username=data[i][0],password=data[i][0], teacher_id=teacher_id)
    teacher = models.Teacher.objects.get(pk=teacher_id)
    role = 1  # 1代表老师，2代表学生
    return render(request, 'homework/done.html', {'teacher': teacher, 'role': role})


# 打开发布作业界面
def upload_homework(request, teacher_id):
    teacher = models.Teacher.objects.get(pk=teacher_id)
    task = models.Task.objects.all()
    return render(request, 'homework/upload_homework.html', {'teacher': teacher})


# 发布作业
def upload_homework_action(request, teacher_id):
    task_title = request.POST.get('task_title', 'None')
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task = models.Task.objects.create(teacher_id=teacher_id, time=time, task_title=task_title)
    question = ['']*21
    value = [''] * 21
    task_value = 0
    for i in range(1, 21):
        question_name = 'question'+str(i)
        question[i] = request.POST.get(question_name, '')
        question_value = 'value'+str(i)
        value[i] = request.POST.get(question_value, '')
        if question[i] != '':
            models.Question.objects.create(question_title=question[i], task_id=task.id, value=value[i])
            task_value += int(value[i])
        else:
            break
    task.value = task_value
    task.save()
    role = 1
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/done.html', {'teacher': teacher, 'role': role})


# 打开管理作业界面
def edit_homework(request, teacher_id):
    teacher = models.Teacher.objects.get(pk=teacher_id)
    tasks = models.Task.objects.filter(teacher_id=teacher_id)
    return render(request, 'homework/edit_homework.html', {'teacher': teacher, 'tasks': tasks})


# 打开编辑作业界面
def edit_task(request, teacher_id, task_id):
    teacher = models.Teacher.objects.get(pk=teacher_id)
    questions = models.Question.objects.filter(task_id=task_id)
    task = models.Task.objects.get(pk=task_id)
    return render(request, 'homework/edit_task.html', {'teacher': teacher, 'questions': questions, 'task': task})


# 编辑已发布的作业
def edit_task_action(request, teacher_id, task_id):
    task = models.Task.objects.get(pk=task_id)
    task.task_title = request.POST.get('task_title', 'None')
    task.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task.teacher_id = teacher_id
    task.save()
    models.Question.objects.filter(task_id=task_id).delete()
    question = [''] * 21
    value = [''] * 21
    task_value = 0
    for i in range(1, 21):
        question_name = 'question' + str(i)
        question[i] = request.POST.get(question_name, '')
        question_value = 'value' + str(i)
        value[i] = request.POST.get(question_value, '')
        if question[i] != '':
            if value[i] == '':
                value[i] = 0
            models.Question.objects.create(question_title=question[i], task_id=task_id, value=value[i])
            task_value += int(value[i])
        else:
            break
    task.value = task_value
    task.save()
    role = 1
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/done.html', {'teacher': teacher, 'role': role})


# 删除作业
def delete_task_action(request, teacher_id, task_id):
    task = models.Task.objects.get(pk=task_id)
    task.delete()
    questions = models.Question.objects.filter(task_id=task_id)
    for question in questions:
        question.delete()
    role = 1
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/done.html', {'teacher': teacher, 'role': role})


# 打开批改作业界面
def correct_homework(request, teacher_id):
    teacher = models.Teacher.objects.get(pk=teacher_id)
    tasks = models.Task.objects.filter(teacher_id=teacher_id)
    return render(request, 'homework/correct_homework.html', {'teacher': teacher, 'tasks': tasks})


# 打开查看作业上传名单界面
def view_upload_list(request, teacher_id, task_id):
    task_grades1 = models.Task_Grade.objects.filter(task_id=task_id, status=1)
    task_grades2 = models.Task_Grade.objects.filter(task_id=task_id, status=2)
    students_id1 = []    # 已提交作业但未批改的学生id
    for task_grade1 in task_grades1:
        students_id1.append(task_grade1.student_id)
    students_id2 = []    # 作业已批改的学生id
    grade2 = []     #作业成绩
    for task_grade2 in task_grades2:
        students_id2.append(task_grade2.student_id)
        grade2.append(task_grade2.grade)
    student_id12 = students_id1 + students_id2      #提交作业的学生
    students0 = models.Student.objects.filter(teacher_id=teacher_id).exclude(student_id__in=student_id12)   # 未提交作业的学生
    task = models.Task.objects.get(pk=task_id)
    teacher = models.Teacher.objects.get(pk=teacher_id)
    students1 = models.Student.objects.filter(student_id__in=students_id1)  # 已提交作业但未批改的学生
    students2 = models.Student.objects.filter(student_id__in=students_id2)  # 作业已批改的学生
    dic = dict()
    i = 0
    for student2 in students2:
        dic[student2] = grade2[i]
        i = i+1
    return render(request, 'homework/view_upload_list.html', {'students0': students0, 'students1': students1, 'dic':dic, 'teacher': teacher, 'task': task})


# 打开批改学生作业界面
def correct_task(request, teacher_id, student_id, task_id):
    questions = models.Question.objects.filter(task_id=task_id)
    dic = dict()
    for question in questions:
        try:
            question_grade = models.Question_Grade.objects.get(student_id=student_id, question_id=question.id)
            dic[question] = question_grade
        except:
            dic[question] = None
            continue
    teacher = models.Teacher.objects.get(pk=teacher_id)
    student = models.Student.objects.get(pk=student_id)
    task = models.Task.objects.get(pk=task_id)
    return render(request, 'homework/correct_task.html', {'dic': dic, 'teacher': teacher, 'student': student, 'task': task})


# 批改学生作业
def correct_task_action(request, teacher_id, student_id, task_id):
    questions = models.Question.objects.filter(task_id=task_id)
    # 已批改：提交题目数量num1等于批改作业数量num2
    # 未批改：提交题目数量num1大于批改作业数量num2
    num1 = 0
    num2 = 0
    total_grade = 0
    for question in questions:
        try:
            question_grade = models.Question_Grade.objects.get(student_id=student_id, question_id=question.id)
            num1 = num1 + 1
            grade_str = 'grade'+str(question_grade.id)
            grade_input = request.POST.get(grade_str)
            question_grade.grade = grade_input
            if question_grade.grade:
                question_grade.status = 2
                num2 = num2+1
                total_grade = total_grade + int(question_grade.grade)
            else:
                question_grade.status = 1
            question_grade.save()
        except:
            continue
    task_grade = models.Task_Grade.objects.get(student_id=student_id, task_id=task_id)
    task_grade.grade = str(total_grade)
    if num1 == num2:
        task_grade.status = 2
    else:
        task_grade.status = 1
    task_grade.save()
    role = 1
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/done.html', {'teacher': teacher, 'role': role})


# 打开涂鸦页面
def paint_image(request, teacher_id, question_grade_id):
    question_grade = models.Question_Grade.objects.get(pk=question_grade_id)
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/paint_image.html', {'teacher': teacher, 'question_grade': question_grade})


# 提交涂鸦
def paint_image_action(request, teacher_id, question_grade_id):
    src = request.POST.get('postil_path')
    question_grade = models.Question_Grade.objects.get(pk=question_grade_id)
    question_grade.postil = src
    question_grade.save()
    role = 1
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/done.html', {'teacher': teacher, 'role': role})


# 查看涂鸦
def show_postil(request, question_grade_id):
    question_grade = models.Question_Grade.objects.get(pk=question_grade_id)
    return render(request, 'homework/show_postil.html', {'question_grade': question_grade})


# 查看作业提交统计
def show_statistics(request, teacher_id):
    students = models.Student.objects.filter(teacher_id=teacher_id)
    tasks = models.Task.objects.filter(teacher_id=teacher_id)
    grades = [(['未提交'] * tasks.count()) for i in range(students.count())]
    for i in range(students.count()):
        for j in range(tasks.count()):
            try:
                task_grade = models.Task_Grade.objects.get(student_id=students[i].student_id, task_id=tasks[j].id)
                if task_grade.status == '1':
                    grades[i][j] = '未批改'
                elif task_grade.status == '2':
                    grades[i][j] = task_grade.grade
            except:
                continue
    teacher = models.Teacher.objects.get(pk=teacher_id)
    return render(request, 'homework/show_statistics.html', {'teacher': teacher, 'students': students, 'tasks': tasks, 'grades': grades})




# 打开学生主页
def index_student(request, student_id):
    student = models.Student.objects.get(pk=student_id)
    return render(request, 'homework/index_student.html', {'student': student})


# 打开修改密码界面
def change_password(request, student_id):
    student = models.Student.objects.get(pk=student_id)
    return render(request, 'homework/change_password.html', {'student': student})


# 修改密码
def change_password_action(request, student_id):
    password_input = request.POST.get('password', 'None')
    re_password_input = request.POST.get('re_password', 'None')
    student = models.Student.objects.get(pk=student_id)
    if password_input and re_password_input:
        if password_input == re_password_input:
            student.password = password_input
            student.save()
            role = 2  # 1代表老师，2代表学生
            student = models.Student.objects.get(pk=student_id)
            return render(request, 'homework/done.html', {'student': student, 'role': role})
        else:
            message = "密码输入不一致"
            return render(request, 'homework/change_password.html', {'message': message, 'student': student})
    else:
        message = "账号密码不能为空"
        return render(request, 'homework/change_password.html', {'message': message, 'student': student})


# 学生打开查看作业界面
def do_homework(request, student_id):
    student = models.Student.objects.get(pk=student_id)
    tasks = models.Task.objects.filter(teacher_id=student.teacher_id)
    return render(request, 'homework/do_homework.html', {'student': student, 'tasks': tasks})


# 打开作业内容界面
def do_task(request, student_id, task_id):
    task = models.Task.objects.get(pk=task_id)
    questions = models.Question.objects.filter(task_id=task_id)
    student = models.Student.objects.get(pk=student_id)
    dic = dict()
    for question in questions:
        try:
            question_grade = models.Question_Grade.objects.get(student_id=student_id, question_id=question.id)
            if question_grade.status == '1':
                dic[question] = '未批改'
            elif question_grade.status == '2':
                dic[question] = '已批改'
        except:
            dic[question] = '未提交'
            continue
    return render(request, 'homework/do_task.html', {'student': student, 'dic': dic, 'task': task})


# 学生提交作业
def do_task_action(request, student_id, question_id, task_id, counter):
    filename = 'answer'+str(counter)
    img = request.FILES.get(filename, '')
    if img != '':
        try:
            question_grade = models.Question_Grade.objects.filter(student_id=student_id, question_id=question_id)
            question_grade.delete()
        finally:
            #status=1代表作业已提交未批改，status=2代表作业已批改
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            models.Question_Grade.objects.create(student_id=student_id, question_id=question_id, answer=img, status='1', time=time)
            try:
                task_grade = models.Task_Grade.objects.get(student_id=student_id, task_id=task_id)
                task_grade.status = '1'
                task_grade.save()
            except:
                models.Task_Grade.objects.create(student_id=student_id, task_id=task_id, status='1')
    task = models.Task.objects.get(pk=task_id)
    questions = models.Question.objects.filter(task_id=task_id)
    student = models.Student.objects.get(pk=student_id)
    dic = dict()
    for question in questions:
        try:
            question_grade = models.Question_Grade.objects.get(student_id=student_id, question_id=question.id)
            if question_grade.status == '1':
                dic[question] = '未批改'
            elif question_grade.status == '2':
                dic[question] = '已批改'
        except:
            dic[question] = '未提交'
            continue
    return render(request, 'homework/do_task.html', {'student': student, 'dic': dic, 'task': task})


# 展示已提交的作业
def show_image(request, student_id, question_id):
    question_grade = models.Question_Grade.objects.get(student_id=student_id, question_id=question_id)
    image = question_grade.answer
    return render(request, 'homework/show_image.html', {'image': image})


# 查看成绩
def view_grade(request, student_id):
    student = models.Student.objects.get(pk=student_id)
    tasks = models.Task.objects.filter(teacher_id=student.teacher_id)
    task_grades = [None] * tasks.count()
    dic = dict()
    for task in tasks:
        try:
            task_grade = models.Task_Grade.objects.get(student_id=student.student_id, task_id=task.id)
            dic[task] = task_grade
        except:
            dic[task] = None
    student = models.Student.objects.get(pk=student_id)
    return  render(request, 'homework/view_grade.html', {'student': student, 'dic': dic})


# 查看作业成绩
def view_task(request, student_id, task_id, task_grade_id):
    questions = models.Question.objects.filter(task_id=task_id)
    dic = dict()
    for question in questions:
        try:
            question_grade = models.Question_Grade.objects.get(student_id=student_id, question_id=question.id)
            dic[question] = question_grade
        except:
            dic[question] = None
            continue
    student = models.Student.objects.get(pk=student_id)
    task = models.Task.objects.get(pk=task_id)
    return render(request, 'homework/view_task.html', {'dic': dic, 'student': student, 'task': task})