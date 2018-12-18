from django.shortcuts import render, redirect
from clients.forms import ClientSignUp
from django.contrib.auth.decorators import login_required
from clients.models import Client
from jsons.sectors_json_main import Setores
from django.shortcuts import get_object_or_404

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

            return redirect('/')

        else:

            print('Form is invalid')
    else:

        form = ClientSignUp()

    return render(request, 'clients/new_clients.html', {'form': form, 'sectors': list_sectors})

@login_required
def client_show(request):

    return render(request, 'clients/show_client.html')
#
# def client_list(request):
#
#     clients = Client.objects.all()
#
#     data = {}
#     data['object_list'] = clients
#
#     return render(request, 'profile/client_list.html', data)
#

#
# def client_update(request, pk):
#
#     clients = get_object_or_404(Client, pk=pk)
#     list_sectors = Setores.list_sectors()
#     form = ClientSignUp(request.POST or None, instance=clients)
#
#     if form.is_valid():
#
#         clients = form.save(commit=False)
#         clients.save()
#
#         return redirect('client_show',pk=clients.pk)
#
#     else:
#
#         form = ClientSignUp(instance=clients)
#
#     return render(request, 'profile/edit_clients.html', {'clients':clients,'sectors':list_sectors})
#
# def client_delete(request, pk):
#
#     clients = get_object_or_404(Client, pk=pk)
#
#     if request.method=='POST':
#
#         clients.delete()
#
#         return redirect('client_list')
#
#     return render(request, 'profile/client_confirm_delete.html', {'clients':clients})