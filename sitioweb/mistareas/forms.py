from django import forms
from django.forms import ModelForm, TextInput, Textarea
from mistareas.models import Tareas, Estados, Etiquetas, Prioridades
from django.contrib.auth.models import User, Group

class DateInput(forms.DateInput):
    input_type = 'date'
    

#Formulario de login
class FormularioLogin(forms.Form):
    username = forms.CharField          (label='Usuario', required=True,
                                        max_length=30, min_length=5,
                                        error_messages={
                                            'required': 'El usuario es obligatorio',
                                            'max_length': 'El nombre de usuario no puede ser superior a los 30 caracteres',
                                            'min_length': 'El nombre de usuario debe tener al menos 5 caracteres'
                                        },
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Por favor, ingrese su nombre de usuario',
                                            'class': 'form-control'
                                        })
                                        )
    password = forms.CharField          (label='Contraseña', required=True,
                                        max_length=30, min_length=1,
                                        error_messages={
                                            'required': 'La contraseña es obligatoria',
                                            'max_length': 'La contraseña no puede superar los 30 caracteres',
                                            'min_length': 'La contraseña debe tener al menos 1 caracter'
                                        },
                                        widget=forms.PasswordInput(attrs={
                                            'placeholder': 'Por favor, ingrese su contraseña',
                                            'class': 'form-control'
                                        })
                                        )

class FormularioNuevaTarea(forms.Form):
    titulo = forms.CharField            (label='Titulo', required=True,
                                            widget=forms.TextInput(attrs={
                                            'placeholder': 'Ingrese un título',
                                            'class': 'form-control'
                                        })
                                        )
    descripcion = forms.CharField       (label='Descripcion', required=True,
                                            widget=forms.TextInput(attrs={
                                            'placeholder': 'Ingrese un descripción',
                                            'class': 'form-control'
                                        })
                                        )
    fecha_vencimiento = forms.DateField (label='Fecha Vencimiento', required=True, widget=DateInput(attrs={'class': 'form-control'}))
    id_estado = forms.ModelChoiceField  (label='Estado', empty_label=('Seleccione una estado'),
                                        queryset=Estados.objects.all().order_by('id'), required=True, 
                                        widget= forms.Select(attrs={
                                            'class':'form-select'}),)
    id_prioridad = forms.ModelChoiceField(label='Prioridad', empty_label=('Seleccione una prioridad'),
                                        queryset=Prioridades.objects.all().order_by('id'), required=True, 
                                        widget= forms.Select(attrs={
                                            'class':'form-select'}),)
    id_etiqueta = forms.ModelChoiceField(label='Etiqueta', empty_label=('Seleccione una etiqueta'),
                                        queryset=Etiquetas.objects.all().order_by('id'), required=True, 
                                        widget= forms.Select(attrs={
                                            'class':'form-select'}),)
    id_usuario = forms.ModelChoiceField (label='Asignar tarea a usuario', empty_label=('Seleccione un usuario'),
                                        queryset=User.objects.all().order_by('id'), required=True, 
                                        widget= forms.Select(attrs={
                                            'class':'form-select'}),)
    
    
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion', 'id_usuario', 'fecha_creacion', 'fecha_vencimiento', 'id_estado', 'id_etiqueta', 'id_prioridad']

class FormularioObservaciones(forms.Form):
    observaciones = forms.CharField     (label='Observaciones', required=True,
                                            widget=forms.Textarea(attrs={
                                            'class': 'form-control',
                                            'rows': 4, 
                                            'placeholder': 'Ingrese acá la observación'
                                        })
                                        )
    
    class Meta:
        model = Tareas
        fields = ['observaciones']