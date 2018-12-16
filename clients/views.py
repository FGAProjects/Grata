import json

from jsons.sectors_json_main import Setores

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from clients.models import Client
from clients.forms import ClientForm

def client_list(request):

    client = Client.objects.all()

    data = {}
    data['object_list'] = client

    return render(request, 'clients/client_list.html', data)

def client_show(request, pk):

    client = get_object_or_404(Client, pk=pk)

    return render(request, 'clients/show_client.html', {'client':client})

def new_clients(request):

    list_sectors = Setores.list_sectors()
    client = ClientForm(request.POST or None)

    if client.is_valid():

        client.save()

        return HttpResponseRedirect('/')

    else:

        client = ClientForm()

    return render(request, 'clients/new_clients.html', {'client': client,'sectors':list_sectors})

def client_update(request, pk):

    client = get_object_or_404(Client, pk=pk)
    list_sectors = Setores.list_sectors()
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():

        client = form.save(commit=False)
        client.save()

        return redirect('client_show',pk=client.pk)

    else:

        form = ClientForm(instance=client)

    return render(request, 'clients/edit_clients.html', {'client':client,'sectors':list_sectors})

def client_delete(request, pk):

    client = get_object_or_404(Client, pk=pk)

    if request.method=='POST':

        client.delete()

        return redirect('client_list')

    return render(request, 'clients/client_confirm_delete.html', {'client':client})