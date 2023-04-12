from django.shortcuts import render
from django.db import connection, DataError, ProgrammingError, OperationalError
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
from .models import Patients

security = 3

def home(request):

    sql = "SELECT * FROM hospital_patients"
    out = Patients.objects.raw(sql)
    # sql_bad = "SELECT * FROM hospital_patients WHERE secret_id=88888"
    # out_bad = Patients.objects.raw(sql_bad)
    out_bad = 0

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

            elif security == 3:
                search = ('SELECT * FROM hospital_patients WHERE secret_id=' + user_input)
                search_out = Patients.objects.raw(search)
                print(search_out)

                model = load('hospital/sqli_ml/model.joblib')
                vectorizer = load('hospital/sqli_ml/vectorizer.joblib')

                search_v = vectorizer.transform([search])
                flag = model.predict(search_v)
                print(flag)

                if flag == 1:
                    print("Error: Possible SQL injection detected.")
                    return render(request, 'home.html', {'data': out_bad, 'security': security})
            
            return render(request, 'home.html', {'data': search_out, 'security': security})
    
        except (DataError, ProgrammingError, ValueError, OperationalError) as e:
            print("Error: Possible SQL injection detected.")
            print(e)
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