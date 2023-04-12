from django.shortcuts import render
from django.db import connection, DataError, ProgrammingError
from .models import Patients

security = 2

def home(request):

    sql = "SELECT * FROM hospital_patients"
    out = Patients.objects.raw(sql)
    sql_bad = "SELECT * FROM hospital_patients WHERE secret_id=88888"
    out_bad = Patients.objects.raw(sql_bad)

    if request.method == 'POST':
        user_input = request.POST.get('textfield', None)    # user input

        try:
            if security == 0:
                search = ('SELECT * FROM hospital_patients WHERE secret_id=' + user_input)
                search_out = Patients.objects.raw(search)

            elif security == 1:
                search_out = Patients.objects.filter(secret_id=user_input)
                print(search_out)

            elif security == 2:
                search = 'SELECT * FROM hospital_patients WHERE secret_id=%s'
                with connection.cursor() as cursor:
                    cursor.execute(search, (user_input,))
                    search_out = cursor.fetchall()

            return render(request, 'home.html', {'data': search_out, 'security': security})
    
        except (DataError, ProgrammingError, ValueError) as e:
            print("Error: Possible SQL injection detected.")
            return render(request, 'home.html', {'data': out_bad, 'security': security})
    else:
        return render(request, 'home.html', {'data': out, 'security': security})


    # sql = "SELECT * FROM hospital_patients"
    # out = Patients.objects.raw(sql)

    # if request.method == 'POST':
    #     user_input = request.POST.get('textfield', None)    # user input
    #     if security == 0:
    #         search = ('SELECT * FROM hospital_patients WHERE secret_id=' + user_input)
    #         search_out = Patients.objects.raw(search)
    #     elif security == 1:
    #         search_out = Patients.objects.filter(secret_id=user_input)
    #     return render(request, 'home.html', {'data': search_out})
    # else:
    #     return render(request, 'home.html', {'data': out})


def about(request):
    return render(request, 'about.html')