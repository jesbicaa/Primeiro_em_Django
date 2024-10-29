from django.shortcuts import render
from .models import User

def home(request):
    return render(request,'users/home.html')

def users(request):
    #salvar dados da tela no BD
    novo_user = User()
    novo_user.nome = request.POST.get('nome')    
    novo_user.idade = request.POST.get('idade')
    novo_user.save()

    #exibir todos os user já cadastrados em uma nova pagina
    users = {
        'users': User.objects.all()
    }

    #retornar os dados para pagina
    return render(request, 'users/users.html', users)
