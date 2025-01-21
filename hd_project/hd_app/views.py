from unittest import result
from django.shortcuts import redirect, render
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Patient

from joblib import load
classifier = load('./saveModel/classifier.joblib')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def info(request):

    
    if request.method == 'POST':
        # Retrieve form data
        age = request.POST['age']
        sex = request.POST['sex']
        cp = request.POST['cp']
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak = request.POST['oldpeak']
        slope = request.POST['slope']
        ca = request.POST['ca']
        thal = request.POST['thal']
       
        

        prediction = classifier.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak), int(slope), int(ca), int(thal), ]])
        
            
        if prediction[0] == 0:
            prediction ="You are likely to not have heart disease." 
        else:
            prediction = "You are likely to have heart disease."

        mypatient = Patient(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, prediction[0])
        mypatient.save()

        return render(request, 'result.html', {'result': prediction})
    return render(request, 'result.html')

def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')
    return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name  # type: ignore
            return render (request, 'index.html', {'fname': fname})
        
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('index')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('index')
   

def record(request):
    records = Patient.objects.all()
    return render(request, 'record.html',{'records': records })