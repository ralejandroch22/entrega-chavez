from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from users.forms import UserRegisterForm, UserEditForm
from users.models import Avatar

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                print(f"INICIO DE SESION EXITOSO DE {user.username}\n")
                return render(request, "stock/index.html")

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"stock/index.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():

            if miFormulario.cleaned_data.get('imagen'):
                if Avatar.objects.filter(user = usuario).exists():

                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    avatar = Avatar(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()

            miFormulario.save()
            return render(request, "stock/index.html")
    else:

        miFormulario = UserEditForm(initial = {'imagen': usuario.avatar.imagen},instance=request.user)

    return render(request, "users/editar_perfil.html", {"form": miFormulario, "usuario": usuario })

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name= 'users/editar_pass.html'
    success_url = reverse_lazy("EditarPerfil")