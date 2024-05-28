from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa
from .forms import EmpresaForm, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
def signup_view(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('empresa_list') # Redirecionar para a página inicial após o registro
    else:
        form = UserProfile()
    return render(request, 'cadastra.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('empresa_list') # Redirecionar para a página inicial após o login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') # Redirecionar para a página de login após o logout

@login_required(login_url='login')
def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresa_list.html', {'empresas': empresas})

@login_required(login_url='login')
def empresa_detail(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, 'empresa_detail.html', {'empresa': empresa})

@user_passes_test(lambda u: u.is_staff, login_url='empresa_list')
def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')
    else:
        form = EmpresaForm()
    return render(request, 'empresa_form.html', {'form': form})

@user_passes_test(lambda u: u.is_staff, login_url='empresa_list')
def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            empresa = form.save()
            return redirect('empresa_detail', pk=empresa.pk)
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresa_form.html', {'form': form})

@user_passes_test(lambda u: u.is_staff, login_url='empresa_list')
def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect('empresa_list')
    return render(request, 'empresa_confirm_delete.html', {'empresa': empresa})
