"""
URL configuration for sitioweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainsite.views import IndexView
from mistareas.views import LoginView, HomeInternalView, ReadTaskView, CreateTaskView, ListAllTaskView, EditTaskView, DeleteTaskView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('internal/home', login_required(HomeInternalView.as_view()), name='home_internal'),
    path('internal/tareas/ver', login_required(ListAllTaskView.as_view()), name='listar_tareas'),
    path('internal/tarea/<int:id_tarea>/ver', login_required(ReadTaskView.as_view()), name='leer_tarea'),
    path('internal/tarea/<int:id_tarea>/editar', login_required(EditTaskView.as_view()), name='editar_tarea'),
    path('internal/tarea/crear', login_required(CreateTaskView.as_view()), name='crear_tarea'),
    path('internal/tarea/<int:pk>/eliminar', login_required(DeleteTaskView.as_view()), name='eliminar_tarea'),
]
