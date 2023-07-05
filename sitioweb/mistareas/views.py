from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from mistareas.forms import FormularioLogin, FormularioNuevaTarea
from mistareas.models import Tareas, Etiquetas, Estados

# Create your views here.

## Acceso al sitio
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
        
## Pagina Interna
class HomeInternalView(TemplateView):
    template_name = 'home_internal.html'

    def get(self, request, *args, **kwargs):
    
        context = {
            'title': '- Inicio',
            'nombre': request.user.first_name,
            'tareas_general' : Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento'),
            'mensajes':  request.session.get('mensajes', None),
        }
        request.session.pop('mensajes', None)
        return render(request, self.template_name, context)
    
## Ver una tarea
class ReadTaskView(TemplateView):
    template_name= 'read_task.html'
    def get(self, request, *args, **kwargs):
        context = {
            'title': '- Ver tarea',
            'nombre': request.user.first_name,
            'tarea' : Tareas.objects.get(id=kwargs['id_tarea']),
        }
        return render(request, self.template_name, context)

## Crear una tarea
class CreateTaskView(TemplateView):
    template_name= 'create_task.html'
    def get(self, request, *args, **kwargs):
        context = {
            'title': '- Crear tarea',
            'nombre': request.user.first_name,
            'id': request.user.id,
            'etiquetas' : Etiquetas.objects.all().order_by('id'),
            'estados' : Estados.objects.all().order_by('id'),
            'form': FormularioNuevaTarea(),
            'mensajes':  request.session.get('mensajes', None),
        }
        request.session.pop('mensajes', None)
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
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha creado la tarea'}
            return redirect('home_internal')
        else:
            request.session['mensajes'] = {'enviado': False, 'resultado': form.errors}
            return redirect('crear_tarea')
        
## Ver todas las tareas
class ListAllTaskView(TemplateView):
    template_name= 'list_all_tasks.html'
    def get(self, request, *args, **kwargs):
        id_busqueda = request.session.get('id_busqueda', 0)
        if id_busqueda == 0:
            tareas = Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento')
        else:
            tareas = Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento').filter(id_estado_id=1).filter(id_etiqueta_id=id_busqueda)
        request.session.pop('id_busqueda', None)
        context = {
            'title': '- Ver tarea',
            'nombre': request.user.first_name,
            'tareas': tareas,
            'etiquetas' : Etiquetas.objects.all().order_by('id'),
            'mensajes':  request.session.get('mensajes', None),
        }
        request.session.pop('mensajes', None)
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha filtrado la búsqueda'}        
        request.session['id_busqueda'] = request.POST.get('id_etiqueta')
        return redirect('listar_tareas')
