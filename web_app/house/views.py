from django.shortcuts import render
from django.http import HttpResponse
from .models import Devices

def home(request):

    sql = "SELECT * FROM house_devices"
    out = Devices.objects.raw(sql)

    if request.method == 'POST':
        search = request.POST.get('textfield', None)    # raw SQL user input
        search_out = Devices.objects.raw(search)
        return render(request, 'home.html', {'data': search_out})
    else:
        return render(request, 'home.html', {'data': out})


def about(request):
    return render(request, 'about.html')