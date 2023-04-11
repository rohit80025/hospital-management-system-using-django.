from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import *
# Create your views here.


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0;
    p = 0;
    a = 0;
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    d1 = {'d':d, 'p':p, 'a':a}    
    return render(request, 'index.html',d1)


def login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                auth_login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'login.html', {'error': error})


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return render(request, 'login.html')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']

        try:
            Doctor.objects.create(name=n, mobile=c, special=sp)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_doctor.html', {'error': error})


def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


# code for Patient


def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    p_doc = Patient.objects.all()
    d = {'p_doc': p_doc}
    return render(request, 'view_patient.html', d)


def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        pn = request.POST['name']
        pg = request.POST['gender']
        pc = request.POST['mobile']
        pa = request.POST['address']

        try:
            Patient.objects.create(name=pn, gender=pg, mobile=pc, address=pa)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_patient.html', {'error': error})


def delete_patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


# Code for Appointment


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = Appointment.objects.all()
    d = {'appoint': appoint}
    return render(request, 'view_appointment.html', d)

'''
def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date1']
        t1 = request.POST['time1']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(doctor=doctor,
                                       patient=patient,
                                       date=d1,
                                       time=t1)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_appointment.html', {
        'error': error,
        'doctor': doctor1,
        'patient': patient1
    })

'''

def add_appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html', d)

def delete_appointment(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
