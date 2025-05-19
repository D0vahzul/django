from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("create-admin/", views.create_admin_user),
    path("migrate/", views.run_migrate),
]

