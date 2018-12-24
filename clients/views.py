from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from clients.forms import ClientSignUp,EditClientForm
from jsons.sectors_json_main import Setores

def new_client(request):

    list_sectors = Setores.list_sectors()

    if request.method == "POST":

        form = ClientSignUp(request.POST)

        if form.is_valid():

            user = form.save()
            user.refresh_from_db()

            user.client.ramal = form.cleaned_data.get('ramal')
            user.client.sector = form.cleaned_data.get('sector')
            user.client.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('username')

            user.username = user.client.email
            user.email = user.client.sector
            user.last_name = user.client.ramal
            user.save()
            messages.success(request, 'O Usuário ' + user.first_name + ' Foi Cadastrado Com Sucesso!')

            return redirect('/')

        else:

            messages.warning(request, 'Houve Algum Com o Formulário. Contate o Desenvolvedor Responsável!')
    else:

        form = ClientSignUp()

    return render(request, 'clients/new_clients.html', {'form': form, 'sectors': list_sectors})

@login_required
def client_show(request):

    return render(request, 'clients/show_client.html')

@login_required
def client_update(request):

    list_sectors = Setores.list_sectors()

    if request.method == "POST":

        form = EditClientForm(request.POST,instance=request.user)

        if form.is_valid():

            user = form.save()
            user.username = form.cleaned_data.get('username')
            user.last_name = form.cleaned_data.get('last_name')
            user.first_name = form.cleaned_data.get('first_name')
            user.email = form.cleaned_data.get('sector')
            user.save()
            messages.success(request, 'Suas informações Foram Alteradas Com Sucesso!')

            return redirect('client_show')

        else:

            messages.warning(request, 'Houve Algum Com o Formulário. Contate o Desenvolvedor Responsável!')

    else:

        form = EditClientForm(request.POST,instance=request.user)

    return render(request,'clients/edit_clients.html',{'sectors':list_sectors,'form':form})

@login_required
def client_delete(request):

    client = User.objects.get(id=request.user.id)

    if request.method == 'POST':

        client.delete()
        messages.success(request, 'Usuário Excluído Com Sucesso')
        return redirect('logout')

    return render(request, 'clients/delete_client.html', {'client': client})


@login_required
def list_users(request):

    client = User.objects.all()

    """
        Aqui vai pegar todos os usuários para adicionar a reunião
    """
    pass