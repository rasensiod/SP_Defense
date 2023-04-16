from django.shortcuts import render
from django.db import connection, DataError, ProgrammingError, OperationalError
from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
from .models import Patients
from hospital.sqli_alert.notification import *

security = 3

def home(request):

    out_bad = 0
    out_start = 1

    if request.method == 'POST':
        user_input = request.POST.get('textfield', None)    # user input

        try:
            # No security: raw SQL query implemented
            if security == 0:
                search = 'SELECT * FROM hospital_patients WHERE secret_id=' + user_input
                search_out = Patients.objects.raw(search)

            # Security: using Django's ORM to escape user input
            elif security == 1:
                search = 'SELECT * FROM hospital_patients WHERE secret_id=' + user_input
                search_out = Patients.objects.filter(secret_id=user_input)

            # Security: using parameterised queries
            elif security == 2:
                search = 'SELECT * FROM hospital_patients WHERE secret_id=%s'
                with connection.cursor() as cursor:
                    cursor.execute(search, (user_input,))
                    search_out = cursor.fetchall()

            # Security: feeding raw query to ML model
            elif security == 3:
                search = ('SELECT * FROM hospital_patients WHERE secret_id=' + user_input)
                search_out = Patients.objects.raw(search)

                model = load('hospital/sqli_ml/model.joblib')
                vectorizer = load('hospital/sqli_ml/vectorizer.joblib')

                search_v = vectorizer.transform([search])
                flag = model.predict(search_v)

                if flag == 1:
                    print("Error: Possible SQL injection detected.")
                    notification(search)
                    return render(request, 'home.html', {'data': out_bad, 'security': security})
            
            # Try block to check if patient is in DB
            try:
                if security == 2: # tuple does not have attribute id
                    if len(search_out) == 0:
                        return render(request, 'home.html', {'data': out_bad, 'security': security})
                    else:
                        return render(request, 'home.html', {'data': search_out, 'security': security})
                else: # for all other security systems
                    patient_check = search_out[0].id
                    return render(request, 'home.html', {'data': search_out, 'security': security})
            except IndexError:
                return render(request, 'home.html', {'data': out_bad, 'security': security})
    
        # Check if input is invalid and might be an SQL injection
        except (DataError, ProgrammingError, ValueError, OperationalError) as e:
            print("Error: Possible SQL injection detected.")
            print(e)
            notification(search)
            return render(request, 'home.html', {'data': out_bad, 'security': security})
    else:
        return render(request, 'home.html', {'data': out_start, 'security': security})



def about(request):

    sql = "SELECT * FROM hospital_patients"
    out = Patients.objects.raw(sql)

    return render(request, 'about.html', {'data': out})