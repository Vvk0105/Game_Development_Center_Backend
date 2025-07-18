from django.urls import path
from .views import register_user, admin_login, students_list, delete_student, admin_logout_view

urlpatterns = [
    path('register/', register_user, name='register-user'),
    path('admin-login/', admin_login),
    path('students/', students_list),
    path('students/<int:pk>/delete/', delete_student),
    path('admin/logout/', admin_logout_view, name='admin_logout'),
]
