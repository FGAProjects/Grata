from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from clients.models import Client

class ClientForm(ModelForm):

    class Meta:

        model = Client
        fields = ['name', 'ramal', 'sector', 'email', 'permission']

def client_list(request):

    client = Client.objects.all()

    data = {}
    data['object_list'] = client

    return render(request, 'clients/client_list.html', data)

def client_show(request, pk):

    client = get_object_or_404(Client, pk=pk)

    return render(request, 'clients/client_detail.html', {'object':client})

def client_new(request):

    form = ClientForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('client_list')

    return render(request, 'clients/client_form.html', {'form':form})

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