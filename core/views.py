from django.shortcuts import render, redirect
from django.contrib.auth import authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout 


def acceder(request):
    """ página de acceso """

    form = AuthenticationForm(data=request.POST)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
    

    return render(request, 'core/login.html', {'form': form})

def salir(request):
    """ Cerrar sesión en el sitio """

    logout(request)
    return redirect('/')