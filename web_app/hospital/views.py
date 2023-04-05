from django.shortcuts import render
from django.http import HttpResponse
from .models import Patients

def home(request):

    sql = "SELECT * FROM hospital_patients"
    out = Patients.objects.raw(sql)

    if request.method == 'POST':
        search = request.POST.get('textfield', None)    # raw SQL user input
        search = ('SELECT * FROM hospital_patients WHERE secret_id= "'+search+'"')
        search_out = Patients.objects.raw(search)
        return render(request, 'home.html', {'data': search_out})
    else:
        return render(request, 'home.html', {'data': out})


def about(request):
    return render(request, 'about.html')