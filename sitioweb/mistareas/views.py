from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from mistareas.forms import FormularioLogin, FormularioNuevaTarea, FormularioObservaciones
from mistareas.models import Tareas, Etiquetas, Estados
from django.urls import reverse_lazy

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
            'tareas_general' : Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento').exclude(id_estado_id=3),
            'tareas_completadas' : Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento').filter(id_estado_id=3),
            'mensajes':  request.session.get('mensajes', None),
        }
        request.session.pop('mensajes', None)
        return render(request, self.template_name, context)


## Ver todas las tareas
class ListAllTaskView(TemplateView):
    template_name= 'list_all_tasks.html'
    def get(self, request, *args, **kwargs):
        id_busqueda = request.session.get('id_busqueda', 0)
        if id_busqueda == 0:
            tareas = Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento')
        else:
            # tareas = Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento').filter(id_estado_id=1).filter(id_etiqueta_id=id_busqueda)´
            tareas = Tareas.objects.filter(id_User_id=request.user.id).order_by('fecha_vencimiento').exclude(id_estado_id=3).filter(id_etiqueta_id=id_busqueda)
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


## Ver una tarea, agrega observaciones
class ReadTaskView(TemplateView):
    template_name= 'read_task.html'
    def get(self, request, *args, **kwargs):
        tarea = Tareas.objects.get(id=kwargs['id_tarea'])
        context = {
            'title': '- Ver tarea',
            'nombre': request.user.first_name,
            'tarea' : tarea,
            'form' :  FormularioObservaciones(initial ={'observaciones': tarea.observaciones} ),
            'mensajes':  request.session.get('mensajes', None),
        }
        request.session.pop('mensajes', None)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = FormularioObservaciones(request.POST)
        if form.is_valid():
            tarea = Tareas.objects.get(id=kwargs['id_tarea'])
            tarea.observaciones = form.cleaned_data['observaciones']
            tarea.save()
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha actualizado la observación'}
            return redirect('leer_tarea', id_tarea=kwargs['id_tarea'])
        else:
            request.session['mensajes'] = {'enviado': False, 'resultado': form.errors}
            return redirect('leer_tarea', id_tarea=kwargs['id_tarea'])

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
            'accion': 'crear',
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

## Editar una tarea
class EditTaskView(TemplateView):
    template_name = 'create_task.html'
    
    def get(self, request, *args, **kwargs):
        try:
            tarea = Tareas.objects.get(id=kwargs['id_tarea'])
        except Tareas.DoesNotExist:
            context = {
                'title': '- Error'
            }
            return render(request, 'elemento_no_existe.html', context)
        form = FormularioNuevaTarea(initial = tarea.__dict__)
        context = {
            'title': '- Editar tarea',
            'form': form,
            'accion': 'editar',

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        tarea = Tareas.objects.get(id=kwargs['id_tarea'])
        print(tarea)
        form = FormularioNuevaTarea(request.POST)
        if form.is_valid():
            tarea = Tareas.objects.get(id=kwargs['id_tarea'])
            tarea.titulo = form.cleaned_data['titulo']
            tarea.descripcion = form.cleaned_data['descripcion']
            tarea.fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
            tarea.id_estado = form.cleaned_data['id_estado']
            tarea.id_etiqueta = form.cleaned_data['id_etiqueta']
            tarea.save()
            request.session['mensajes'] = {'enviado': True, 'resultado': 'Has actualizado la tarea exitosamente'}
            return redirect('listar_tareas') 
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        context = {
            'form': form,
            'mensajes': mensajes
        }
        return render(request, self.template_name, context)

## Elimina una tarea
class DeleteTaskView(DeleteView):
    model = Tareas
    template_name = 'eliminar_tarea.html'
    success_url = '/internal/tareas/ver'

## Marcar una tarea como completada
class CompleteTaskView(TemplateView):

    def get(self, request, *args, **kwargs):
        tarea = Tareas.objects.get(id=kwargs['pk'])
        idtarea = kwargs['pk']
        tarea.id_estado = Estados.objects.get(id=3)
        tarea.save()
        request.session['mensajes'] = {'enviado': True, 'resultado': 'Se ha marcado como completada la tarea'}
        return redirect(reverse('leer_tarea', kwargs={'id_tarea': idtarea}))