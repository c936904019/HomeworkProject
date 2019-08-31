from django.urls import path, include
from . import views

app_name = '[homework]'

urlpatterns = [
    path('login/', views.login),
    path('login/action', views.login_action, name='login_action'),
    path('index_teacher/<int:teacher_id>', views.index_teacher, name='index_teacher'),
    path('upload_student_list/<int:teacher_id>', views.upload_student_list, name='upload_student_list'),
    path('upload_student_list/action/<int:teacher_id>', views.upload_student_list_action, name='upload_student_list_action'),
    path('upload_homework/<int:teacher_id>', views.upload_homework, name='upload_homework'),
    path('upload_homework/action/<int:teacher_id>', views.upload_homework_action, name='upload_homework_action'),
    path('edit_homework/<int:teacher_id>', views.edit_homework, name='edit_homework'),
    path('edit_task/<int:teacher_id>/<int:task_id>', views.edit_task, name='edit_task'),
    path('edit_task/action/<int:teacher_id>/<int:task_id>', views.edit_task_action, name='edit_task_action'),
    path('delete_task/action/<int:teacher_id>/<int:task_id>', views.delete_task_action, name='delete_task_action'),
    path('correct_homework/<int:teacher_id>', views.correct_homework, name='correct_homework'),
    path('view_upload_list/<int:teacher_id>/<int:task_id>', views.view_upload_list, name='view_upload_list'),
    path('correct_task/<int:teacher_id>/<int:student_id>/<int:task_id>', views.correct_task, name='correct_task'),
    path('correct_task_action/<int:teacher_id>/<int:student_id>/<int:task_id>', views.correct_task_action, name='correct_task_action'),
    path('paint_image/<int:teacher_id>/<int:question_grade_id>', views.paint_image, name='paint_image'),
    path('paint_image_action/<int:teacher_id>/<int:question_grade_id>', views.paint_image_action, name='paint_image_action'),
    path('show_postil/<int:question_grade_id>', views.show_postil, name='show_postil'),
    path('show_statistics/<int:teacher_id>', views.show_statistics, name='show_statistics'),

    path('index_student/<int:student_id>', views.index_student, name='index_student'),
    path('change_password/<int:student_id>', views.change_password, name='change_password'),
    path('change_password/action/<int:student_id>', views.change_password_action, name='change_password_action'),
    path('do_homework/<int:student_id>', views.do_homework, name='do_homework'),
    path('do_task/<int:student_id>/<int:task_id>', views.do_task, name='do_task'),
    path('do_task/action/<int:student_id>/<int:question_id>/<int:task_id>/<int:counter>', views.do_task_action, name='do_task_action'),
    path('show_image/<int:student_id>/<int:question_id>', views.show_image, name='show_image'),
    path('view_grade/<int:student_id>', views.view_grade, name='view_grade'),
    path('view_task/<int:student_id>/<int:task_id>/<int:task_grade_id>', views.view_task, name='view_task'),
]
