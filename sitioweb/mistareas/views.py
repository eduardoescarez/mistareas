from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from mistareas.forms import FormularioLogin

# Create your views here.

class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        formulario = FormularioLogin()
        return render(request, self.template_name, {'formulario': formulario, 'titulo': 'Acceso al sitio Interno',})
    
    def post(self, request, *args, **kwargs):
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.user.groups.filter(name='trabajadores').exists():
                        return redirect('hometrabajadores')
                    elif request.user.groups.filter(name='clientes').exists():
                        return redirect('homeclientes')
                    else:
                        return redirect('index')
            form.add_error('username', 'Se han ingresado las credenciales equivocadas, verifique sus datos de identificación')
            return render(request, self.template_name, { 'form': form,})
        else:
            return render(request, self.template_name, { 'form': form,})
        
