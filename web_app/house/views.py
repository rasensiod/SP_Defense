from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

    sql = "SELECT * FROM house_devices"
    out = Devices.objects.raw(sql)

    print(posts)

    return render(request, 'home.html', {'data': out})

def about(request):
    return render(request, 'about.html')