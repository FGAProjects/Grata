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

    return render(request, 'clients/client_detail.html', {'object':client})

def new_clients(request):

    client = ClientForm(request.POST or None)

    if client.is_valid():

        client.save()

        return HttpResponseRedirect('/')

    else:

        client = ClientForm()

    return render(request, 'clients/new_clients.html', {'client': client})

    # form = ClientForm(request.POST or None)
    #
    # if form.is_valid():
    #
    #     form.save()
    #
    #     return redirect('client_list')
    #
    # return render(request, 'clients/client_form.html', {'form':form})

def client_update(request, pk):

    client = get_object_or_404(Client, pk=pk)

    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():

        form.save()

        return redirect('client_list')

    return render(request, 'clients/client_form.html', {'form':form})

def client_delete(request, pk):

    client = get_object_or_404(Client, pk=pk)

    if request.method=='POST':

        client.delete()

        return redirect('client_list')

    return render(request, 'clients/client_confirm_delete.html', {'object':client})