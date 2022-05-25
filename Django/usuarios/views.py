from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('campo nome não pode ser em branco')
            return redirect('cadastro')

        if not email.strip():
            print('campo email não pode ser em branco')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas não correspondem')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('usuário ja cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def dashboard(request):
    pass


def logout(request):
    pass
