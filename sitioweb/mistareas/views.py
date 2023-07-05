from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from mistareas.forms import FormularioLogin, FormularioNuevaTarea
from mistareas.models import Tareas, Etiquetas, Estados

# Create your views here.

class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        formulario = FormularioLogin()
        return render(request, self.template_name, {'formulario': formulario, 'title': ' Inicio de sesión',})
    
    def post(self, request, *args, **kwargs):
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home_internal')
            form.add_error('username', 'Se han ingresado las credenciales equivocadas, verifique sus datos de identificación')
            return render(request, self.template_name, { 'form': form,})
        else:
            return render(request, self.template_name, { 'form': form,})
        
class HomeInternalView(TemplateView):
    template_name = 'home_internal.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': '- Inicio',
            'nombre': request.user.first_name,
            'tareas_general' : Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento')
        }
        return render(request, self.template_name, context)
    
class ReadTaskView(TemplateView):

    template_name= 'read_task.html'
    def get(self, request, *args, **kwargs):
        context = {
            'title': '- Ver tarea',
            'nombre': request.user.first_name,
            'tarea' : Tareas.objects.get(id=kwargs['id_tarea']),
        }
        
        return render(request, self.template_name, context)

class CreateTaskView(TemplateView):

    template_name= 'create_task.html'
    def get(self, request, *args, **kwargs):
        context = {
            'title': '- Crear tarea',
            'nombre': request.user.first_name,
            'id': request.user.id,
            'etiquetas' : Etiquetas.objects.all().order_by('id'),
            'estados' : Estados.objects.all().order_by('id'),
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = FormularioNuevaTarea(request.POST)
        id = request.user.id
        if form.is_valid():
            tarea = Tareas(
                titulo = form.cleaned_data['titulo'],
                descripcion = form.cleaned_data['descripcion'],
                fecha_vencimiento = form.cleaned_data['fecha_vencimiento'],
                id_estado = form.cleaned_data['id_estado'],
                id_etiqueta = form.cleaned_data['id_etiqueta'],
                id_User_id = id
            )
            tarea.save()
            return redirect('home_internal')
        else:
            return render(request, self.template_name, { 'form': form,})